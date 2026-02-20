# 🚀 Guide de Déploiement PyPI - VisionIT Framework

Ce guide vous explique comment publier VisionIT Framework sur PyPI (Python Package Index).

---

## 📋 Prérequis

### 1. Créer un Compte PyPI

1. Allez sur [pypi.org](https://pypi.org/)
2. Cliquez sur **"Register"**
3. Créez votre compte avec email vérifié
4. Notez vos identifiants

### 2. Créer un Token d'API (Recommandé)

**Sur PyPI :**
1. Allez dans **Account Settings** → **API Tokens**
2. Cliquez sur **"Add API Token"**
3. Donnez un nom (ex: `visionit-publish`)
4. Sélectionnez **"Entire project"** ou un projet spécifique
5. Copiez le token (il ne sera affiché qu'une fois !)

**Format du token :** `pypi-AgEIcHlwaS5vcmc...`

### 3. Installer les Outils de Build

```bash
# Dans votre environnement virtuel
cd visionit
source venv/bin/activate

# Installer les outils de build
pip install build twine
```

---

## 🏗️ Préparation du Package

### 1. Vérifier la Structure

Assurez-vous que la structure est correcte :

```
visionit/
├── visionit/              # Package principal
│   ├── __init__.py        # Avec __version__
│   └── cli.py
├── tests/
│   ├── __init__.py
│   └── test_cli.py
├── templates/             # Templates à inclure
│   └── components/
├── setup.py               # Configuration legacy
├── pyproject.toml         # Configuration moderne
├── README.md              # Documentation
├── LICENSE                # Licence
└── MANIFEST.in            # Fichiers à inclure
```

### 2. Créer MANIFEST.in

**Fichier :** `MANIFEST.in`

```ini
# Inclure les fichiers de documentation
include README.md
include LICENSE
include pyproject.toml

# Inclure les templates
recursive-include visionit/templates *.html

# Inclure les tests
recursive-include tests *.py

# Exclure les fichiers inutiles
global-exclude *.pyc
global-exclude *.pyo
global-exclude __pycache__
global-exclude .gitignore
global-exclude .env
global-exclude venv
global-exclude dist
global-exclude build
global-exclude *.egg-info
```

### 3. Mettre à Jour la Version

**Fichier :** `visionit/__init__.py`

```python
"""VisionIT Framework - Python 3.9+ boilerplate for rapid application development."""

__version__ = "0.1.0"  # ← Mettre à jour ici
__author__ = "Vision IT"
```

**Fichier :** `pyproject.toml`

```toml
[project]
name = "visionit"
version = "0.1.0"  # ← Mettre à jour ici
```

**Fichier :** `setup.py`

```python
setup(
    name='visionit',
    version='0.1.0',  # ← Mettre à jour ici
    ...
)
```

---

## 🧪 Tester avec TestPyPI (Recommandé)

TestPyPI est un environnement de test séparé de PyPI.

### 1. Créer un Compte TestPyPI

1. Allez sur [test.pypi.org](https://test.pypi.org/)
2. Créez un compte (différent de PyPI)
3. Créez un token API

### 2. Configurer .pypirc

**Fichier :** `~/.pypirc` (Linux/Mac) ou `%USERPROFILE%\.pypirc` (Windows)

```ini
[distutils]
index-servers =
    pypi
    testpypi

[pypi]
username = __token__
password = pypi-AgEIcHlwaS5vcmc...  # Votre token PyPI

[testpypi]
repository = https://test.pypi.org/legacy/
username = __token__
password = pypi-AgEIcHlwaS5vcmc...  # Votre token TestPyPI
```

### 3. Construire le Package

```bash
# Nettoyer les anciens builds
rm -rf dist/ build/ *.egg-info

# Construire le package
python -m build
```

Cela crée :
- `dist/visionit-0.1.0.tar.gz` (source distribution)
- `dist/visionit-0.1.0-py3-none-any.whl` (wheel)

### 4. Vérifier le Package

```bash
# Vérifier avec twine
twine check dist/*
```

Vous devriez voir :
```
Checking dist/visionit-0.1.0.tar.gz: PASSED
Checking dist/visionit-0.1.0-py3-none-any.whl: PASSED
```

### 5. Publier sur TestPyPI

```bash
# Publier sur TestPyPI
twine upload --repository testpypi dist/*

# Ou avec token en ligne de commande
twine upload --repository testpypi -u __token__ -p pypi-... dist/*
```

### 6. Tester l'Installation

```bash
# Créer un environnement de test
python -m venv test-env
source test-env/bin/activate

# Installer depuis TestPyPI
pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple visionit

# Tester
visionit --help
visionit version
```

---

## 📦 Publier sur PyPI

### 1. Dernière Vérification

```bash
# Vérifier que tout est prêt
twine check dist/*

# Vérifier les tests
pytest tests/ -v
```

### 2. Publier

```bash
# Publier sur PyPI
twine upload dist/*

# Ou avec token en ligne de commande
twine upload -u __token__ -p pypi-... dist/*
```

### 3. Vérifier la Publication

1. Allez sur `https://pypi.org/project/visionit/`
2. Vérifiez que la page s'affiche correctement
3. Testez l'installation :

```bash
pip install visionit
visionit --help
```

---

## 🔄 Mettre à Jour une Version

### 1. Changer le Numéro de Version

Suivez le [Semantic Versioning](https://semver.org/) :

- **MAJOR.MINOR.PATCH** (ex: 1.2.3)
- **MAJOR** : Changements incompatibles
- **MINOR** : Nouvelles fonctionnalités rétrocompatibles
- **PATCH** : Corrections de bugs rétrocompatibles

**Fichiers à mettre à jour :**
- `visionit/__init__.py`
- `pyproject.toml`
- `setup.py`

### 2. Reconstruire et Republier

```bash
# Nettoyer
rm -rf dist/ build/ *.egg-info

# Reconstruire
python -m build

# Publier
twine upload dist/*
```

---

## 🤖 Automatisation avec GitHub Actions

### Workflow de Publication Automatique

**Fichier :** `.github/workflows/publish.yml`

```yaml
name: Publish to PyPI

on:
  push:
    tags:
      - 'v*'  # Déclenche sur les tags v1.0.0, v2.1.3, etc.

jobs:
  build-and-publish:
    runs-on: ubuntu-latest
    
    steps:
      - uses: actions/checkout@v3
      
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.9'
      
      - name: Install build tools
        run: |
          pip install build twine
      
      - name: Build package
        run: python -m build
      
      - name: Check package
        run: twine check dist/*
      
      - name: Run tests
        run: pytest tests/ -v
      
      - name: Publish to PyPI
        env:
          TWINE_USERNAME: __token__
          TWINE_PASSWORD: ${{ secrets.PYPI_API_TOKEN }}
        run: twine upload dist/*
```

### Configurer le Secret GitHub

1. Allez dans votre repo GitHub → **Settings** → **Secrets and variables** → **Actions**
2. Cliquez sur **"New repository secret"**
3. Nom : `PYPI_API_TOKEN`
4. Valeur : Votre token PyPI (`pypi-AgEIcHlwaS5vcmc...`)

### Publier un Nouveau Version

```bash
# Mettre à jour la version dans __init__.py
# Commit et push
git add visionit/__init__.py
git commit -m "Release v0.1.0"
git push

# Créer un tag
git tag v0.1.0
git push origin v0.1.0

# GitHub Actions va automatiquement build et publier !
```

---

## 📊 Statistiques et Suivi

### PyPI Stats

- **Page du projet :** `https://pypi.org/project/visionit/`
- **Statistiques de téléchargement :** `https://pypistats.org/packages/visionit`

### Ajouter des Badges

Dans votre README.md :

```markdown
[![PyPI version](https://badge.fury.io/py/visionit.svg)](https://badge.fury.io/py/visionit)
[![Downloads](https://pepy.tech/badge/visionit)](https://pepy.tech/project/visionit)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/visionit.svg)](https://pypi.org/project/visionit/)
```

---

## ❓ Dépannage

### Erreur: "Upload failed (400): File already exists"

Le nom de version existe déjà. Solution :

```bash
# Incrémenter la version
# Ex: 0.1.0 → 0.1.1
```

### Erreur: "Invalid or non-existent authentication information"

Vérifiez votre token :

```bash
# Régénérer un token sur PyPI
# Mettre à jour ~/.pypirc
```

### Erreur: "No module named 'visionit.templates'"

Vérifiez `MANIFEST.in` et `setup.py` :

```python
# setup.py
setup(
    ...
    include_package_data=True,
    package_data={
        "visionit": ["templates/*", "templates/components/*"],
    },
)
```

### Erreur: "README.md not found"

Assurez-vous que `README.md` est à la racine et inclus dans `MANIFEST.in`.

---

## 🔐 Bonnes Pratiques de Sécurité

1. **Jamais** stocker les tokens dans le code
2. Utiliser les variables d'environnement ou `~/.pypirc`
3. Régénérer les tokens régulièrement
4. Utiliser 2FA sur votre compte PyPI
5. Limiter les permissions des tokens

---

## 📞 Support PyPI

- **Documentation PyPI :** https://packaging.python.org/
- **Support PyPI :** https://pypi.org/help/
- **Status PyPI :** https://status.python.org/

---

## 🎯 Checklist de Publication

- [ ] Version mise à jour dans tous les fichiers
- [ ] Tests passent (`pytest tests/ -v`)
- [ ] `twine check dist/*` passe
- [ ] README.md à jour
- [ ] LICENSE inclus
- [ ] MANIFEST.in correct
- [ ] Token PyPI configuré
- [ ] Test sur TestPyPI effectué
- [ ] Tag Git créé
- [ ] Publication sur PyPI réussie
- [ ] Page PyPI vérifiée
- [ ] Installation testée avec `pip install visionit`

---

**VisionIT Framework** - Publié avec ❤️ sur PyPI
