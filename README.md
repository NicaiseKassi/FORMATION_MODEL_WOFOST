# FORMATION_MODEL_WOFOST

Formation sur le modèle de simulation de cultures WOFOST (World Food Studies)

## 📋 Description

Ce dépôt contient les matériaux de formation pour l'utilisation du modèle WOFOST via la bibliothèque Python PCSE (Python Crop Simulation Environment).

## 🌾 À propos de WOFOST

WOFOST est un modèle de simulation de croissance des cultures développé par l'Université de Wageningen. Il permet de simuler la croissance et le développement des cultures en fonction de :
- Conditions météorologiques
- Propriétés du sol
- Caractéristiques des cultures
- Pratiques de gestion agricole

## 📁 Structure du projet

```
FORMATION_MODEL_WOFOST/
├── Docs/                          # Documentation et fichiers de référence
├── wofost-projects/               # Projets WOFOST principaux
│   ├── notebooks/                 # Notebooks Jupyter de simulation
│   ├── pcse_notebooks/            # Notebooks d'apprentissage PCSE
│   ├── data/                      # Données d'entrée (crop, soil, weather)
│   ├── results/                   # Résultats de simulations
│   └── scripts/                   # Scripts Python
├── WOSFOST/                       # Fichiers de configuration
├── Wofost_folder2/               # Dossier de travail supplémentaire
├── py3_pcse_export.yml           # Environnement conda exporté
└── README.md                      # Ce fichier
```

## 🛠️ Installation

### Prérequis
- Anaconda ou Miniconda
- Python 3.10

### Créer l'environnement

```bash
# Créer l'environnement à partir du fichier exporté
conda env create -f py3_pcse_export.yml

# Ou créer l'environnement avec les packages essentiels
conda env create -f wofost-projects/py3_pcse.yml

# Activer l'environnement
conda activate py3_pcse
```

### Configuration du kernel Jupyter

```bash
# Enregistrer le kernel pour Jupyter
python -m ipykernel install --user --name=py3_pcse --display-name="Python 3.10 (py3_pcse)"
```

## 🚀 Utilisation

### Lancer Jupyter Lab

```bash
conda activate py3_pcse
cd wofost-projects/notebooks
jupyter lab
```

### Notebooks disponibles

1. **01.simulation.ipynb** - Simulation de base WOFOST
2. **pcse_notebooks/** - Collection complète de tutoriels :
   - Getting Started with PCSE
   - Running with custom input data
   - Running LINTUL3
   - Batch mode simulations
   - Data assimilation
   - Parameter optimization
   - Sensitivity analysis
   - Et plus encore...

## 📦 Packages principaux

- **pcse** (6.0.9) - Python Crop Simulation Environment
- **numpy** - Calculs numériques
- **pandas** - Manipulation de données
- **matplotlib** - Visualisation
- **xarray** - Données multidimensionnelles
- **netcdf4** - Fichiers de données climatiques
- **jupyter** - Notebooks interactifs

## 📚 Ressources

- [Documentation PCSE](https://pcse.readthedocs.io/)
- [WOFOST Control Centre](https://www.wur.nl/en/Research-Results/Research-Institutes/plant-research/open-teelten/Models/WOFOST.htm)

## 👤 Auteur

Kassi - Formation WOFOST

## 📅 Date

Octobre 2025

## 📄 Licence

Ce projet est destiné à un usage éducatif et de formation.
