from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st

# --------------------------------------------------
# 1. Configuration
# --------------------------------------------------
st.set_page_config(
    page_title="Online Retail | Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Online Retail Data Analysis")
st.caption(
    "Tableau de bord interactif — Analyse des ventes, des clients "
    "et des performances commerciales"
)

# --------------------------------------------------
# 2. Chargement des données
# --------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent

candidats = [
    BASE_DIR / "data" / "cleaned_data.csv",
    BASE_DIR / "données" / "cleaned_data.csv",
    BASE_DIR / "cleaned_data.csv",
    BASE_DIR / "data" / "online_retail_cleaned.csv",
    BASE_DIR / "cleaned_data.zip",
    BASE_DIR / "data" / "cleaned_data.zip",
]


fichier = next((p for p in candidats if p.exists()), None)

if fichier is None:
    st.error(
        "Fichier de données introuvable. Place cleaned_data.csv "
        "dans le dossier data/ du projet."
    )
    st.stop()


@st.cache_data
def charger_donnees(chemin):
    data = pd.read_csv(chemin)
    data["InvoiceDate"] = pd.to_datetime(
        data["InvoiceDate"], errors="coerce"
    )
    data["Quantity"] = pd.to_numeric(
        data["Quantity"], errors="coerce"
    )
    data["UnitPrice"] = pd.to_numeric(
        data["UnitPrice"], errors="coerce"
    )
    data["CustomerID"] = pd.to_numeric(
        data["CustomerID"], errors="coerce"
    )
    data["InvoiceNo"] = data["InvoiceNo"].astype("string")
    data["Country"] = data["Country"].fillna("Inconnu")
    data["Description"] = data["Description"].fillna("Non renseigné")
    return data


df = charger_donnees(str(fichier))

# Exclure les retours, annulations et montants non positifs
ventes = df[
    (df["Quantity"] > 0)
    & (df["UnitPrice"] > 0)
    & (~df["InvoiceNo"].str.startswith("C", na=False))
    & df["InvoiceDate"].notna()
].copy()

ventes["ChiffreAffaires"] = (
    ventes["Quantity"] * ventes["UnitPrice"]
)

if ventes.empty:
    st.warning("Aucune vente exploitable dans le fichier.")
    st.stop()

# --------------------------------------------------
# 3. Filtres interactifs
# --------------------------------------------------
st.sidebar.header("🔎 Filtres")

pays_disponibles = sorted(ventes["Country"].unique())
pays_selectionnes = st.sidebar.multiselect(
    "Pays",
    options=pays_disponibles,
    default=pays_disponibles
)

date_min = ventes["InvoiceDate"].min().date()
date_max = ventes["InvoiceDate"].max().date()

periode = st.sidebar.date_input(
    "Période des ventes",
    value=(date_min, date_max),
    min_value=date_min,
    max_value=date_max
)

produits = sorted(
    ventes["Description"].dropna().unique().tolist()
)
produits_selectionnes = st.sidebar.multiselect(
    "Produits (laisser vide pour tous)",
    options=produits
)

filtre = ventes[
    ventes["Country"].isin(pays_selectionnes)
].copy()

if len(periode) == 2:
    debut, fin = periode
    filtre = filtre[
        (filtre["InvoiceDate"].dt.date >= debut)
        & (filtre["InvoiceDate"].dt.date <= fin)
    ]

if produits_selectionnes:
    filtre = filtre[
        filtre["Description"].isin(produits_selectionnes)
    ]

if filtre.empty:
    st.warning("Aucune vente ne correspond à ces filtres.")
    st.stop()

# --------------------------------------------------
# 4. Résumé : indicateurs clés
# --------------------------------------------------
chiffre_affaires = filtre["ChiffreAffaires"].sum()
commandes = filtre["InvoiceNo"].nunique()
clients = filtre["CustomerID"].nunique()

ca_par_commande = filtre.groupby("InvoiceNo")[
    "ChiffreAffaires"
].sum()
panier_moyen = ca_par_commande.mean() if len(ca_par_commande) else 0

c1, c2, c3, c4 = st.columns(4)

c1.metric("Chiffre d'affaires", f"{chiffre_affaires:,.2f} £")
c2.metric("Commandes", f"{commandes:,}")
c3.metric("Clients identifiés", f"{clients:,}")
c4.metric("Panier moyen", f"{panier_moyen:,.2f} £")

st.caption(
    "Les indicateurs sont calculés sur les ventes positives filtrées. "
    "Les commandes sans CustomerID ne sont pas comptées comme clients identifiés."
)

# --------------------------------------------------
# 5. Principaux résultats
# --------------------------------------------------
st.header("📈 Principaux résultats")

ventes["Mois"] = ventes["InvoiceDate"].dt.to_period("M").astype(str)
filtre["Mois"] = filtre["InvoiceDate"].dt.to_period("M").astype(str)

ca_mensuel = (
    filtre.groupby("Mois", as_index=False)["ChiffreAffaires"]
    .sum()
)

top_produits = (
    filtre.groupby("Description", as_index=False)["ChiffreAffaires"]
    .sum()
    .nlargest(10, "ChiffreAffaires")
    .sort_values("ChiffreAffaires")
)

top_pays = (
    filtre.groupby("Country", as_index=False)["ChiffreAffaires"]
    .sum()
    .nlargest(10, "ChiffreAffaires")
    .sort_values("ChiffreAffaires")
)

gauche, droite = st.columns(2)

with gauche:
    fig_mois = px.line(
        ca_mensuel,
        x="Mois",
        y="ChiffreAffaires",
        markers=True,
        title="Évolution mensuelle du chiffre d'affaires",
        labels={
            "Mois": "Mois",
            "ChiffreAffaires": "Chiffre d'affaires (£)"
        }
    )
    st.plotly_chart(fig_mois, use_container_width=True)

with droite:
    fig_pays = px.bar(
        top_pays,
        x="ChiffreAffaires",
        y="Country",
        orientation="h",
        title="Top 10 des pays par chiffre d'affaires",
        labels={
            "Country": "Pays",
            "ChiffreAffaires": "Chiffre d'affaires (£)"
        }
    )
    st.plotly_chart(fig_pays, use_container_width=True)

fig_produits = px.bar(
    top_produits,
    x="ChiffreAffaires",
    y="Description",
    orientation="h",
    title="Top 10 des produits par chiffre d'affaires",
    labels={
        "Description": "Produit",
        "ChiffreAffaires": "Chiffre d'affaires (£)"
    }
)
st.plotly_chart(fig_produits, use_container_width=True)

# --------------------------------------------------
# 6. Recommandations
# --------------------------------------------------
st.header("💡 Recommandations commerciales")

meilleur_pays = filtre.groupby("Country")[
    "ChiffreAffaires"
].sum().idxmax()

meilleur_produit = filtre.groupby("Description")[
    "ChiffreAffaires"
].sum().idxmax()

st.markdown(
    f"""
    - **Marchés :** le pays générant le plus de chiffre d'affaires
      dans la sélection est **{meilleur_pays}**. Étudier les facteurs
      de cette performance avant d'y renforcer les investissements.
    - **Produits :** **{meilleur_produit}** est le produit qui génère
      le plus de chiffre d'affaires dans la sélection. Vérifier sa
      marge et la stabilité de sa demande avant de décider des stocks.
    - **Suivi :** surveiller l'évolution mensuelle pour repérer les
      périodes fortes et adapter les actions commerciales.
    """
)

# --------------------------------------------------
# 7. Aperçu des données
# --------------------------------------------------
with st.expander("Afficher les données filtrées"):
    st.dataframe(
        filtre[
            [
                "InvoiceNo", "InvoiceDate", "Description",
                "Quantity", "UnitPrice", "Country",
                "CustomerID", "ChiffreAffaires"
            ]
        ],
        use_container_width=True
    )

st.caption("Projet portfolio — Python, Pandas, Streamlit et Plotly")
