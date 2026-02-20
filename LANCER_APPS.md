# 🖥️ Lancer les Applications Desktop VisionIT

## Applications Créées

### 1. 📝 Text Editor (Éditeur de Texte)
**Dossier:** `text_editor_app/`

**Lancer:**
```bash
cd text_editor_app
source ../venv/bin/activate
python main.py
```

**Fonctionnalités:**
- ✅ Fenêtre desktop native (1200x800)
- ✅ Barre de menu avec boutons (Nouveau, Ouvrir, Sauvegarder)
- ✅ Zone d'édition de texte
- ✅ Compteur de mots et caractères
- ✅ Outils de formatage
- ✅ Barre de status

---

### 2. 🎉 Demo Window (Fenêtre de Démo)
**Dossier:** `demo_window/`

**Lancer:**
```bash
cd demo_window
source ../venv/bin/activate
python main.py
```

**Fonctionnalités:**
- ✅ Fenêtre desktop native (1000x700)
- ✅ Interface moderne avec dégradés
- ✅ Boutons interactifs
- ✅ Champs de saisie
- ✅ Sliders, checkboxes, switches
- ✅ Notifications
- ✅ Informations du projet

---

## 🔧 Mode de Lancement

### Mode Navigateur (par défaut)
```python
ui.run(
    native=False,  # Ouvre dans le navigateur
    ...
)
```

### Mode Fenêtre Desktop (NATIF) ⭐
```python
ui.run(
    native=True,  # Ouvre une fenêtre desktop
    window_size=(1000, 700),
    fullscreen=False,
    frameless=False,  # Barre de titre visible
    ...
)
```

---

## 📦 Build en Exécutable

Pour créer un exécutable standalone :

```bash
# Installer PyInstaller
visionit build deps

# Build en mode onefile (exécutable unique)
visionit build onefile

# L'exécutable sera dans : dist/
```

---

## 🎨 Personnalisation de la Fenêtre

Dans `main.py`, modifiez :

```python
WINDOW_TITLE = "Mon Application"
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 800

def configure_app():
    app.native.title = WINDOW_TITLE
    app.native.width = WINDOW_WIDTH
    app.native.height = WINDOW_HEIGHT
    app.native.resizable = True
    app.native.fullscreen = False
    app.native.frameless = False  # True pour cacher la barre de titre
```

---

## ✅ Ce Que Vous Devriez Voir

Quand vous lancez `python main.py` :

1. **Une fenêtre desktop s'ouvre** (pas dans le navigateur)
2. **Barre de titre** avec le nom de l'application
3. **Boutons** de contrôle (réduire, agrandir, fermer)
4. **Interface graphique** avec tous les composants NiceGUI
5. **Interactivité** - boutons, inputs, notifications fonctionnent

---

## 🐛 Problèmes Courants

### La fenêtre ne s'ouvre pas
Vérifiez que `native=True` dans `ui.run()`

### La fenêtre s'ouvre dans le navigateur
Changez `native=False` à `native=True`

### Erreur avec PyWebView
```bash
pip install pywebview
```

### Fenêtre trop petite
Ajustez `WINDOW_WIDTH` et `WINDOW_HEIGHT` dans `main.py`

---

## 🚀 Test Rapide

```bash
# Test de la démo
cd demo_window
source ../venv/bin/activate
python main.py

# Test de l'éditeur de texte
cd ../text_editor_app
source ../venv/bin/activate
python main.py
```

---

**VisionIT Framework** - Créez des applications desktop modernes avec Python ! 🎉
