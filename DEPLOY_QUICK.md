# 🚀 Déploiement Rapide - VisionIT Framework

## ✅ Checklist de Déploiement

### 1. Prérequis

- [ ] Compte PyPI créé sur [pypi.org](https://pypi.org/)
- [ ] Token API PyPI généré (Account Settings → API Tokens)
- [ ] Compte TestPyPI créé sur [test.pypi.org](https://test.pypi.org/)
- [ ] Token API TestPyPI généré

### 2. Installation des Outils

```bash
cd visionit
source venv/bin/activate
pip install build twine
```

### 3. Build du Package

```bash
# Nettoyer
rm -rf dist/ build/ *.egg-info

# Construire
python -m build
```

### 4. Vérification

```bash
# Vérifier le package
twine check dist/*
```

Doit afficher :
```
Checking dist/visionit-0.1.0-py3-none-any.whl: PASSED
Checking dist/visionit-0.1.0.tar.gz: PASSED
```

### 5. Test sur TestPyPI (Recommandé)

```bash
# Publier sur TestPyPI
twine upload --repository testpypi dist/*

# Ou avec token en ligne de commande
twine upload --repository testpypi -u __token__ -p pypi-YOUR_TOKEN dist/*
```

### 6. Publication sur PyPI

```bash
# Publier sur PyPI
twine upload dist/*

# Ou avec token en ligne de commande
twine upload -u __token__ -p pypi-YOUR_TOKEN dist/*
```

### 7. Vérification

1. Allez sur https://pypi.org/project/visionit/
2. Testez l'installation :

```bash
pip install visionit
visionit --help
```

---

## 🔄 Mise à Jour d'une Version

### 1. Mettre à Jour la Version

**Fichiers à modifier :**
- `visionit/__init__.py` : `__version__ = "0.1.1"`
- `pyproject.toml` : `version = "0.1.1"`
- `setup.cfg` : `version = 0.1.1`

### 2. Reconstruire et Publier

```bash
# Nettoyer
rm -rf dist/ build/ *.egg-info

# Reconstruire
python -m build

# Vérifier
twine check dist/*

# Publier
twine upload dist/*
```

---

## 🤖 Publication Automatique avec GitHub

### 1. Configurer le Secret GitHub

1. GitHub Repo → Settings → Secrets and variables → Actions
2. New repository secret
3. Nom : `PYPI_API_TOKEN`
4. Valeur : `pypi-YOUR_TOKEN`

### 2. Créer un Tag

```bash
git tag v0.1.0
git push origin v0.1.0
```

GitHub Actions va automatiquement build et publier !

---

## 📁 Fichiers de Distribution

Après build, vous aurez :

- `dist/visionit-0.1.0.tar.gz` - Source distribution
- `dist/visionit-0.1.0-py3-none-any.whl` - Wheel distribution

Les deux sont nécessaires pour PyPI.

---

## 🔧 Commandes Utiles

```bash
# Installer depuis TestPyPI
pip install --index-url https://test.pypi.org/simple/ visionit

# Installer depuis PyPI
pip install visionit

# Vérifier la version installée
visionit version

# Voir les fichiers du package
tar -tzf dist/visionit-0.1.0.tar.gz
```

---

## ⚠️ Problèmes Courants

### "File already exists"

La version existe déjà. Incrémentez la version :
```python
__version__ = "0.1.1"  # 0.1.0 → 0.1.1
```

### "Invalid authentication"

Vérifiez votre token :
- Régénérer un token sur PyPI
- Mettre à jour la commande twine

### "Missing files"

Vérifiez `MANIFEST.in` et reconstruisez :
```bash
rm -rf dist/ build/ *.egg-info
python -m build
```

---

## 📞 Support

- **Guide complet :** `PYPI_DEPLOY.md`
- **Documentation PyPI :** https://packaging.python.org/
- **Status PyPI :** https://status.python.org/

---

**VisionIT Framework** - Publié avec ❤️ sur PyPI
