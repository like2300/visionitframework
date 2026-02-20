# 📚 VisionIT Framework - Documentation Complète

**Version:** 0.1.0  
**Auteur:** Vision IT  
**Licence:** MIT  
**Python Requis:** 3.9+

---

## 📖 Table des Matières

1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Création d'un Projet](#création-dun-projet)
4. [Structure du Projet](#structure-du-projet)
5. [Configuration](#configuration)
6. [Base de Données](#base-de-données)
7. [Composants HTML](#composants-html)
8. [Templates](#templates)
9. [Fichiers Statiques](#fichiers-statiques)
10. [Actions (Logique NiceGUI)](#actions-logique-nicegui)
11. [Construction d'Exécutables](#construction-dexécutables)
12. [Cas Pratiques](#cas-pratiques)
13. [FAQ et Dépannage](#faq-et-dépannage)

---

## 🎯 Introduction

VisionIT est un framework de scaffolding (génération de structure de projet) pour créer rapidement des applications Python avec :

- **NiceGUI** - Interface utilisateur web moderne
- **Prisma ORM** - Gestion de base de données type-safe
- **SQLite** - Base de données légère (extensible vers PostgreSQL/MySQL)
- **PyInstaller** - Création d'exécutables pour Mac, Linux, Windows
- **Composants HTML réutilisables** - Accélération du développement frontend

### Pourquoi VisionIT ?

- ⚡ **Démarrage rapide** - Projet prêt en 30 secondes
- 🎨 **UI moderne** - Tailwind CSS inclus
- 🔧 **CLI puissant** - Toutes les commandes utiles
- 📦 **Multi-plateforme** - Build pour tous les OS
- 🧩 **Composants** - Bibliothèque de composants réutilisables

---

## 📥 Installation

### Installation Globale

```bash
pip install visionit
```

### Installation en Mode Développement

```bash
# Cloner le repository
git clone https://github.com/visionit/visionit.git
cd visionit

# Installer avec les dépendances de développement
pip install -e ".[dev,build]"
```

### Vérification

```bash
visionit --help
visionit version
```

---

## 🚀 Création d'un Projet

### Mode Interactif

```bash
visionit new mon_application
```

Le CLI posera les questions suivantes :
- Nom du développeur
- Version de l'application
- ORM (Prisma par défaut)
- Base de données (SQLite par défaut)

### Mode Non-Interactif (CI/CD)

```bash
visionit new mon_application --no-interactive
```

### Structure Générée

```
mon_application/
├── db/
│   └── schema.prisma      # Schéma de base de données
├── templates/
│   ├── index.html         # Page d'accueil
│   └── components/        # Composants réutilisables
│       ├── navbar.html
│       ├── footer.html
│       ├── card.html
│       ├── button.html
│       ├── input.html
│       ├── alert.html
│       └── modal.html
├── static/
│   ├── css/
│   │   └── main.css       # Styles personnalisés
│   ├── js/
│   │   └── main.js        # Scripts JavaScript
│   └── icons/             # Icônes pour l'application
│       └── README.md
├── actions/
│   └── main_logic.py      # Logique métier NiceGUI
├── info.json              # Métadonnées du projet
├── package.txt            # Dépendances Python
├── build.json             # Configuration de build
├── main.py                # Point d'entrée
└── README.md              # Documentation du projet
```

---

## ⚙️ Configuration

### info.json

Fichier de métadonnées du projet :

```json
{
  "project_name": "mon_application",
  "author": "Votre Nom",
  "version": "1.0.0",
  "orm": "Prisma",
  "database": "SQLite"
}
```

**Utilisation dans le code :**

```python
from pathlib import Path
import json

INFO_FILE = Path(__file__).parent / "info.json"
with open(INFO_FILE, "r", encoding="utf-8") as f:
    project_info = json.load(f)

print(f"Application: {project_info['project_name']}")
print(f"Version: {project_info['version']}")
```

### package.txt

Liste des dépendances Python :

```
nicegui>=1.4.0
prisma>=0.11.0
pywebview>=4.4.0
uvicorn>=0.24.0
```

**Installation :**

```bash
visionit install
# ou
pip install -r package.txt
```

### build.json

Configuration pour PyInstaller :

```json
{
  "app_name": "mon_application",
  "main_module": "main",
  "icon": "static/icons/icon_256.png",
  "onefile": true,
  "windowed": false,
  "hidden_imports": [
    "nicegui",
    "nicegui.elements",
    "uvicorn"
  ],
  "exclude_modules": [
    "matplotlib",
    "numpy"
  ],
  "add_data": [
    ["templates", "templates"],
    ["static", "static"],
    ["db", "db"]
  ]
}
```

**Options :**

| Option | Type | Description |
|--------|------|-------------|
| `app_name` | string | Nom de l'application et de l'exécutable |
| `main_module` | string | Module Python principal (sans .py) |
| `icon` | string | Chemin vers l'icône de l'application |
| `onefile` | boolean | true = exécutable unique, false = dossier |
| `windowed` | boolean | true = pas de console, false = avec console |
| `hidden_imports` | array | Modules à inclure explicitement |
| `exclude_modules` | array | Modules à exclure pour réduire la taille |
| `add_data` | array | Fichiers/dossiers à inclure dans l'exécutable |

---

## 🗄️ Base de Données

### Configuration Prisma

Fichier : `db/schema.prisma`

```prisma
datasource db {
  provider = "sqlite"
  url      = "file:../dev.db"
}

generator client {
  provider = "prisma-client-py"
}

model User {
  id        Int      @id @default(autoincrement())
  email     String   @unique
  name      String?
  password  String?
  role      String   @default("user")
  createdAt DateTime @default(now())
  updatedAt DateTime @updatedAt
  posts     Post[]
}

model Post {
  id        Int      @id @default(autoincrement())
  title     String
  content   String?
  published Boolean  @default(false)
  authorId  Int
  author    User     @relation(fields: [authorId], references: [id])
  createdAt DateTime @default(now())
  updatedAt DateTime @updatedAt
}
```

### Commandes de Base de Données

**Initialiser la base de données :**

```bash
# Synchroniser le schéma avec la DB
visionit db sync

# Générer le client Prisma
visionit db generate
```

### Utilisation dans le Code

```python
# actions/database.py
from prisma import Prisma

db = Prisma()

async def init_db():
    await db.connect()
    return db

async def create_user(email: str, name: str):
    user = await db.user.create({
        'email': email,
        'name': name
    })
    return user

async def get_all_users():
    users = await db.user.find_many()
    return users

async def get_user_by_id(user_id: int):
    user = await db.user.find_unique(where={'id': user_id})
    return user

async def update_user(user_id: int, **kwargs):
    user = await db.user.update(
        where={'id': user_id},
        data=kwargs
    )
    return user

async def delete_user(user_id: int):
    await db.user.delete(where={'id': user_id})
```

### Exemple Complet avec NiceGUI

```python
# main.py
from nicegui import ui
from prisma import Prisma

db = Prisma()

@ui.page("/")
async def index():
    await db.connect()
    users = await db.user.find_many()
    
    ui.label("Liste des utilisateurs").classes("text-h4")
    
    for user in users:
        with ui.card():
            ui.label(f"Nom: {user.name}")
            ui.label(f"Email: {user.email}")

@ui.page("/create-user")
async def create_user_page():
    await db.connect()
    
    with ui.form().classes("w-full max-w-md"):
        ui.input("Nom", key="name").classes("w-full")
        ui.input("Email", key="email").classes("w-full")
        
        ui.button("Créer", on_click=lambda: create_user())
    
    async def create_user():
        name = ui.context.client.content["name"]
        email = ui.context.client.content["email"]
        await db.user.create({'name': name, 'email': email})
        ui.notify("Utilisateur créé !")
        ui.navigate.to("/")

if __name__ == "__main__":
    ui.run()
```

---

## 🧩 Composants HTML

### Système de Composants

VisionIT inclut un système de composants HTML basés sur **Tailwind CSS** et **Jinja2**.

### Liste des Composants

#### 1. Navbar

**Fichier:** `templates/components/navbar.html`

**Variables :**
- `app_name` - Nom de l'application
- `app_icon` - URL de l'icône
- `nav_items` - Liste des liens [{label, url}]

**Exemple d'utilisation :**

```html
{% set nav_items = [
    {'label': 'Accueil', 'url': '/'},
    {'label': 'Produits', 'url': '/products'},
    {'label': 'Contact', 'url': '/contact'}
] %}

{% include 'components/navbar.html' %}
```

#### 2. Footer

**Fichier:** `templates/components/footer.html`

**Variables :**
- `footer_title` - Titre de section
- `footer_description` - Description
- `footer_links` - Liens [{label, url}]
- `social_links` - Réseaux sociaux {platform: url}
- `year` - Année
- `copyright_owner` - Propriétaire

**Exemple :**

```html
{% set footer_links = [
    {'label': 'Mentions légales', 'url': '/legal'},
    {'label': 'Confidentialité', 'url': '/privacy'}
] %}

{% set social_links = {
    'twitter': 'https://twitter.com/visionit',
    'github': 'https://github.com/visionit'
} %}

{% include 'components/footer.html' %}
```

#### 3. Card

**Fichier:** `templates/components/card.html`

**Variables :**
- `card_title` - Titre de la carte
- `card_description` - Description
- `card_image` - URL de l'image
- `card_badge` - Badge optionnel
- `card_link` - Lien
- `card_link_text` - Texte du lien
- `card_class` - Classes CSS additionnelles

**Exemple :**

```html
{% for product in products %}
    {% include 'components/card.html' with {
        card_title: product.name,
        card_description: product.description,
        card_image: product.image,
        card_link: '/product/' ~ product.id,
        card_link_text: 'Voir le produit',
        card_badge: 'Nouveau' if product.is_new else null
    } %}
{% endfor %}
```

#### 4. Button

**Fichier:** `templates/components/button.html`

**Variables :**
- `button_text` - Texte du bouton
- `button_style` - primary, secondary, success, danger, warning, outline, ghost
- `button_size` - sm, md, lg
- `button_type` - button, submit, reset
- `button_onclick` - Action JavaScript
- `button_disabled` - true/false
- `button_class` - Classes CSS additionnelles

**Exemple :**

```html
<!-- Bouton primary -->
{% include 'components/button.html' with {
    button_text: 'Valider',
    button_style: 'primary',
    button_size: 'md'
} %}

<!-- Bouton danger -->
{% include 'components/button.html' with {
    button_text: 'Supprimer',
    button_style: 'danger',
    button_onclick: 'confirmDelete()'
} %}
```

#### 5. Input

**Fichier:** `templates/components/input.html`

**Variables :**
- `input_id` - ID HTML
- `input_name` - Nom du champ
- `input_type` - text, email, password, number, textarea, etc.
- `label` - Étiquette
- `placeholder` - Texte de remplacement
- `value` - Valeur par défaut
- `required` - true/false
- `help_text` - Texte d'aide
- `error` - Message d'erreur

**Exemple :**

```html
<form action="/submit" method="POST">
    {% include 'components/input.html' with {
        input_id: 'email',
        input_name: 'email',
        input_type: 'email',
        label: 'Adresse email',
        placeholder: 'vous@exemple.com',
        required: true,
        help_text: 'Nous ne partagerons jamais votre email'
    } %}
    
    {% include 'components/input.html' with {
        input_id: 'message',
        input_name: 'message',
        input_type: 'textarea',
        label: 'Message',
        rows: 5,
        required: true
    } %}
    
    {% include 'components/button.html' with {
        button_text: 'Envoyer',
        button_type: 'submit'
    } %}
</form>
```

#### 6. Alert

**Fichier:** `templates/components/alert.html`

**Variables :**
- `alert_type` - info, success, warning, error
- `alert_title` - Titre
- `message` - Message
- `alert_dismissible` - true/false
- `alert_show_icon` - true/false

**Exemple :**

```html
<!-- Alert succès -->
{% include 'components/alert.html' with {
    alert_type: 'success',
    alert_title: 'Succès !',
    message: 'Votre modification a été enregistrée.',
    alert_dismissible: true
} %}

<!-- Alert erreur -->
{% include 'components/alert.html' with {
    alert_type: 'error',
    alert_title: 'Erreur',
    message: 'Une erreur est survenue.',
    alert_show_icon: true
} %}
```

#### 7. Modal

**Fichier:** `templates/components/modal.html`

**Variables :**
- `modal_id` - ID unique
- `modal_title` - Titre
- `modal_content` - Contenu
- `modal_icon` - Icône SVG
- `modal_confirm_text` - Texte du bouton confirmer
- `modal_confirm_action` - Action JavaScript
- `modal_cancel_text` - Texte du bouton annuler

**Exemple :**

```html
<!-- Bouton pour ouvrir la modal -->
<button onclick="toggleModal('confirmModal')">
    Supprimer
</button>

<!-- Modal -->
{% include 'components/modal.html' with {
    modal_id: 'confirmModal',
    modal_title: 'Confirmer la suppression',
    modal_content: 'Êtes-vous sûr de vouloir supprimer cet élément ?',
    modal_confirm_text: 'Supprimer',
    modal_confirm_action: 'deleteItem()',
    modal_confirm_color: 'red',
    modal_cancel_text: 'Annuler'
} %}

<script>
function deleteItem() {
    // Logique de suppression
    console.log('Item deleted');
}
</script>
```

#### 8. Hero

**Fichier:** `templates/components/hero.html`

**Variables :**
- `hero_title` - Titre principal
- `hero_subtitle` - Sous-titre
- `hero_cta_text` - Texte du CTA
- `hero_cta_link` - Lien du CTA

**Exemple :**

```html
{% include 'components/hero.html' with {
    hero_title: 'Bienvenue sur Notre Plateforme',
    hero_subtitle: 'La solution complète pour gérer votre activité',
    hero_cta_text: 'Commencer maintenant',
    hero_cta_link: '/signup'
} %}
```

#### 9. Feature

**Fichier:** `templates/components/feature.html`

**Variables :**
- `feature_icon` - SVG de l'icône
- `feature_title` - Titre
- `feature_description` - Description

**Exemple :**

```html
<div class="grid grid-cols-1 md:grid-cols-3 gap-8">
    {% include 'components/feature.html' with {
        feature_icon: '<path d="M13 10V3L4 14h7v7l9-11h-7z"/>',
        feature_title: 'Rapide',
        feature_description: 'Performance optimisée pour une expérience fluide'
    } %}
    
    {% include 'components/feature.html' with {
        feature_icon: '<path d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z"/>',
        feature_title: 'Sécurisé',
        feature_description: 'Vos données sont protégées et chiffrées'
    } %}
</div>
```

#### 10. Testimonial

**Fichier:** `templates/components/testimonial.html`

**Variables :**
- `testimonial_text` - Texte du témoignage
- `author_name` - Nom de l'auteur
- `author_title` - Titre de l'auteur
- `author_avatar` - URL de l'avatar

**Exemple :**

```html
{% include 'components/testimonial.html' with {
    testimonial_text: 'Ce produit a transformé notre façon de travailler. Je le recommande vivement !',
    author_name: 'Jean Dupont',
    author_title: 'CEO, TechCorp',
    author_avatar: '/images/avatars/jean.jpg'
} %}
```

### Créer un Composant Personnalisé

```bash
# Créer un nouveau composant
visionit component new sidebar

# Le composant sera créé dans templates/components/sidebar.html
```

**Exemple de composant personnalisé :**

```html
<!-- templates/components/sidebar.html -->
<aside class="w-64 bg-gray-800 text-white min-h-screen">
    <div class="p-4">
        <h2 class="text-xl font-bold mb-4">{{ sidebar_title|default('Menu') }}</h2>
        
        <nav class="space-y-2">
            {% for item in sidebar_items|default([]) %}
            <a href="{{ item.url }}" 
               class="block px-4 py-2 rounded hover:bg-gray-700 {{ 'bg-gray-700' if item.active else '' }}">
                {{ item.label }}
            </a>
            {% endfor %}
        </nav>
    </div>
</aside>

<!-- Utilisation -->
{% set sidebar_items = [
    {'label': 'Tableau de bord', 'url': '/dashboard', 'active': true},
    {'label': 'Paramètres', 'url': '/settings', 'active': false}
] %}

{% include 'components/sidebar.html' %}
```

---

## 🎨 Templates

### Template de Base

**Fichier:** `templates/base.html`

```html
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}VisionIT App{% endblock %}</title>
    
    <!-- Tailwind CSS -->
    <script src="https://cdn.tailwindcss.com"></script>
    
    <!-- Custom CSS -->
    <link rel="stylesheet" href="/static/css/main.css">
    
    {% block extra_head %}{% endblock %}
</head>
<body class="bg-gray-50 min-h-screen">
    <!-- Navigation -->
    {% include 'components/navbar.html' %}
    
    <!-- Main Content -->
    <main class="container mx-auto px-4 py-8">
        {% block content %}{% endblock %}
    </main>
    
    <!-- Footer -->
    {% include 'components/footer.html' %}
    
    <!-- Custom JS -->
    <script src="/static/js/main.js"></script>
    
    {% block extra_scripts %}{% endblock %}
</body>
</html>
```

### Étendre un Template

```html
{% extends 'base.html' %}

{% block title %}Accueil - Mon Application{% endblock %}

{% block content %}
<div class="max-w-4xl mx-auto">
    <h1 class="text-3xl font-bold mb-6">Bienvenue</h1>
    
    <p class="text-gray-700 mb-8">
        Ceci est la page d'accueil de votre application.
    </p>
    
    <!-- Utiliser des composants -->
    {% include 'components/card.html' with {
        card_title: 'Fonctionnalité 1',
        card_description: 'Description de la fonctionnalité'
    } %}
</div>
{% endblock %}

{% block extra_scripts %}
<script>
    console.log('Page chargée');
</script>
{% endblock %}
```

---

## 📁 Fichiers Statiques

### CSS Personnalisé

**Fichier:** `static/css/main.css`

```css
/* Styles globaux */
body {
    font-family: 'Inter', sans-serif;
}

/* Classes utilitaires personnalisées */
.text-gradient {
    background: linear-gradient(to right, #3b82f6, #8b5cf6);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

/* Animations */
@keyframes fadeIn {
    from { opacity: 0; }
    to { opacity: 1; }
}

.animate-fade-in {
    animation: fadeIn 0.3s ease-in-out;
}
```

### JavaScript Personnalisé

**Fichier:** `static/js/main.js`

```javascript
// Initialisation globale
document.addEventListener('DOMContentLoaded', function() {
    console.log('Application initialisée');
    
    // Initialiser les tooltips
    initTooltips();
    
    // Initialiser les modals
    initModals();
});

// Fonction utilitaire pour les notifications
function notify(message, type = 'info') {
    const notification = document.createElement('div');
    notification.className = `alert alert-${type}`;
    notification.textContent = message;
    document.body.appendChild(notification);
    
    setTimeout(() => {
        notification.remove();
    }, 3000);
}

// Gestion des formulaires AJAX
async function submitForm(formElement) {
    const formData = new FormData(formElement);
    
    try {
        const response = await fetch(formElement.action, {
            method: formElement.method,
            body: formData
        });
        
        const result = await response.json();
        
        if (result.success) {
            notify(result.message, 'success');
        } else {
            notify(result.error, 'error');
        }
    } catch (error) {
        notify('Une erreur est survenue', 'error');
    }
}
```

### Icônes

**Structure:** `static/icons/`

```
icons/
├── README.md           # Instructions pour les icônes
├── icon_16.png         # Favicon petit
├── icon_32.png         # Favicon
├── icon_128.png        # macOS
├── icon_256.png        # macOS, Windows
├── icon_512.png        # Haute résolution
└── icon_1024.png       # App Store
```

**Pour Windows (.ico) :**

```bash
# Créer un fichier .ico multi-tailles
convert icon_16.png icon_32.png icon_48.png icon_256.png icon.ico
```

**Pour macOS (.icns) :**

```bash
mkdir icon.iconset
cp icon_16.png icon.iconset/icon_16x16.png
cp icon_32.png icon.iconset/icon_16x16@2x.png
cp icon_128.png icon.iconset/icon_128x128.png
cp icon_256.png icon.iconset/icon_128x128@2x.png
cp icon_512.png icon.iconset/icon_256x256@2x.png
cp icon_1024.png icon.iconset/icon_512x512@2x.png
iconutil -c icns icon.iconset
```

---

## ⚡ Actions (Logique NiceGUI)

### Structure des Actions

**Fichier:** `actions/main_logic.py`

```python
"""
Module de logique métier pour l'application.
Séparez votre logique NiceGUI dans ce dossier.
"""

from nicegui import ui
from typing import Optional, List, Dict, Any
from prisma import Prisma


class UserManager:
    """Gestion des utilisateurs."""
    
    def __init__(self, db: Prisma):
        self.db = db
    
    async def get_current_user(self, user_id: int) -> Optional[Dict]:
        """Récupérer l'utilisateur actuel."""
        user = await self.db.user.find_unique(where={'id': user_id})
        return user.dict() if user else None
    
    async def authenticate(self, email: str, password: str) -> Optional[Dict]:
        """Authentifier un utilisateur."""
        user = await self.db.user.find_unique(where={'email': email})
        
        if user and self.verify_password(password, user.password):
            return user.dict()
        return None
    
    def verify_password(self, plain: str, hashed: str) -> bool:
        """Vérifier le mot de passe."""
        # Implémenter la vérification avec bcrypt/argon2
        import bcrypt
        return bcrypt.checkpw(plain.encode(), hashed.encode())


class ProductManager:
    """Gestion des produits."""
    
    def __init__(self, db: Prisma):
        self.db = db
    
    async def get_all_products(self) -> List[Dict]:
        """Récupérer tous les produits."""
        products = await self.db.product.find_many()
        return [p.dict() for p in products]
    
    async def get_product(self, product_id: int) -> Optional[Dict]:
        """Récupérer un produit par ID."""
        product = await self.db.product.find_unique(
            where={'id': product_id}
        )
        return product.dict() if product else None
    
    async def create_product(self, data: Dict) -> Dict:
        """Créer un nouveau produit."""
        product = await self.db.product.create(data=data)
        return product.dict()
    
    async def update_product(self, product_id: int, data: Dict) -> Dict:
        """Mettre à jour un produit."""
        product = await self.db.product.update(
            where={'id': product_id},
            data=data
        )
        return product.dict()
    
    async def delete_product(self, product_id: int) -> bool:
        """Supprimer un produit."""
        await self.db.product.delete(where={'id': product_id})
        return True


# Fonctions utilitaires pour NiceGUI

def create_notification(message: str, type: str = 'info'):
    """Créer une notification NiceGUI."""
    ui.notify(
        message,
        type=type,
        position='top-right',
        timeout=3000
    )


def create_card(title: str, content: str, link: Optional[str] = None):
    """Créer une carte NiceGUI."""
    with ui.card().classes('w-full p-4'):
        ui.label(title).classes('text-lg font-semibold')
        ui.label(content).classes('text-gray-600 mt-2')
        
        if link:
            ui.link('Voir plus', link).classes('text-blue-600 mt-2')


def create_form_field(
    label: str,
    key: str,
    field_type: str = 'text',
    required: bool = False
):
    """Créer un champ de formulaire NiceGUI."""
    if field_type == 'textarea':
        return ui.textarea(label=label, key=key, required=required)
    elif field_type == 'password':
        return ui.input(
            label=label,
            key=key,
            password=True,
            password_toggle_button=True,
            required=required
        )
    else:
        return ui.input(label=label, key=key, required=required)
```

### Intégration avec main.py

```python
# main.py
from nicegui import ui, app
from pathlib import Path
import json
from actions.main_logic import UserManager, ProductManager, create_notification
from prisma import Prisma

# Initialisation de la base de données
db = Prisma()

@app.get("/startup")
async def startup():
    await db.connect()

@app.get("/shutdown")
async def shutdown():
    await db.disconnect()

# Initialiser les managers
user_manager = UserManager(db)
product_manager = ProductManager(db)

@ui.page("/")
async def index():
    ui.label("Bienvenue").classes("text-h4")
    
    products = await product_manager.get_all_products()
    
    for product in products:
        create_card(
            title=product['name'],
            content=product['description'],
            link=f"/product/{product['id']}"
        )

@ui.page("/login")
async def login_page():
    ui.label("Connexion").classes("text-h4")
    
    with ui.form().classes("w-full max-w-md"):
        email = ui.input("Email", key="email")
        password = ui.input(
            "Mot de passe",
            key="password",
            password=True,
            password_toggle_button=True
        )
        
        async def do_login():
            user = await user_manager.authenticate(
                email=email.value,
                password=password.value
            )
            
            if user:
                create_notification("Connexion réussie !", "positive")
                ui.navigate.to("/")
            else:
                create_notification("Email ou mot de passe incorrect", "negative")
        
        ui.button("Se connecter", on_click=do_login)

if __name__ == "__main__":
    ui.run(
        title="Mon Application",
        host="0.0.0.0",
        port=8080,
        reload=False
    )
```

---

## 🔨 Construction d'Exécutables

### Installation des Dépendances de Build

```bash
visionit build deps
```

### Build pour la Plateforme Actuelle

**Mode Onefile (exécutable unique) :**

```bash
visionit build onefile
```

Sortie : `dist/mon_application` (ou `.exe` sur Windows)

**Mode Onedir (dossier avec dépendances) :**

```bash
visionit build onedir
```

Sortie : `dist/mon_application/` (dossier complet)

**Build Complet (les deux modes) :**

```bash
visionit build all
```

### Configuration pour Multi-Plateforme

#### macOS

```json
{
  "app_name": "MonApp",
  "icon": "static/icons/icon_256.png",
  "windowed": true
}
```

```bash
# Build pour macOS
visionit build onefile

# L'application sera dans dist/MonApp.app
```

#### Windows

```json
{
  "app_name": "MonApp",
  "icon": "static/icons/icon.ico",
  "windowed": true
}
```

```bash
# Build pour Windows (depuis Windows)
visionit build onefile

# L'application sera dans dist/MonApp.exe
```

#### Linux

```json
{
  "app_name": "mon-app",
  "icon": "static/icons/icon_256.png",
  "windowed": false
}
```

```bash
# Build pour Linux
visionit build onefile

# L'application sera dans dist/mon-app
```

### Build Cross-Platform avec CI/CD

**GitHub Actions (.github/workflows/build.yml) :**

```yaml
name: Build Executables

on:
  push:
    tags:
      - 'v*'

jobs:
  build:
    strategy:
      matrix:
        os: [ubuntu-latest, macos-latest, windows-latest]
    
    runs-on: ${{ matrix.os }}
    
    steps:
      - uses: actions/checkout@v3
      
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      
      - name: Install dependencies
        run: |
          pip install -r package.txt
          pip install pyinstaller
      
      - name: Build executable
        run: |
          visionit build onefile
      
      - name: Upload artifact
        uses: actions/upload-artifact@v3
        with:
          name: ${{ runner.os }}-build
          path: dist/
```

---

## 📚 Cas Pratiques

### Cas 1 : Application de Gestion de Tâches

**Structure :**

```
task_manager/
├── db/
│   └── schema.prisma
├── templates/
│   └── components/
├── actions/
│   ├── task_manager.py
│   └── auth.py
├── static/
├── main.py
└── build.json
```

**Schéma Prisma :**

```prisma
model User {
  id       Int    @id @default(autoincrement())
  email    String @unique
  password String
  tasks    Task[]
}

model Task {
  id          Int      @id @default(autoincrement())
  title       String
  description String?
  completed   Boolean  @default(false)
  dueDate     DateTime?
  userId      Int
  user        User     @relation(fields: [userId], references: [id])
  createdAt   DateTime @default(now())
  updatedAt   DateTime @updatedAt
}
```

**Logique NiceGUI (actions/task_manager.py) :**

```python
from nicegui import ui
from prisma import Prisma

db = Prisma()

async def get_user_tasks(user_id: int):
    tasks = await db.task.find_many(
        where={'userId': user_id},
        order={'createdAt': 'desc'}
    )
    return tasks

async def create_task(user_id: int, title: str, description: str = None):
    task = await db.task.create(
        data={
            'title': title,
            'description': description,
            'userId': user_id
        }
    )
    return task

async def toggle_task(task_id: int):
    task = await db.task.find_unique(where={'id': task_id})
    await db.task.update(
        where={'id': task_id},
        data={'completed': not task.completed}
    )

async def delete_task(task_id: int):
    await db.task.delete(where={'id': task_id})
```

**Interface (main.py) :**

```python
from nicegui import ui
from actions.task_manager import get_user_tasks, create_task, toggle_task, delete_task

current_user_id = 1  # À remplacer par une vraie authentification

@ui.page("/")
async def task_list():
    ui.label("Mes Tâches").classes("text-2xl font-bold mb-4")
    
    # Formulaire d'ajout
    with ui.row().classes("w-full mb-4"):
        title_input = ui.input("Titre").classes("flex-grow")
        desc_input = ui.input("Description").classes("flex-grow")
        
        async def add_task():
            await create_task(current_user_id, title_input.value, desc_input.value)
            title_input.value = ""
            desc_input.value = ""
            ui.navigate.reload()
        
        ui.button("Ajouter", on_click=add_task)
    
    # Liste des tâches
    tasks = await get_user_tasks(current_user_id)
    
    for task in tasks:
        with ui.card().classes("w-full"):
            with ui.row().classes("w-full items-center"):
                ui.checkbox(
                    value=task.completed,
                    on_change=lambda t=task: toggle_task(t.id)
                ).props(f'disable={task.completed}')
                
                ui.label(task.title).classes(
                    "flex-grow " + ("line-through text-gray-400" if task.completed else "")
                )
                
                ui.button(
                    icon="delete",
                    on_click=lambda t=task: delete_task(t.id)
                ).props("flat color=red")

if __name__ == "__main__":
    ui.run()
```

### Cas 2 : Dashboard de Vente

**Composants utilisés :** navbar, card, hero, feature, alert

```python
from nicegui import ui
from datetime import datetime, timedelta

@ui.page("/dashboard")
async def sales_dashboard():
    # Hero section
    ui.html("""
    <section class="bg-gradient-to-r from-blue-600 to-purple-600 text-white py-12 rounded-lg mb-8">
        <div class="text-center">
            <h1 class="text-4xl font-bold mb-4">Dashboard des Ventes</h1>
            <p class="text-xl">Suivez vos performances en temps réel</p>
        </div>
    </section>
    """)
    
    # KPI Cards
    with ui.row().classes("w-full gap-4 mb-8"):
        with ui.card().classes("flex-1 p-6"):
            ui.label("Ventes du jour").classes("text-gray-600")
            ui.label("1,234 €").classes("text-3xl font-bold text-green-600")
            ui.label("+12% vs hier").classes("text-sm text-green-500")
        
        with ui.card().classes("flex-1 p-6"):
            ui.label("Commandes").classes("text-gray-600")
            ui.label("45").classes("text-3xl font-bold text-blue-600")
            ui.label("+5 vs hier").classes("text-sm text-blue-500")
        
        with ui.card().classes("flex-1 p-6"):
            ui.label("Clients").classes("text-gray-600")
            ui.label("128").classes("text-3xl font-bold text-purple-600")
            ui.label("+8 nouveaux").classes("text-sm text-purple-500")
    
    # Features
    ui.label("Fonctionnalités").classes("text-2xl font-bold mb-4")
    
    with ui.row().classes("w-full gap-4"):
        with ui.card().classes("flex-1 p-6 text-center"):
            ui.icon("show_chart", size="48px").classes("text-blue-600")
            ui.label("Analytics").classes("text-xl font-semibold mt-2")
            ui.label("Graphiques détaillés").classes("text-gray-600 mt-2")
        
        with ui.card().classes("flex-1 p-6 text-center"):
            ui.icon("people", size="48px").classes("text-green-600")
            ui.label("Clients").classes("text-xl font-semibold mt-2")
            ui.label("Gestion de la base").classes("text-gray-600 mt-2")
        
        with ui.card().classes("flex-1 p-6 text-center"):
            ui.icon("inventory_2", size="48px").classes("text-orange-600")
            ui.label("Stock").classes("text-xl font-semibold mt-2")
            ui.label("Suivi en temps réel").classes("text-gray-600 mt-2")

if __name__ == "__main__":
    ui.run()
```

### Cas 3 : Application de Réservation

**Schéma Prisma :**

```prisma
model Service {
  id          Int          @id @default(autoincrement())
  name        String
  description String
  duration    Int          // en minutes
  price       Float
  bookings    Booking[]
}

model Booking {
  id        Int      @id @default(autoincrement())
  date      DateTime
  status    String   @default("pending")
  serviceId Int
  service   Service  @relation(fields: [serviceId], references: [id])
  userId    Int
  createdAt DateTime @default(now())
}
```

**Interface de réservation :**

```python
from nicegui import ui
from datetime import datetime, timedelta

@ui.page("/booking")
async def booking_page():
    ui.label("Réserver un Service").classes("text-2xl font-bold mb-6")
    
    # Sélection du service
    ui.label("1. Choisissez un service").classes("text-xl font-semibold mb-4")
    
    services = [
        {"id": 1, "name": "Consultation", "duration": 30, "price": 50},
        {"id": 2, "name": "Suivi", "duration": 15, "price": 30},
        {"id": 3, "name": "Bilan complet", "duration": 60, "price": 100}
    ]
    
    selected_service = {"value": None}
    
    with ui.row().classes("w-full gap-4"):
        for service in services:
            with ui.card().classes("flex-1 cursor-pointer").on('click', lambda s=service: setattr(selected_service, 'value', s)):
                ui.label(service["name"]).classes("text-lg font-semibold")
                ui.label(f"{service['duration']} min - {service['price']}€").classes("text-gray-600")
    
    # Sélection de la date
    ui.label("2. Choisissez une date").classes("text-xl font-semibold mt-6 mb-4")
    
    date_picker = ui.date().classes("w-full")
    
    # Confirmation
    ui.label("3. Confirmez").classes("text-xl font-semibold mt-6 mb-4")
    
    async def confirm_booking():
        if not selected_service.value:
            ui.notify("Veuillez sélectionner un service", type="warning")
            return
        
        ui.notify(f"Réservation confirmée pour {selected_service.value['name']}", type="positive")
        # Ici, enregistrer dans la base de données
    
    ui.button(
        "Confirmer la réservation",
        on_click=confirm_booking,
        color="primary"
    ).classes("mt-4")

if __name__ == "__main__":
    ui.run()
```

---

## ❓ FAQ et Dépannage

### Questions Fréquentes

**Q: Comment changer la base de données pour PostgreSQL ?**

R: Modifiez `db/schema.prisma` :

```prisma
datasource db {
  provider = "postgresql"
  url      = env("DATABASE_URL")
}
```

Puis créez un fichier `.env` :

```
DATABASE_URL="postgresql://user:password@localhost:5432/mydb"
```

**Q: Comment ajouter une page de connexion ?**

R: Créez une nouvelle route dans `main.py` :

```python
@ui.page("/login")
def login():
    with ui.form():
        ui.input("Email", key="email")
        ui.input("Mot de passe", key="password", password=True)
        ui.button("Se connecter", on_click=authenticate)
```

**Q: Comment personnaliser le thème ?**

R: Modifiez `static/css/main.css` :

```css
:root {
    --primary-color: #3b82f6;
    --secondary-color: #8b5cf6;
    --background: #f3f4f6;
}
```

### Problèmes Courants

**Erreur: "Prisma not found"**

```bash
# Solution
pip install prisma
prisma generate
```

**Erreur: "Module not found" dans l'exécutable**

```bash
# Ajoutez le module dans build.json
{
  "hidden_imports": ["nom_du_module"]
}

# Puis rebuild
visionit build onefile
```

**Erreur: "Ressources non trouvées dans l'exécutable"**

Vérifiez que `add_data` dans `build.json` inclut tous les dossiers nécessaires :

```json
{
  "add_data": [
    ["templates", "templates"],
    ["static", "static"]
  ]
}
```

**L'application est lente au démarrage**

- Utilisez `onedir` au lieu de `onefile`
- Excluez les modules inutiles dans `exclude_modules`
- Optimisez les imports dans `main.py`

---

## 📞 Support

- **Documentation:** Ce fichier
- **Issues GitHub:** https://github.com/visionit/visionit/issues
- **Email:** contact@visionit.com

---

**VisionIT Framework** - Développé avec ❤️ par Vision IT
