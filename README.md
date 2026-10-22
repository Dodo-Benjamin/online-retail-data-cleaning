# 🛒 Online Retail Data Analysis

## 📌 Présentation du projet

Ce projet consiste à analyser les données d'une entreprise de vente en ligne afin d'identifier des tendances commerciales, de comprendre le comportement des clients et de produire des informations utiles à la prise de décision.

Le projet couvre quatre étapes principales : le nettoyage des données, l'analyse SQL, la visualisation des résultats et la segmentation des clients par la méthode RFM.

## 🎯 Objectifs

- Nettoyer et structurer un jeu de données transactionnelles.
- Utiliser Python et Pandas pour préparer les données.
- Répondre à des questions métier avec SQL et SQLite.
- Visualiser les performances commerciales avec Matplotlib et Seaborn.
- Segmenter les clients selon leur récence, leur fréquence d'achat et leur valeur monétaire.
- Formuler des recommandations commerciales à partir des résultats obtenus.

## 📊 Jeu de données

Le projet utilise le jeu de données **Online Retail**, qui contient des informations sur les factures, les produits, les quantités vendues, les prix, les dates d'achat, les clients et les pays.

Après le nettoyage, le jeu de données contient :

- **536 641 lignes**
- **8 colonnes**
- **0 doublon exact restant**

Les principales colonnes sont `InvoiceNo`, `StockCode`, `Description`, `Quantity`, `InvoiceDate`, `UnitPrice`, `CustomerID` et `Country`.

Les valeurs manquantes, les doublons et les transactions atypiques sont examinés durant la préparation des données. Les quantités négatives sont conservées dans le jeu nettoyé pour tenir compte des retours ou annulations potentiels. Les analyses de ventes positives appliquent des filtres adaptés à chaque question métier.

## 🛠️ Technologies utilisées

- **Python**
- **Pandas**
- **SQLite / SQL**
- **Matplotlib**
- **Seaborn**
- **Jupyter Notebook**
- **Git et GitHub**

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
│   ├── 03_visualizations.ipynb
│   └── 04_deeper_analysis.ipynb
│
├── analysis.db
└── README.md
```

*Remarque : adapte cette structure aux emplacements réels de tes fichiers dans GitHub. Les données volumineuses peuvent être conservées dans une archive ZIP. La base SQLite peut être recréée à partir du CSV nettoyé si nécessaire.*

## 🧹 Étape 1 — Nettoyage des données

**Notebook :** `01_clean_and_structure.ipynb`

Cette étape comprend :

- Le chargement et l'exploration du jeu de données.
- La détection et la suppression des doublons exacts.
- La conversion des dates au format datetime.
- La normalisation des données textuelles.
- L'examen des valeurs manquantes et des valeurs atypiques.
- L'exportation des données nettoyées.

**Résultat :** un jeu de données nettoyé de 536 641 lignes et 8 colonnes, sans doublon exact restant.

## 🗄️ Étape 2 — Analyse SQL

**Notebook : `02_sql_analysis.ipynb`

Les données sont chargées dans une base SQLite afin de répondre à plusieurs questions métier :

- Quels pays génèrent le plus de chiffre d'affaires ?
- À quelles heures les commandes sont-elles les plus fréquentes ?
- Quelle est la répartition entre clients fidèles et occasionnels ?
- Quel est le montant moyen d'une commande ?
- Comment le chiffre d'affaires évolue-t-il chaque mois ?

Les requêtes utilisent notamment les regroupements, les fonctions d'agrégation, les filtres et les fonctions de dates SQL.

📈 Étape 3 — Visualisation des données

**Notebook :** `03_visualizations.ipynb`

Cette étape transforme les résultats en graphiques clairs et interprétables :

- Courbe d'évolution mensuelle du chiffre d'affaires.
- Graphique à barres des 10 pays les plus performants.
- Graphique du nombre de commandes par heure.
- Diagramme circulaire de la répartition des clients selon leur fidélité.
- Histogramme de la distribution des montants des commandes.

Chaque graphique est accompagné d'une interprétation métier afin de relier les observations aux décisions commerciales.

 👥 Étape 4 — Analyse approfondie : segmentation RFM

**Notebook :** `04_deeper_analysis.ipynb`

L'analyse RFM permet de segmenter les clients à partir de trois indicateurs :

- **Récence (Recency)** : nombre de jours depuis le dernier achat observé.
- **Fréquence (Frequency)** : nombre de commandes distinctes passées par le client.
- **Valeur monétaire (Monetary)** : montant total des achats du client sur la période analysée.

Des scores sont calculés pour chaque indicateur afin de constituer des segments de clientèle, notamment les meilleurs clients, les clients fidèles récents, les clients à réactiver et les clients nouveaux ou occasionnels.

Les résultats sont présentés à l'aide de tableaux récapitulatifs et de visualisations comparant les segments, la fréquence d'achat et les dépenses.

 💡 Intérêt métier de l'analyse RFM

La segmentation RFM aide une entreprise à adapter ses actions commerciales à différents profils de clients. Elle peut notamment contribuer à fidéliser les meilleurs clients, encourager les achats répétés et cibler les clients qui n'ont pas acheté depuis longtemps.

Les segments et recommandations doivent être interprétés à partir des résultats réellement calculés. La récence est mesurée par rapport à la dernière date disponible dans le jeu de données et ne correspond pas nécessairement à la date actuelle.

 📌 Compétences développées

- Nettoyage et préparation des données avec Pandas.
- Manipulation des dates et des valeurs manquantes.
- Requêtes SQL et analyse de données avec SQLite.
- Création et interprétation de visualisations.
- Analyse exploratoire des données.
- Segmentation client avec la méthode RFM.
- Documentation et gestion de projet avec GitHub.

 🚀 Améliorations futures

Les prochaines évolutions possibles sont :

- Création d'un tableau de bord interactif avec Streamlit ou Power BI.
- Ajout de filtres par période, pays et segment client.
- Analyse de la rétention client par cohortes.
- Élaboration de recommandations commerciales fondées sur les résultats.
- Automatisation de certaines étapes du traitement des données.

*Projet d'analyse de données commerciales basé sur le jeu de données Online Retail.*
