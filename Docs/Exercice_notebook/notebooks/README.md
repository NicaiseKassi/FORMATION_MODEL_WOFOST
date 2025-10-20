# 📚 Exercices WOFOST - Calibration du modèle

Ce dossier contient **12 notebooks Jupyter** pour apprendre à calibrer le modèle de croissance des cultures WOFOST.

---

## 📖 À propos

Ces exercices sont basés sur le document **"Calibration of WOFOST crop growth simulation model for use within CGMS"** (Wolf & de Wit, 2003-2010).

Ils vous guident pas à pas dans le processus de calibration de WOFOST pour des conditions spécifiques.

---

## 🎯 Objectifs pédagogiques

Apprendre à :

- ✅ Configurer et lancer des simulations WOFOST
- ✅ Calibrer la phénologie (TSUM1, TSUM2)
- ✅ Ajuster les paramètres de croissance (LAI, biomasse)
- ✅ Calibrer le partitionnement des assimilats
- ✅ Simuler la production limitée par l'eau
- ✅ Créer des fichiers crop et soil personnalisés

---

## 📋 Liste des exercices

### 🌱 Phase 1 : Production potentielle (Exercices 1-7)

| #   | Notebook                                                                                                                             | Objectif                                           | Durée  |
| --- | ------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------- | ------ |
| 1   | [Exercice_01_Familiarisation_avec_WOFOST.ipynb](Exercice_01_Familiarisation_avec_WOFOST.ipynb)                                       | Première simulation de blé en conditions optimales | 30 min |
| 2   | [Exercice_02_Calibration_de_la_phenologie_du_ble.ipynb](Exercice_02_Calibration_de_la_phenologie_du_ble.ipynb)                       | Ajuster TSUM1 et TSUM2 pour dates phénologiques    | 45 min |
| 3   | [Exercice_03_Creer_un_nouveau_fichier_crop.ipynb](Exercice_03_Creer_un_nouveau_fichier_crop.ipynb)                                   | Créer fichier crop avec paramètres calibrés        | 20 min |
| 4   | [Exercice_04_Interception_lumineuse_et_biomasse_potentielle.ipynb](Exercice_04_Interception_lumineuse_et_biomasse_potentielle.ipynb) | Analyser LAI, interception lumineuse et biomasse   | 60 min |
| 5   | [Exercice_05_Calibration_du_LAI_et_de_la_biomasse.ipynb](Exercice_05_Calibration_du_LAI_et_de_la_biomasse.ipynb)                     | Ajuster SLA et AMAXTB pour LAI et biomasse         | 45 min |
| 6   | [Exercice*06_Exercice_6*(Non_documente).ipynb](<Exercice_06_Exercice_6_(Non_documente).ipynb>)                                       | _Exercice non documenté dans le PDF_               | -      |
| 7   | [Exercice_07_Distribution_des_assimilats.ipynb](Exercice_07_Distribution_des_assimilats.ipynb)                                       | Calibrer partitionnement pour indice de récolte    | 45 min |

### 💧 Phase 2 : Production limitée par l'eau (Exercices 8-12)

| #   | Notebook                                                                                                                             | Objectif                                          | Durée  |
| --- | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------- | ------ |
| 8   | [Exercice_08_Disponibilite_en_eau.ipynb](Exercice_08_Disponibilite_en_eau.ipynb)                                                     | Comprendre la balance hydrique et stress hydrique | 45 min |
| 9   | [Exercice_09_Sensibilite_aux_conditions_initiales_d'eau.ipynb](Exercice_09_Sensibilite_aux_conditions_initiales_d'eau.ipynb)         | Impact de l'eau initiale (SMLIM, WAV)             | 30 min |
| 10  | [Exercice*10_Sensibilite*à_la_capacite_de_retention_du_sol.ipynb](Exercice_10_Sensibilite_à_la_capacite_de_retention_du_sol.ipynb)   | Effet du type de sol sur le rendement             | 40 min |
| 11  | [Exercice_11_Creer_un_nouveau_fichier_sol.ipynb](Exercice_11_Creer_un_nouveau_fichier_sol.ipynb)                                     | Créer fichier soil avec paramètres mesurés        | 20 min |
| 12  | [Exercice_12_Calibration_de_la_production_limitee_par_l'eau.ipynb](Exercice_12_Calibration_de_la_production_limitee_par_l'eau.ipynb) | Calibration finale en conditions de stress        | 60 min |

**⏱️ Durée totale estimée : 7-8 heures**

---

## 🚀 Comment utiliser ces notebooks

### Prérequis

```bash
# 1. Activer l'environnement Python
conda activate py3_pcse

# 2. Vérifier que PCSE est installé
python -c "import pcse; print(pcse.__version__)"

# 3. Lancer Jupyter Lab
cd ~/Documents/FORMATION_MODEL_WOFOST/Docs/Exercice_notebook/notebooks
jupyter lab
```

### Ordre recommandé

1. **Commencez par l'exercice 1** et suivez l'ordre numérique
2. Chaque exercice s'appuie sur les précédents
3. Complétez tous les exercices de la Phase 1 avant de passer à la Phase 2

### Structure d'un notebook

Chaque notebook contient :

- 🎯 **Objectif** : Ce que vous allez apprendre
- 📖 **Instructions** : Étapes détaillées
- ⚙️ **Concepts clés** : Notions importantes
- 💻 **Code** : Cellules à exécuter et compléter
- ✅ **Points clés** : Résumé à retenir

---

## 📊 Données nécessaires

Les exercices utilisent :

- **Données météo** : Wageningen 1973 (NL1.973)
- **Fichier crop** : WWH102.cab (blé d'hiver)
- **Fichier soil** : EC1.new, EC2.new, EC3.new
- **Observations** : Dates phénologiques, LAI, biomasse

Ces fichiers sont référencés dans le PDF source.

---

## 📚 Ressources

### Documents de référence

- 📄 [Hefei_Wofost_Training_Exercises.pdf](../Hefei_Wofost_Training_Exercises.pdf) - Document source
- 🌐 [Documentation PCSE](https://pcse.readthedocs.io/)
- 🌐 [WOFOST à Wageningen](http://www.wofost.wur.nl)

### Fichiers de configuration

- Fichiers crop : `../../wofost-projects/data/crop/`
- Fichiers soil : `../../wofost-projects/data/soil/`
- Fichiers météo : `../../wofost-projects/data/meteo/`

---

## 🎓 Compétences acquises

À la fin de ces exercices, vous saurez :

✅ Configurer et exécuter WOFOST en mode PP et WLP  
✅ Calibrer la phénologie d'une variété  
✅ Ajuster les paramètres de croissance  
✅ Calibrer le partitionnement des assimilats  
✅ Analyser la balance hydrique  
✅ Créer des fichiers crop et soil personnalisés  
✅ Interpréter les sorties de WOFOST  
✅ Valider un modèle avec des observations

---

## 💡 Conseils

1. **Prenez votre temps** - La calibration est un processus itératif
2. **Notez vos observations** - Ajoutez des cellules markdown avec vos réflexions
3. **Expérimentez** - Testez différentes valeurs de paramètres
4. **Comparez** - Toujours comparer simulations vs observations
5. **Documentez** - Gardez trace des valeurs testées et des résultats

---

## 🐛 Problèmes courants

### Erreur d'import PCSE

```bash
pip install pcse
```

### Kernel py3_pcse non trouvé

```bash
python -m ipykernel install --user --name=py3_pcse --display-name="Python 3.10 (py3_pcse)"
```

### Fichiers de données manquants

Vérifiez les chemins dans `../../wofost-projects/data/`

---

## 👤 Auteur

**Nicaise Kassi**  
Formation WOFOST - Octobre 2025

---

## 📄 Licence

Matériel pédagogique - Usage éducatif

Basé sur le travail de :

- Joost Wolf (Wageningen University)
- Allard de Wit (Alterra, WUR)
