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
# Créer l'environnement à partir du fichier exporté (recommandé)
conda env create -f py3_pcse_export.yml

# Activer l'environnement
conda activate py3_pcse
```

**Note** : Le fichier `py3_pcse_export.yml` contient l'environnement complet avec :

- Python 3.10.18
- PCSE 6.0.9 (WOFOST)
- Jupyter & ipykernel 7.0.1
- Toutes les dépendances scientifiques (numpy, pandas, matplotlib, xarray, netcdf4, etc.)

### Configuration du kernel Jupyter

```bash
# Le kernel est déjà configuré avec l'environnement exporté !
# Pour vérifier : jupyter kernelspec list

# Si besoin de le réinstaller :
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

## � Workflow Git

Ce projet utilise une stratégie de branches pour gérer le développement :

### Structure des branches

```
main (production)  ← Code stable et testé
  ↑
  │ (merge via Pull Request)
  │
dev (développement) ← Développement actif
```

### Workflow de développement

#### 1️⃣ Travailler sur la branche dev

```bash
# Se positionner sur dev (branche de développement)
git checkout dev

# Vérifier les modifications
git status

# Ajouter les fichiers modifiés
git add .
# ou ajouter des fichiers spécifiques
git add fichier1.py fichier2.ipynb

# Commiter avec un message descriptif
git commit -m "feat: ajout de la simulation pour le maïs"

# Pousser vers GitHub
git push origin dev
```

#### 2️⃣ Merger dev vers main (quand tout est validé)

```bash
# Se positionner sur main
git checkout main

# Mettre à jour main depuis GitHub
git pull origin main

# Merger la branche dev dans main
git merge dev

# Pousser les changements vers GitHub
git push origin main

# Retourner sur dev pour continuer le développement
git checkout dev
```

#### 3️⃣ Commandes utiles

```bash
# Voir toutes les branches
git branch -a

# Voir les différences entre dev et main
git diff main..dev

# Voir l'historique des commits
git log --oneline --graph --all

# Annuler des modifications non commitées
git restore fichier.py

# Voir le statut du dépôt
git status
```

### Convention de messages de commit

- `feat:` - Nouvelle fonctionnalité
- `fix:` - Correction de bug
- `docs:` - Modification de documentation
- `refactor:` - Refactorisation du code
- `data:` - Ajout/modification de données
- `notebook:` - Modification de notebooks

**Exemples :**

```bash
git commit -m "feat: ajout simulation blé d'hiver"
git commit -m "fix: correction du calcul de biomasse"
git commit -m "docs: mise à jour du README avec workflow Git"
git commit -m "data: ajout données météo Dakar 2024"
```

## �👤 Auteur

**Nicaise Kassi** - Formation WOFOST

📧 Contact : [GitHub](https://github.com/NicaiseKassi)

## 📅 Date

Octobre 2025

## 📄 Licence

Ce projet est destiné à un usage éducatif et de formation.
