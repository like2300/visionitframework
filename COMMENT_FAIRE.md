# 🚀 Comment Utiliser VisionIT Framework

## ⚡ Démarrage Rapide

### 1. Installer le Framework

```bash
pip install visionit
```

### 2. Créer une Application Desktop

```bash
visionit new mon_app
cd mon_app
```

### 3. Lancer l'Application

```bash
# Installer les dépendances
pip install -r package.txt

# Lancer avec fenêtre desktop
python main.py
```

**✅ Une fenêtre desktop s'ouvre avec votre application !**

---

## 📁 Structure d'un Projet

```
mon_app/
├── main.py                # Point d'entrée (fenêtre desktop)
├── info.json              # Infos du projet
├── package.txt            # Dépendances
├── build.json             # Config pour exécutable
├── db/
│   └── schema.prisma      # Base de données
├── templates/
│   └── components/        # Composants HTML
├── static/
│   ├── css/
│   ├── js/
│   └── icons/
└── actions/
    └── *.py               # Logique métier
```

---

## 🖥️ La Fenêtre Desktop

### Configuration par Défaut

Dans `main.py` :

```python
WINDOW_TITLE = "mon_app"
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 800
PORT = 8080

ui.run(
    native=True,  # ⭐ Fenêtre desktop (pas navigateur)
    window_size=(WINDOW_WIDTH, WINDOW_HEIGHT),
    ...
)
```

### Ce Que Vous Voyez

```
┌─────────────────────────────────────────────────┐
│ mon_app  v1.0.0                          [_][□][X]│
├─────────────────────────────────────────────────┤
│ 🏠 mon_app                                       │
│                                                 │
│  ✅ Application Démarrée avec Succès !          │
│                                                 │
│  ┌──────────┬──────────┬──────────┐            │
│  │Application│ Auteur  │ Version  │            │
│  │mon_app   │Vision IT│  1.0.0   │            │
│  └──────────┴──────────┴──────────┘            │
│                                                 │
│  [👍 Test] [✅ Succès] [⚠️ Warning]             │
│  [Nom: ______] [Email: ______]                  │
│                                                 │
│  ┌────────┬────────┬────────┐                  │
│  │🖥️     │🎨      │🔧      │                  │
│  │Fenêtre │UI      │Exéc.   │                  │
│  └────────┴────────┴────────┘                  │
│                                                 │
├─────────────────────────────────────────────────┤
│ © 2024 VisionIT  |  ✅ VisionIT Framework       │
└─────────────────────────────────────────────────┘
```

---

## 🎯 Commandes Principales

### Créer un Projet
```bash
visionit new <nom_du_projet>
```

### Base de Données
```bash
visionit db sync      # Synchroniser DB
visionit db generate  # Générer client Prisma
```

### Build Exécutable
```bash
visionit build deps      # Installer PyInstaller
visionit build onefile   # Créer exécutable unique
```

### Composants
```bash
visionit component list      # Lister composants
visionit component create navbar  # Ajouter composant
```

---

## 🔧 Personnalisation

### Changer la Fenêtre

```python
# Dans main.py
WINDOW_TITLE = "Mon Super App"
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 900
```

### Ajouter une Page

```python
@ui.page("/about")
def about_page():
    ui.label("À propos").classes("text-h4")
    ui.markdown("""
    ## Mon Application
    Créée avec VisionIT Framework
    """)
```

### Utiliser les Composants

```python
# Dans main.py
with ui.card().classes('p-6 bg-blue-50'):
    ui.label("Titre").classes("text-xl font-bold")
    ui.label("Contenu").classes("text-gray-600")
```

---

## 📦 Build en Exécutable

### Pour Votre Plateforme

```bash
cd mon_app
visionit build deps
visionit build onefile

# L'exécutable est dans : dist/
```

### Pour Toutes Plateformes

Utilisez GitHub Actions (voir `PYPI_DEPLOY.md`)

---

## ❓ Problèmes ?

### La fenêtre ne s'ouvre pas

1. Vérifiez `native=True` dans `main.py`
2. Installez pywebview : `pip install pywebview`
3. Voir `TROUBLESHOOTING.md`

### Ouvre dans le navigateur

Changez `native=False` à `native=True` dans `main.py`

### Erreur de port

Changez le port : `PORT = 8081` dans `main.py`

---

## 📚 Documentation Complète

- **DOCUMENTATION.md** - Guide complet avec exemples
- **AI_GUIDE.md** - Guide pour les IA
- **TROUBLESHOOTING.md** - Dépannage détaillé
- **PYPI_DEPLOY.md** - Publication sur PyPI
- **LANCER_APPS.md** - Lancer les applications de démo

---

## 🎉 Exemple Complet

```python
from nicegui import ui, app

WINDOW_TITLE = "Mon App"
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 800

@ui.page("/")
def index():
    ui.label("Bienvenue !").classes("text-h4")
    
    with ui.row():
        ui.button("Cliquez-moi", 
                  on_click=lambda: ui.notify("Ça marche !"))
        ui.input("Votre nom")

if __name__ == "__main__":
    app.native.title = WINDOW_TITLE
    app.native.width = WINDOW_WIDTH
    app.native.height = WINDOW_HEIGHT
    
    ui.run(
        native=True,
        window_size=(WINDOW_WIDTH, WINDOW_HEIGHT)
    )
```

---

**VisionIT Framework** - Créez des applications desktop en Python ! 🚀
