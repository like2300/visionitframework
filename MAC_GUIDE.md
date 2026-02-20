# 🍀 VisionIT sur macOS - Guide Complet

## ✅ Comment Ouvrir la Fenêtre sur Mac

### Méthode 1 : Script de Test (Recommandé)

```bash
cd /Users/omerlinks/Desktop/vidionit\ framework/visionit
source venv/bin/activate
python test_mac_window.py
```

**→ Une fenêtre devrait s'ouvrir !**

---

### Méthode 2 : Demo Window

```bash
cd demo_window
source ../venv/bin/activate
python main.py
```

---

### Méthode 3 : test_final

```bash
cd test_final
source ../venv/bin/activate
python main.py
```

---

## 🔧 Si la Fenêtre Ne S'Ouvre Pas

### Problème 1 : pywebview

**Symptôme :** Erreur "No module named 'webview'"

**Solution :**
```bash
pip install pywebview
```

---

### Problème 2 : Permission macOS

**Symptôme :** La fenêtre ne s'ouvre pas, erreur de permission

**Solution :**

1. Allez dans **System Preferences** → **Security & Privacy**
2. Onglet **Privacy**
3. Cherchez **Automation** ou **Accessibility**
4. Autorisez Python / Terminal

---

### Problème 3 : Port déjà utilisé

**Symptôme :** "Address already in use"

**Solution :**
```bash
# Tuer les processus sur le port 8080
lsof -ti:8080 | xargs kill -9

# Ou changer le port dans main.py
PORT = 8081
```

---

### Problème 4 : pywebview ne trouve pas Qt

**Symptôme :** "Qt library could not be loaded"

**Solution :**
```bash
# Réinstaller pywebview avec Qt
pip uninstall pywebview
pip install pywebview[qt]

# Ou avec Cocoa (spécial Mac)
pip install pywebview[cocoa]
```

---

## 🎯 Ce Que Vous Devez Voir

Quand la fenêtre s'ouvre correctement :

```
┌─────────────────────────────────────────────────┐
│ 🖥️ Démo VisionIT - Mac                   [_][□][X]│
├─────────────────────────────────────────────────┤
│                                                 │
│  ✅ FENÊTRE MAC FONCTIONNELLE !                 │
│                                                 │
│  ┌──────────┬──────────┬──────────┐            │
│  │Application│ Auteur  │ Version  │            │
│  │demo_window│Vision IT│  1.0.0   │            │
│  └──────────┴──────────┴──────────┘            │
│                                                 │
│  [👍 Primaire] [✅ Succès] [⚠️ Warning]        │
│  [Nom: ______] [Email: ______]                  │
│                                                 │
│       [🎉 CLIQUEZ-MOI !]                        │
│                                                 │
└─────────────────────────────────────────────────┘
```

---

## 🧪 Test Rapide

### Test 1 : Vérifier pywebview
```bash
python -c "import webview; print('OK')"
```

### Test 2 : Vérifier nicegui
```bash
python -c "from nicegui import ui; print('OK')"
```

### Test 3 : Ouvrir en mode navigateur (fallback)
```bash
# Si native ne fonctionne pas, ouvrez dans Safari/Chrome
cd demo_window
source ../venv/bin/activate

# Modifier main.py : ui.run(..., show=True)
python main.py

# Puis ouvrir : http://127.0.0.1:8080
```

---

## 📦 Installation Complète (Si Rien Ne Marche)

```bash
# Nettoyer
cd /Users/omerlinks/Desktop/vidionit\ framework/visionit
rm -rf venv
python3 -m venv venv
source venv/bin/activate

# Installer
pip install --upgrade pip
pip install nicegui pywebview prisma uvicorn

# Tester
python test_mac_window.py
```

---

## 🎨 Exemple de Code pour Mac

```python
import webview
import threading
from nicegui import ui

def start_server():
    ui.run(host='127.0.0.1', port=8080, reload=False, show=False)

def create_window():
    # Start server
    server = threading.Thread(target=start_server, daemon=True)
    server.start()
    
    # Create window
    window = webview.create_window(
        title="Mon App Mac",
        url="http://127.0.0.1:8080",
        width=1000,
        height=800,
    )
    
    webview.start()

if __name__ == "__main__":
    create_window()
```

---

## ❓ FAQ Mac

### Q: La fenêtre s'ouvre dans le navigateur, pas en desktop

**R :** Utilisez `python main.py` avec le code qui utilise `webview.create_window()` directement (pas `ui.run(native=True)`).

### Q: Erreur "Segmentation fault"

**R :** Conflit avec pyobjc. Essayez :
```bash
pip uninstall pyobjc-framework-Cocoa
pip install pyobjc-framework-Cocoa
```

### Q: La fenêtre est blanche

**R :** Le serveur NiceGUI n'a pas démarré. Attendez 2 secondes après `ui.run()` avant de créer la fenêtre.

### Q: Comment fermer la fenêtre ?

**R :** Cmd+W ou cliquez sur la croix rouge.

---

## 🚀 Applications de Démo Incluses

3 applications sont prêtes à tester :

1. **demo_window/** - Démo complète
   ```bash
   cd demo_window && python main.py
   ```

2. **text_editor_app/** - Éditeur de texte
   ```bash
   cd text_editor_app && python main.py
   ```

3. **test_final/** - Test rapide
   ```bash
   cd test_final && python main.py
   ```

---

## 📞 Support Mac

Si rien ne fonctionne :

1. **Vérifiez macOS version :**
   ```bash
   sw_vers
   # Minimum: macOS 10.13+
   ```

2. **Vérifiez Python :**
   ```bash
   python --version
   # Minimum: Python 3.9+
   ```

3. **Logs détaillés :**
   ```bash
   python main.py 2>&1 | tee mac_debug.log
   ```

4. **Test alternatif :**
   ```bash
   # Mode navigateur (toujours fonctionne)
   python -c "
   from nicegui import ui
   @ui.page('/')
   def index(): ui.label('OK')
   ui.run(show=True)
   "
   # Puis ouvrir http://127.0.0.1:8080 dans Safari
   ```

---

## ✅ Checklist Mac

- [ ] macOS 10.13 ou supérieur
- [ ] Python 3.9+ installé
- [ ] pywebview installé (`pip list | grep webview`)
- [ ] nicegui installé (`pip list | grep nicegui`)
- [ ] Permissions macOS accordées (Security & Privacy)
- [ ] Port 8080 libre (`lsof -ti:8080`)
- [ ] test_mac_window.py exécuté avec succès

---

**VisionIT Framework** - Fonctionne sur Mac ! 🍀
