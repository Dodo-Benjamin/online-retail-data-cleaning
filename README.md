# 📊 Online Retail Data Analysis

## 🚀 Application interactive

**Explorez les données de vente grâce à un tableau de bord interactif développé avec Python, Streamlit et Plotly.**

👉 **Accéder au tableau de bord en ligne**

## 📌 Présentation du projet

Ce projet consiste à analyser les données d'une entreprise de vente au détail en ligne afin d'identifier les tendances commerciales, les produits les plus performants, les principaux marchés et les comportements des clients.

Il couvre plusieurs étapes d'un projet réel d'analyse de données : nettoyage, analyse SQL, visualisation, segmentation client et création d'une application web interactive.

## 🎯 Objectifs

- Nettoyer et structurer un jeu de données commerciales.
- Analyser les ventes à l'aide de SQL et SQLite.
- Identifier les tendances mensuelles et les performances par pays et par produit.
- Réaliser une segmentation des clients avec la méthode RFM.
- Concevoir un tableau de bord interactif destiné aux décideurs métiers.
- Présenter les résultats et formuler des recommandations commerciales.

## 🛠️ Technologies utilisées

- **Python** : langage de programmation.
- **Pandas** : nettoyage, préparation et analyse des données.
- **SQLite et SQL** : interrogation et analyse des données.
- **Matplotlib et Seaborn** : visualisation exploratoire.
- **Plotly** : graphiques interactifs.
- **Streamlit** : création et déploiement du tableau de bord.
- **Jupyter Notebook** : exploration et documentation des analyses.
- **GitHub** : versionnement et partage du projet.

## 📂 Structure du projet

```text
online-retail-data-analysis/
│
├── app.py
├── requirements.txt
├── cleaned_data.zip
├── README.md
├── 01_clean_and_structure.ipynb
├── 02_sql_analysis.ipynb
├── 03_visualizations.ipynb
└── 04_analyse_approfondie.ipynb
```

*Cette structure est indicative : adaptez-la aux noms et emplacements réellement présents dans le dépôt.*

## 🧹 Étape 1 — Nettoyage des données

Notebook : `01_clean_and_structure.ipynb`

Travaux réalisés :

- Suppression des doublons exacts.
- Conversion des dates au format datetime.
- Normalisation des données textuelles.
- Examen des quantités et prix négatifs.
- Gestion des valeurs manquantes.
- Exportation des données nettoyées.

Le jeu de données nettoyé comporte 536 641 lignes et 8 colonnes.

## 🗄️ Étape 2 — Analyse SQL

Notebook : `02_sql_analysis.ipynb`

L'analyse avec SQL et SQLite permet notamment d'étudier :

- Les produits générant le plus de chiffre d'affaires.
- L'évolution mensuelle des ventes.
- Les performances commerciales par pays.
- La fréquence des achats.
- Les indicateurs de performance des commandes.

## 📈 Étape 3 — Visualisation des données

Notebook : `03_visualizations.ipynb`

Création de graphiques permettant de comprendre :

- L'évolution du chiffre d'affaires dans le temps.
- Les principaux pays contributeurs.
- Les périodes d'activité commerciale.
- La distribution des montants des commandes.
- Les habitudes d'achat des clients.

## 👥 Étape 4 — Analyse approfondie et segmentation RFM

Notebook : `04_analyse_approfondie.ipynb`

La méthode RFM repose sur trois indicateurs :

- **Recency (R)** : ancienneté du dernier achat.
- **Frequency (F)** : fréquence des achats.
- **Monetary (M)** : montant total dépensé.

Cette méthode permet de distinguer différents segments de clients et de proposer des actions commerciales adaptées à leurs comportements.

## 📊 Tableau de bord Streamlit

L'application interactive permet d'explorer les données filtrées et d'afficher :

- Le chiffre d'affaires.
- Le nombre de commandes.
- Le nombre de clients identifiés.
- Le panier moyen par commande.
- L'évolution mensuelle des ventes.
- Les principaux pays et produits.
- Des recommandations commerciales fondées sur les données sélectionnées.

Les utilisateurs peuvent filtrer les résultats par pays, période et produit.

👉 **[Ouvrir l'application Streamlit](COLLER_ICI_LE_LIEN_STREAMLIT)**

## 💡 Valeur métier

Cette analyse peut aider une entreprise à :

- Repérer les marchés les plus performants.
- Comprendre l'évolution des ventes.
- Identifier les produits qui contribuent le plus au chiffre d'affaires.
- Adapter ses actions de fidélisation selon les segments RFM.
- Faciliter la prise de décision grâce à des indicateurs visuels.

Les recommandations doivent être complétées par une analyse des marges, des coûts et du contexte commercial avant toute décision d'investissement.

## ▶️ Exécuter l'application en local

### 1. Cloner le dépôt

```bash
git clone https://github.com/Dodo-Benjamin/online-retail-data-cleaning.git
cd online-retail-data-cleaning
```

### 2. Installer les dépendances

```bash
python -m pip install -r requirements.txt
```

### 3. Préparer les données

Placer le fichier CSV nettoyé à un emplacement reconnu par `app.py`, par exemple dans le dossier `data/`, ou conserver l'archive ZIP à la racine si elle est prise en charge par la version de l'application.

### 4. Lancer le tableau de bord

```bash
python -m streamlit run app.py
```

Le tableau de bord s'ouvrira dans le navigateur.

## ☁️ Déploiement

L'application est publiée avec Streamlit Community Cloud.

Pour déployer une nouvelle version, consulter :

[https://share.streamlit.io/](https://share.streamlit.io/)

## 🧠 Compétences démontrées

- Nettoyage et préparation des données.
- Analyse exploratoire des données.
- Requêtes SQL et utilisation de SQLite.
- Analyse commerciale et segmentation RFM.
- Création de visualisations.
- Développement d'un tableau de bord interactif.
- Déploiement d'une application Python.
- Documentation et gestion d'un projet avec GitHub.

## 👨‍💻 Auteur

**Benjamin Dodo**

Projet de portfolio en analyse de données, réalisé dans le cadre de mon apprentissage des outils Python, SQL et de la Business Intelligence.

🔗 **Dépôt GitHub :**
[https://github.com/Dodo-Benjamin/online-retail-data-cleaning](https://github.com/Dodo-Benjamin/online-retail-data-cleaning)

