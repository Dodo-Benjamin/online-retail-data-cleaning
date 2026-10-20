# Projet Python - Nettoyage et Structuration des données

## Description
# 🛒 Online Retail Data Analysis

## 📌 Présentation du projet

Ce projet consiste à analyser un jeu de données de ventes en ligne afin d'en extraire des informations utiles à la prise de décision commerciale.

L'objectif est de transformer des données brutes en données fiables, de réaliser des analyses SQL et de produire des visualisations permettant de comprendre les performances commerciales, le comportement des clients et l'évolution des ventes.

Ce projet s'inscrit dans mon parcours d'apprentissage en **Data Analytics**, avec une mise en pratique des outils utilisés dans les projets réels d'analyse de données.

## 🎯 Objectifs

- Nettoyer et structurer un jeu de données de ventes.
- Identifier et traiter les doublons et les valeurs manquantes.
- Manipuler et analyser les données avec Python et Pandas.
- Utiliser SQL pour répondre à des questions métier.
- Étudier l'évolution du chiffre d'affaires et les performances par pays.
- Analyser les heures de pointe, la fidélité des clients et les montants des commandes.
- Présenter les résultats à l'aide de graphiques clairs et professionnels.

## 📊 Jeu de données

Le projet utilise le jeu de données **Online Retail**, qui contient des informations sur les transactions d'une entreprise de vente en ligne.

Après le nettoyage, le jeu de données contient :

- **536 641 lignes**
- **8 colonnes**
- **0 doublon exact restant**

Les principales variables sont :

| Colonne | Description |
|---|---|
| `InvoiceNo` | Numéro de facture |
| `StockCode` | Code du produit |
| `Description` | Description du produit |
| `Quantity` | Quantité vendue |
| `InvoiceDate` | Date et heure de la transaction |
| `UnitPrice` | Prix unitaire |
| `CustomerID` | Identifiant du client |
| `Country` | Pays du client |

Les valeurs manquantes et les transactions particulières sont examinées pendant le nettoyage. Les quantités négatives sont conservées pour représenter les retours ou annulations potentiels, tandis que les analyses de ventes positives appliquent des filtres adaptés.

## 🛠️ Technologies utilisées

- **Python** : langage de programmation.
- **Pandas** : manipulation et nettoyage des données.
- **SQLite** : stockage local et analyse SQL.
- **Matplotlib** : création de graphiques.
- **Seaborn** : visualisations statistiques.
- **Jupyter Notebook** : environnement de travail.
- **GitHub** : gestion et partage du projet.

## 📁 Structure du projet

```text
online-retail-data-cleaning/
│
├── data/
│   ├── raw_data.csv
│   ├── cleaned_data.csv
│   └── cleaned_data.zip
│
├── notebooks/
│   ├── 01_clean_and_structure.ipynb
│   ├── 02_sql_analysis.ipynb
│   └── 03_visualizations.ipynb
│
├── analysis.db
└── README.md
```

*Remarque : les fichiers et dossiers présentés correspondent à la structure cible. Adapte cette arborescence aux fichiers réellement présents dans ton dépôt. Le jeu de données nettoyé peut être distribué sous forme d'archive ZIP.*

## 🧹 Étape 1 — Nettoyage des données

Le notebook `01_clean_and_structure.ipynb` présente les opérations de préparation des données :

- Chargement et exploration du jeu de données.
- Détection et suppression des doublons exacts.
- Conversion de `InvoiceDate` au format datetime.
- Normalisation des valeurs textuelles.
- Examen des valeurs manquantes et des valeurs atypiques.
- Exportation des données nettoyées.

**Résultat :** un jeu de données structuré de 536 641 lignes et 8 colonnes, sans doublon exact restant.

## 🗄️ Étape 2 — Analyse SQL

Le notebook `02_sql_analysis.ipynb` utilise SQLite pour répondre à plusieurs questions métier :

- Quels pays génèrent le plus de chiffre d'affaires ?
- À quelles heures les commandes sont-elles les plus fréquentes ?
- Quelle est la proportion de clients fidèles et occasionnels ?
- Quel est le montant moyen d'une commande ?
- Comment le chiffre d'affaires évolue-t-il chaque mois ?

Ces analyses reposent notamment sur les requêtes SQL, les agrégations, les regroupements et les fonctions de dates.

## 📈 Étape 3 — Visualisation des données

Le notebook `03_visualizations.ipynb` transforme les résultats en graphiques interprétables :

- **Graphique linéaire** : évolution mensuelle du chiffre d'affaires.
- **Graphique à barres** : classement des pays par chiffre d'affaires.
- **Graphique à barres** : nombre de commandes par heure.
- **Diagramme circulaire** : répartition des clients fidèles et occasionnels.
- **Histogramme** : distribution des montants des commandes.

Chaque visualisation est accompagnée d'une interprétation métier afin de relier les résultats aux décisions que pourrait prendre une entreprise.

## 💡 Compétences développées

Ce projet m'a permis de mettre en pratique :

- Le nettoyage et la préparation des données.
- La manipulation de données avec Pandas.
- Les requêtes SQL et l'analyse de données avec SQLite.
- La création de visualisations avec Matplotlib et Seaborn.
- L'interprétation des indicateurs commerciaux.
- L'organisation et la documentation d'un projet sur GitHub.

## 🚀 Améliorations possibles

Les prochaines évolutions du projet pourraient inclure :

- La création d'un tableau de bord interactif avec Streamlit ou Power BI.
- L'ajout de filtres par pays, période et produit.
- L'analyse plus approfondie de la rétention et de la valeur client.
- La formulation de recommandations commerciales fondées sur les résultats observés.

## 👨‍💻 Auteur

**Benjamin Dodo**

Projet personnel de Data Analytics réalisé dans le cadre de mon apprentissage de Python, SQL et de la visualisation des données.

🔗 **GitHub :** [Dodo-Benjamin](https://github.com/Dodo-Benjamin)

---

*Projet pédagogique d'analyse de données commerciales à partir du jeu de données Online Retail.*
