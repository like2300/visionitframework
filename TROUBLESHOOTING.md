# 🖥️ Guide de Dépannage - Fenêtre Desktop VisionIT

## ✅ Comment Lancer une Application

### Méthode 1 : Script de Lancement
```bash
cd test_final
./run.sh
```

### Méthode 2 : Commandes Manuelles
```bash
cd test_final
source ../venv/bin/activate
pip install -r package.txt
python main.py
```

---

## 🔧 Si la Fenêtre Ne S'Affiche PAS

### Problème 1 : pywebview non installé

**Symptôme :** Erreur "No module named 'webview'"

**Solution :**
```bash
pip install pywebview
```

### Problème 2 : native=False dans main.py

**Symptôme :** La page s'ouvre dans le navigateur au lieu d'une fenêtre

**Solution :** Vérifiez que `native=True` dans `main.py` :
```python
ui.run(
    native=True,  # ⭐ Doit être True pour fenêtre desktop
    window_size=(1000, 800),
    ...
)
```

### Problème 3 : Port déjà utilisé

**Symptôme :** Error: Address already in use

**Solution :** Changez le port dans `main.py` :
```python
PORT = 8081  # Au lieu de 8080
```

### Problème 4 : Fenêtre trop petite

**Symptôme :** La fenêtre est minuscule

**Solution :** Ajustez la taille dans `main.py` :
```python
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 900
```

---

## 🎯 Ce Que Vous Devez Voir

Quand l'application démarre correctement :

```
======================================================
🚀 LANCEMENT DE test_final
======================================================
📝 Titre: test_final
📐 Taille: 1000x800
🌐 Port: 8080
🖥️  Mode: Fenêtre Desktop Native
======================================================

⏳ Ouverture de la fenêtre...

✅ LA FENÊTRE S'AFFICHE CORRECTEMENT !
Votre application desktop VisionIT est fonctionnelle.
```

**Et une fenêtre apparaît sur votre bureau avec :**
- Barre de titre bleue
- Icone "home"
- Message de bienvenue vert
- 3 cartes (Application, Auteur, Version)
- Boutons interactifs
- Champs de saisie

---

## 🧪 Test Rapide

### Test 1 : Vérifier pywebview
```bash
python -c "import webview; print('✅ pywebview OK')"
```

### Test 2 : Vérifier nicegui
```bash
python -c "from nicegui import ui; print('✅ nicegui OK')"
```

### Test 3 : Lancer en mode navigateur (fallback)
```bash
# Si native=True ne fonctionne pas, essayez native=False
python -c "
from nicegui import ui

@ui.page('/')
def index():
    ui.label('Test OK').classes('text-h4')

ui.run(native=False)  # Ouvre dans le navigateur
"
```

---

## 📦 Installation Complète

Si rien ne fonctionne, réinstallez tout :

```bash
# Nettoyer
rm -rf venv
python -m venv venv
source venv/bin/activate

# Installer
pip install --upgrade pip
pip install nicegui pywebview prisma uvicorn

# Tester
python main.py
```

---

## 🐛 Erreurs Connues

### "Qt library could not be loaded"

**Cause :** pywebview ne trouve pas les librairies Qt

**Solution (macOS) :**
```bash
brew install qt
```

**Solution (Linux) :**
```bash
sudo apt-get install python3-pyqt5
```

**Solution (Windows) :**
```bash
pip install --upgrade pywebview
```

### "Segmentation fault"

**Cause :** Conflit avec d'autres librairies GUI

**Solution :**
```bash
pip uninstall pyobjc-framework-Cocoa
pip install pyobjc-framework-Cocoa
```

### La fenêtre se ferme immédiatement

**Cause :** Erreur dans le code Python

**Solution :** Lancez avec traceback :
```bash
python -u main.py 2>&1 | tee debug.log
```

---

## 📞 Support

Si le problème persiste :

1. **Vérifiez les logs :**
   ```bash
   python main.py 2>&1 | tee app.log
   ```

2. **Testez en mode navigateur :**
   ```python
   ui.run(native=False)  # Dans main.py
   ```

3. **Créez une issue GitHub :**
   - https://github.com/like2300/visionitframework/issues

---

## ✅ Checklist de Vérification

- [ ] pywebview est installé (`pip list | grep webview`)
- [ ] native=True dans ui.run()
- [ ] Le port 8080 est libre
- [ ] WINDOW_WIDTH et WINDOW_HEIGHT sont définis
- [ ] Les dépendances sont installées (`pip install -r package.txt`)
- [ ] Python 3.9+ est utilisé (`python --version`)

---

**VisionIT Framework** - Applications Desktop avec Python ! 🚀
