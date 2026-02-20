# 🖥️ VisionIT Framework

**Framework Python pour créer des applications desktop avec fenêtre native**

---

## 🍀 Sur Mac - Test Rapide

```bash
# 1. Aller dans le dossier
cd /Users/omerlinks/Desktop/vidionit\ framework/visionit

# 2. Activer l'environnement
source venv/bin/activate

# 3. Lancer le test
python test_mac_window.py

# ✅ Une fenêtre Mac native s'ouvre !
```

**Si ça ne marche pas :** → Lisez [MAC_GUIDE.md](MAC_GUIDE.md)

---

## ⚡ Démarrage en 30 Secondes

```bash
# 1. Installer le framework
pip install visionit

# 2. Créer une application
visionit new mon_app
cd mon_app

# 3. Lancer
pip install -r package.txt
python main.py

# ✅ Une fenêtre desktop s'ouvre sur votre bureau !
```

---

## 🎯 Ce Que Vous Obtenez

### Une Vraie Fenêtre Desktop (Pas dans le Navigateur !)

```
┌─────────────────────────────────────────────────┐
│ mon_app  v1.0.0                          [_][□][X]│
├─────────────────────────────────────────────────┤
│ 🏠 mon_app                                       │
│                                                 │
│  ✅ Application Démarrée avec Succès !          │
│                                                 │
│  [👍 Test] [✅ Succès] [⚠️ Warning]             │
│  [Nom: ______] [Email: ______]                  │
│                                                 │
└─────────────────────────────────────────────────┘
```

### Fonctionnalités Incluses

- ✅ **Fenêtre native** avec pywebview
- 🎨 **UI moderne** avec NiceGUI + Tailwind CSS
- 💾 **Base de données** Prisma + SQLite
- 📦 **Exécutables** PyInstaller (Mac, Linux, Windows)
- 🧩 **10 composants** UI réutilisables
- 🔧 **CLI complet** pour générer et build

---

## 📚 Documentation

| Fichier | Description |
|---------|-------------|
| **[MAC_GUIDE.md](MAC_GUIDE.md)** | 🍀 **Guide spécial macOS** - Ouvre la fenêtre sur Mac |
| **[COMMENT_FAIRE.md](COMMENT_FAIRE.md)** | 📘 Guide pratique "Comment faire" |
| **[TROUBLESHOOTING.md](TROUBLESHOOTING.md)** | 🔧 Dépannage (fenêtre ne s'ouvre pas, etc.) |
| **[DOCUMENTATION.md](DOCUMENTATION.md)** | 📖 Documentation complète avec exemples |
| **[LANCER_APPS.md](LANCER_APPS.md)** | 🚀 Lancer les applications de démo |
| **[AI_GUIDE.md](AI_GUIDE.md)** | 🤖 Guide pour les IA |
| **[PYPI_DEPLOY.md](PYPI_DEPLOY.md)** | 📦 Publier sur PyPI |

---

## 🛠️ Commandes Principales

### Créer un Projet
```bash
visionit new <nom>
```

### Lancer l'Application
```bash
cd <nom>
pip install -r package.txt
python main.py  # ✅ Ouvre une fenêtre desktop
```

### Build en Exécutable
```bash
visionit build deps
visionit build onefile  # Crée .exe ou .app
```

### Base de Données
```bash
visionit db sync
visionit db generate
```

### Composants
```bash
visionit component list
visionit component create navbar
```

---

## 🔧 Si la Fenêtre Ne S'Ouvre Pas

### Solution Rapide

1. **Vérifiez pywebview :**
   ```bash
   pip install pywebview
   ```

2. **Vérifiez `native=True` :**
   Dans `main.py`, assurez-vous que :
   ```python
   ui.run(native=True, ...)  # ⭐ Important !
   ```

3. **Lisez le guide de dépannage :**
   ```bash
   cat TROUBLESHOOTING.md
   ```

---

## 📦 Installation

### Depuis PyPI (Recommandé)
```bash
pip install visionit
```

### Depuis GitHub
```bash
git clone https://github.com/like2300/visionitframework.git
cd visionitframework
pip install -e .
```

### Mode Développement
```bash
pip install -e ".[dev,build]"
```

---

## 🎉 Exemple de Code

### Application Simple

```python
from nicegui import ui

@ui.page("/")
def index():
    ui.label("Bienvenue !").classes("text-h4")
    ui.button("Cliquez-moi", 
              on_click=lambda: ui.notify("Ça marche !"))

if __name__ == "__main__":
    ui.run(native=True, window_size=(800, 600))
```

### Avec Base de Données

```python
from prisma import Prisma

db = Prisma()
await db.connect()

# Créer un utilisateur
user = await db.user.create({
    'email': 'test@example.com',
    'name': 'Test'
})
```

---

## 🖥️ Applications de Démo Incluses

Le framework inclut 2 applications de démo pour tester :

### 1. Demo Window
```bash
cd demo_window
python main.py
```

### 2. Text Editor
```bash
cd text_editor_app
python main.py
```

---

## 📞 Support

- **Issues GitHub :** https://github.com/like2300/visionitframework/issues
- **Documentation :** Voir les fichiers `.md` dans ce repository
- **Email :** contact@visionit.com

---

## ✅ Checklist de Vérification

Après installation, testez :

- [ ] `visionit --help` fonctionne
- [ ] `visionit new test_app` crée un projet
- [ ] `python main.py` ouvre une fenêtre desktop
- [ ] Les boutons sont cliquables
- [ ] Les notifications s'affichent

Si tout est ✅, votre framework est prêt !

---

## 🚀 Prêt à Créer ?

```bash
visionit new mon_super_app
cd mon_super_app
python main.py
```

**VisionIT Framework** - Applications Desktop avec Python ! 🎉

---

## 📄 Licence

MIT License - Voir [LICENSE](LICENSE)

---

**GitHub :** https://github.com/like2300/visionitframework  
**PyPI :** https://pypi.org/project/visionit/ (bientôt)
