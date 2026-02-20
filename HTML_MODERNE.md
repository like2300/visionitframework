# 🎨 HTML Moderne avec Tailwind CSS - VisionIT

## ✅ Fenêtre Desktop avec HTML Moderne

Le framework VisionIT affiche maintenant un **fichier HTML moderne avec Tailwind CSS** dans une fenêtre desktop native.

---

## 🚀 Comment Lancer

```bash
cd "/Users/omerlinks/Desktop/vidionit framework/visionit/demo_window"
source ../venv/bin/activate
python main.py
```

**→ Une fenêtre s'ouvre avec un design moderne !**

---

## 🎨 Ce Que Vous Voyez

### Design Moderne

- **Gradient animé** - Fond bleu-violet avec animation
- **Cartes avec glassmorphism** - Effet de flou et transparence
- **Boutons avec gradients** - Effets hover et scale
- **Notifications** - Popup animés
- **Responsive** - S'adapte à la taille de fenêtre

### Sections

1. **Header** - Logo + Status "Fenêtre Desktop Active"
2. **Hero** - "🎉 Installation Réussie !" avec animation float
3. **Info Cards** - 3 cartes (Fenêtre Native, Tailwind CSS, 100% Fonctionnel)
4. **Interactive** - Boutons et formulaire de test
5. **Features** - 4 features (Desktop, Design, Rapide, Build)
6. **Status** - "✅ Tout Fonctionne Parfaitement !"
7. **Footer** - Copyright VisionIT

---

## 🎯 Fonctionnalités

### Animations CSS

```css
@keyframes gradient {
    /* Animation de fond */
}

@keyframes float {
    /* Effet de flottement */
}

@keyframes pulse-glow {
    /* Lueur pulsante */
}
```

### Tailwind CSS

Utilisation de toutes les classes Tailwind :

- `bg-gradient-to-br` - Dégradés
- `backdrop-blur-md` - Effet glassmorphism
- `transform hover:scale-105` - Effets hover
- `animate-pulse` - Animations
- `grid grid-cols-3` - Grilles responsive

### Interactivité JavaScript

```javascript
// Notifications
function showNotification(type) {
    // Crée une notification popup
    // Animation d'entrée/sortie
    // Auto-dismiss après 3 secondes
}

// Formulaire
function submitForm() {
    // Montre notification de succès
}
```

---

## 📁 Fichiers

### `templates/index.html`

Fichier HTML principal avec :
- Tailwind CSS via CDN
- Styles CSS personnalisés (animations)
- Structure HTML moderne
- Scripts JavaScript pour l'interactivité

### `main.py`

Script Python qui :
- Démarre le serveur NiceGUI
- Ouvre une fenêtre avec pywebview
- Charge le fichier HTML local

---

## 🎨 Personnalisation

### Changer les Couleurs

Dans `index.html`, modifiez les classes Tailwind :

```html
<!-- Changer le gradient de fond -->
<body class="bg-gradient-to-br from-blue-900 via-purple-900 to-indigo-900">

<!-- Ou pour un thème sombre -->
<body class="bg-gradient-to-br from-gray-900 via-black to-gray-900">
```

### Changer le Titre

Dans `main.py` :

```python
WINDOW_TITLE = "Mon Application - Titre Personnalisé"
```

### Changer la Taille

Dans `main.py` :

```python
WINDOW_WIDTH = 1400
WINDOW_HEIGHT = 1000
```

---

## 🧪 Test des Boutons

Cliquez sur les boutons pour tester :

- **👍 Primaire** → Notification bleue
- **✅ Succès** → Notification verte
- **⚠️ Warning** → Notification jaune
- **❌ Erreur** → Notification rouge

---

## 📸 Capture d'Écran (Textuelle)

```
┌─────────────────────────────────────────────────────────────────┐
│ VisionIT Framework                        ✅ Fenêtre Desktop    │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│              🎉 Installation Réussie !                          │
│         Votre application desktop fonctionne                    │
│                                                                 │
│  ┌──────────┬──────────┬──────────┐                            │
│  │🖥️       │🎨        │✅        │                            │
│  │Fenêtre   │Tailwind  │Fonctionnel                            │
│  │Native    │CSS       │100%     │                            │
│  └──────────┴──────────┴──────────┘                            │
│                                                                 │
│  🚀 Testez l'Interactivité                                      │
│  [👍 Primaire] [✅ Succès] [⚠️ Warning] [❌ Erreur]             │
│  [Nom: ______] [Email: ______] [📤 Envoyer]                    │
│                                                                 │
│  🖥️ Desktop  🎨 Design  ⚡ Rapide  📦 Build                     │
│                                                                 │
│  ✅ Tout Fonctionne Parfaitement !                              │
│  macOS ✓ pywebview ✓ NiceGUI ✓ Tailwind ✓                      │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│ VisionIT Framework v0.1.0        © 2024 - Fenêtre Desktop      │
└─────────────────────────────────────────────────────────────────┘
```

---

## 🔧 Dépannage

### La fenêtre est blanche

**Solution :** Vérifiez le chemin du fichier HTML

```python
# Dans main.py
html_file = Path(__file__).parent / "templates" / "index.html"
print(f"HTML file: {html_file}")  # Debug
print(f"Exists: {html_file.exists()}")  # Debug
```

### Tailwind ne charge pas

**Solution :** Vérifiez la connexion Internet (Tailwind CDN)

Ou utilisez Tailwind en local :

```bash
npm install tailwindcss
npx tailwindcss -o static/css/tailwind.css
```

### Animations ne fonctionnent pas

**Solution :** Vérifiez les préfixes CSS

```html
<style>
@keyframes gradient { ... }
</style>
```

---

## 📚 Ressources

- **Tailwind CSS :** https://tailwindcss.com/
- **pywebview :** https://pywebview.flowrl.com/
- **NiceGUI :** https://nicegui.io/

---

## 🎉 Félicitations !

Votre fenêtre desktop avec HTML moderne fonctionne sur Mac !

**VisionIT Framework** - Design moderne + Technologie native 🚀
