# Projet Python - Nettoyage et Structuration des données

## Description

Ce projet consiste à nettoyer et structurer un jeu de données de ventes en ligne afin de préparer les données pour de futures analyses statistiques et exploratoires.

## Objectifs

- Charger et examiner les données brutes
- Identifier et supprimer les doublons exacts
- Corriger les types de données
- Convertir les dates au format approprié
- Traiter les valeurs manquantes lorsque cela est possible
- Standardiser les colonnes textuelles
- Examiner les valeurs atypiques, notamment les quantités négatives
- Exporter un fichier de données nettoyé

## Traitements réalisés

### Doublons

5 268 doublons exacts ont été identifiés et supprimés.

### Dates

La colonne InvoiceDate a été convertie au format datetime.

### Description

Les descriptions manquantes ont été complétées lorsque cela était possible à partir du StockCode.

112 descriptions restent manquantes.

### CustomerID

Les identifiants clients manquants ont été conservés car ils ne peuvent pas être reconstitués de manière fiable.

### Quantités négatives

Les quantités négatives ont été conservées car elles peuvent correspondre à des retours, annulations ou ajustements.

### Prix négatifs

Deux lignes présentant un prix unitaire négatif ont été conservées. Elles correspondent à des opérations d'ajustement comptable (Adjust bad debt).

## Résultat final

Le jeu de données nettoyé contient :

- 536 641 lignes
- 8 colonnes
- 0 doublon exact

## Structure du projet

Projet_Python/
    data/
        archive/
            data.csv
        raw_data.csv
        cleaned_data.csv
    notebooks/
        01_clean_and_structure.ipynb
    README.md

## Technologies utilisées

- Python
- Pandas
- NumPy
- Jupyter Notebook
