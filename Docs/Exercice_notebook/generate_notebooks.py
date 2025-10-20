#!/usr/bin/env python3
"""
Script pour générer les 12 notebooks d'exercices WOFOST
"""
import json
import os

# Définir le répertoire de sortie
OUTPUT_DIR = "/home/kassi/Documents/FORMATION_MODEL_WOFOST/Docs/Exercice_notebook/notebooks"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Liste des exercices avec leurs descriptions
exercises_info = {
    1: {
        "title": "Familiarisation avec WOFOST",
        "objective": "Première simulation de croissance du blé d'hiver en production potentielle",
        "key_concepts": ["DVS", "TAGP", "LAI", "Production potentielle"],
        "what_to_do": [
            "Configurer une simulation WOFOST pour le blé",
            "Lancer la simulation en mode production potentielle",
            "Observer les dates d'émergence, anthèse et maturité",
            "Analyser l'évolution de la biomasse et du LAI"
        ]
    },
    2: {
        "title": "Calibration de la phénologie du blé",
        "objective": "Ajuster TSUM1 et TSUM2 pour faire correspondre les dates phénologiques simulées avec les observations",
        "key_concepts": ["TSUM1", "TSUM2", "Calibration", "Somme de températures"],
        "what_to_do": [
            "Comparer dates simulées vs observées",
            "Tester 4 scénarios avec TSUM1 et TSUM2 décroissants",
            "Identifier les valeurs optimales",
            "Valider avec les observations"
        ]
    },
    3: {
        "title": "Créer un nouveau fichier crop",
        "objective": "Créer un fichier de paramètres pour une nouvelle variété avec TSUM calibrés",
        "key_concepts": ["Fichier crop", "Paramètres calibrés", "YAML/CAB format"],
        "what_to_do": [
            "Copier le fichier crop existant",
            "Modifier TSUM1 et TSUM2",
            "Sauvegarder sous un nouveau nom",
            "Tester la nouvelle variété"
        ]
    },
    4: {
        "title": "Interception lumineuse et biomasse potentielle",
        "objective": "Analyser la relation entre LAI, interception lumineuse et production de biomasse",
        "key_concepts": ["LAI", "KDIF", "Loi de Beer-Lambert", "AMAXTB", "Photosynthèse"],
        "what_to_do": [
            "Calculer l'interception lumineuse en fonction du LAI",
            "Analyser la production de biomasse",
            "Comprendre les paramètres AMAXTB et EFFTB",
            "Évaluer la respiration de maintenance"
        ]
    },
    5: {
        "title": "Calibration du LAI et de la biomasse",
        "objective": "Ajuster SLA pour reproduire le LAI maximum observé et calibrer la biomasse",
        "key_concepts": ["SLA", "SLATB", "LAI maximum", "Calibration biomasse"],
        "what_to_do": [
            "Comparer LAI simulé vs observé",
            "Ajuster SLATB (Specific Leaf Area)",
            "Calibrer AMAXTB si biomasse incorrecte",
            "Valider les résultats"
        ]
    },
    6: {
        "title": "Exercice 6 (Non documenté)",
        "objective": "Cet exercice n'est pas présent dans le document PDF",
        "key_concepts": ["Non applicable"],
        "what_to_do": ["Exercice manquant dans la documentation"]
    },
    7: {
        "title": "Distribution des assimilats",
        "objective": "Calibrer le partitionnement des assimilats pour reproduire l'indice de récolte observé",
        "key_concepts": ["Harvest Index", "FLTB", "FSTB", "FOTB", "Partitionnement"],
        "what_to_do": [
            "Calculer l'indice de récolte simulé",
            "Comparer avec l'indice observé",
            "Ajuster les tables de partitionnement",
            "Modifier le DVS de début de remplissage des grains"
        ]
    },
    8: {
        "title": "Disponibilité en eau",
        "objective": "Comprendre la balance hydrique et la production limitée par l'eau",
        "key_concepts": ["Production limitée eau", "Stress hydrique", "Balance hydrique", "WOFOST_WLP_FD"],
        "what_to_do": [
            "Simuler en mode water-limited production",
            "Analyser les périodes de stress hydrique",
            "Comparer avec la production potentielle",
            "Examiner le contenu en eau du sol"
        ]
    },
    9: {
        "title": "Sensibilité aux conditions initiales d'eau",
        "objective": "Évaluer l'impact de l'eau initiale du sol (SMLIM et WAV)",
        "key_concepts": ["SMLIM", "WAV", "Eau initiale", "Sensibilité"],
        "what_to_do": [
            "Tester différentes valeurs de SMLIM",
            "Tester différentes valeurs de WAV",
            "Comparer les rendements obtenus",
            "Analyser l'impact sur la croissance"
        ]
    },
    10: {
        "title": "Sensibilité à la capacité de rétention du sol",
        "objective": "Évaluer l'impact du type de sol sur la production limitée par l'eau",
        "key_concepts": ["Capacité au champ", "Point de flétrissement", "Texture du sol", "Rétention d'eau"],
        "what_to_do": [
            "Tester sols de différentes textures",
            "Comparer sols grossiers, moyens et fins",
            "Analyser l'impact sur le rendement",
            "Identifier le sol optimal"
        ]
    },
    11: {
        "title": "Créer un nouveau fichier sol",
        "objective": "Créer un fichier soil avec des paramètres hydriques mesurés sur le terrain",
        "key_concepts": ["Fichier soil", "Paramètres hydriques", "SMW", "SMFCF"],
        "what_to_do": [
            "Copier un fichier soil existant",
            "Modifier SMW (wilting point)",
            "Modifier SMFCF (field capacity)",
            "Tester le nouveau fichier"
        ]
    },
    12: {
        "title": "Calibration de la production limitée par l'eau",
        "objective": "Calibration finale pour la production en conditions de stress hydrique",
        "key_concepts": ["RDMCR", "DEPNR", "Profondeur racinaire", "Sensibilité sécheresse"],
        "what_to_do": [
            "Ajuster la profondeur racinaire maximale (RDMCR)",
            "Calibrer DEPNR (facteur de sécheresse)",
            "Comparer avec biomasse observée",
            "Valider la calibration complète"
        ]
    }
}

def create_notebook(ex_num, info):
    """Créer un notebook pour un exercice donné"""
    
    # Construction des sources avec vraies nouvelles lignes
    title_md = [
        f"# Exercice {ex_num} : {info['title']}",
        "",
        "---",
        "",
        "## 🎯 Objectif",
        "",
        info['objective'],
        "",
        "---",
        "",
        "## 📖 Qu'est-ce qu'on va faire ?",
        ""
    ]
    title_md.extend([f"{i+1}. {task}" for i, task in enumerate(info['what_to_do'])])
    title_md.extend(["", "---", "", "## ⚙️ Concepts clés", ""])
    title_md.extend([f"- **{concept}**" for concept in info['key_concepts']])
    
    imports_code = [
        "# Imports nécessaires",
        "import os",
        "import sys",
        "import yaml",
        "import pandas as pd",
        "import numpy as np",
        "import matplotlib.pyplot as plt",
        "from datetime import datetime, timedelta",
        "",
        "# Configuration des graphiques",
        "plt.style.use('seaborn-v0_8-darkgrid')",
        "plt.rcParams['figure.figsize'] = (12, 6)",
        "plt.rcParams['font.size'] = 10",
        "",
        "print('='*70)",
        f"print('  EXERCICE {ex_num}: {info['title'].upper()}')",
        "print('='*70)",
        "print('\\n✅ Environnement configuré')"
    ]
    
    instructions_md = [
        "## 📋 Instructions de l'exercice",
        "",
        f"Cet exercice vous guide dans : **{info['objective']}**",
        "",
        "### Étapes à suivre :",
        ""
    ]
    instructions_md.extend([f"{i+1}. {task}" for i, task in enumerate(info['what_to_do'])])
    
    work_code = [
        f"# Zone de travail - Exercice {ex_num}",
        "",
        "# TODO: Implémenter la simulation WOFOST",
        "# Suivez les instructions ci-dessus",
        "",
        f"print('\\n📝 Exercice {ex_num} en cours...')",
        f"print('Objectif: {info['objective']}')"
    ]
    
    conclusion_md = [
        "## ✅ Points clés à retenir",
        ""
    ]
    conclusion_md.extend([f"- {concept}" for concept in info['key_concepts']])
    conclusion_md.extend(["", "---", "", f"**📚 Exercice suivant : Exercice {ex_num + 1}** (si disponible)"])
    
    notebook = {
        "cells": [
            # Titre et introduction
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": title_md
            },
            # Imports
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": imports_code
            },
            # Instructions
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": instructions_md
            },
            # Zone de travail
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": work_code
            },
            # Conclusion
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": conclusion_md
            }
        ],
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3 (py3_pcse)",
                "language": "python",
                "name": "py3_pcse"
            },
            "language_info": {
                "codemirror_mode": {"name": "ipython", "version": 3},
                "file_extension": ".py",
                "mimetype": "text/x-python",
                "name": "python",
                "nbconvert_exporter": "python",
                "pygments_lexer": "ipython3",
                "version": "3.10.18"
            }
        },
        "nbformat": 4,
        "nbformat_minor": 4
    }
    
    # Sauvegarder le notebook
    filename = f"Exercice_{ex_num:02d}_{info['title'].replace(' ', '_').replace('é', 'e').replace('è', 'e')}.ipynb"
    filepath = os.path.join(OUTPUT_DIR, filename)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(notebook, f, indent=2, ensure_ascii=False)
    
    return filename

# Créer tous les notebooks
print(f"\\n🚀 Génération des 12 notebooks WOFOST...\\n")
print("="*70)

created_notebooks = []
for ex_num in range(1, 13):
    info = exercises_info[ex_num]
    filename = create_notebook(ex_num, info)
    created_notebooks.append(filename)
    print(f"✅ Exercice {ex_num:02d}: {filename}")

print("="*70)
print(f"\\n🎉 {len(created_notebooks)} notebooks créés avec succès!")
print(f"📁 Emplacement: {OUTPUT_DIR}")
print("\\n📝 Notebooks créés:")
for nb in created_notebooks:
    print(f"   - {nb}")
