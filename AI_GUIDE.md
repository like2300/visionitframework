# 🤖 VisionIT Framework - Guide pour Intelligences Artificielles

**Version:** 0.1.0  
**Objectif:** Permettre aux IA de générer du code compatible VisionIT en respectant les normes du framework

---

## 📋 Règles Fondamentales

Lorsque vous générez du code pour un projet VisionIT, respectez TOUJOURS ces règles :

### 1. Structure de Projet Standard

```
mon_projet/
├── db/
│   └── schema.prisma          # Schéma de base de données Prisma
├── templates/
│   ├── index.html             # Templates HTML
│   └── components/            # Composants réutilisables
│       ├── navbar.html
│       ├── footer.html
│       ├── card.html
│       └── ...
├── static/
│   ├── css/
│   │   └── main.css           # CSS personnalisé
│   ├── js/
│   │   └── main.js            # JavaScript personnalisé
│   └── icons/                 # Icônes de l'application
├── actions/
│   └── *.py                   # Logique métier NiceGUI
├── info.json                  # Métadonnées (NE PAS MODIFIER)
├── package.txt                # Dépendances Python
├── build.json                 # Configuration PyInstaller
└── main.py                    # Point d'entrée
```

### 2. Conventions de Code

#### Python (main.py et actions/)

```python
# ✅ BIEN - Structure recommandée
from nicegui import ui, app
from pathlib import Path
import json
from prisma import Prisma

# Import des actions
from actions.user_manager import UserManager
from actions.product_manager import ProductManager

# Initialisation DB
db = Prisma()

@app.get("/startup")
async def startup():
    await db.connect()

@app.get("/shutdown")
async def shutdown():
    await db.disconnect()

# Routes
@ui.page("/")
async def index():
    """Page d'accueil."""
    ui.label("Bienvenue").classes("text-h4")

@ui.page("/about")
async def about():
    """Page à propos."""
    ui.label("À propos").classes("text-h4")

if __name__ == "__main__":
    ui.run(
        title="Mon Application",
        host="0.0.0.0",
        port=8080,
        reload=False
    )
```

```python
# ❌ MAL - À éviter
import nicegui  # Import incorrect
# Pas de structure, code en vrac
```

#### Actions (Logique Métier)

```python
# ✅ BIEN - actions/user_manager.py
"""Gestion des utilisateurs."""

from prisma import Prisma
from typing import Optional, List, Dict


class UserManager:
    """Service de gestion des utilisateurs."""
    
    def __init__(self, db: Prisma):
        self.db = db
    
    async def get_user(self, user_id: int) -> Optional[Dict]:
        """Récupérer un utilisateur par ID."""
        user = await self.db.user.find_unique(where={'id': user_id})
        return user.dict() if user else None
    
    async def create_user(self, email: str, name: str) -> Dict:
        """Créer un nouvel utilisateur."""
        user = await self.db.user.create(
            data={'email': email, 'name': name}
        )
        return user.dict()
    
    async def delete_user(self, user_id: int) -> bool:
        """Supprimer un utilisateur."""
        await self.db.user.delete(where={'id': user_id})
        return True


# Instance globale
user_manager = None

def get_user_manager(db: Prisma) -> UserManager:
    """Obtenir ou créer le UserManager."""
    global user_manager
    if user_manager is None:
        user_manager = UserManager(db)
    return user_manager
```

### 3. Templates HTML

#### Structure de Base

```html
<!-- ✅ BIEN - templates/index.html -->
{% extends 'base.html' %}

{% block title %}Accueil - Mon Application{% endblock %}

{% block content %}
<div class="container mx-auto px-4 py-8">
    <h1 class="text-3xl font-bold mb-6">Bienvenue</h1>
    
    <!-- Utiliser les composants VisionIT -->
    {% include 'components/card.html' with {
        card_title: 'Fonctionnalité',
        card_description: 'Description'
    } %}
</div>
{% endblock %}

{% block extra_scripts %}
<script>
    console.log('Page chargée');
</script>
{% endblock %}
```

#### Utilisation des Composants

```html
<!-- ✅ BIEN - Utiliser les composants existants -->
{% include 'components/navbar.html' with {
    app_name: 'MonApp',
    nav_items: [
        {'label': 'Accueil', 'url': '/'},
        {'label': 'Services', 'url': '/services'},
        {'label': 'Contact', 'url': '/contact'}
    ]
} %}

{% for product in products %}
    {% include 'components/card.html' with {
        card_title: product.name,
        card_description: product.description,
        card_link: '/product/' ~ product.id
    } %}
{% endfor %}

{% include 'components/footer.html' with {
    year: '2024',
    copyright_owner: 'Mon Entreprise'
} %}
```

```html
<!-- ❌ MAL - Recréer ce qui existe déjà -->
<nav>
    <!-- Code HTML brut au lieu d'utiliser navbar.html -->
</nav>
```

### 4. Base de Données (Prisma)

#### Schéma Standard

```prisma
// ✅ BIEN - db/schema.prisma
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

#### Requêtes Prisma

```python
# ✅ BIEN - Utilisation de Prisma
from prisma import Prisma

db = Prisma()
await db.connect()

# CREATE
user = await db.user.create(
    data={'email': 'user@example.com', 'name': 'John'}
)

# READ
users = await db.user.find_many()
user = await db.user.find_unique(where={'id': 1})
filtered = await db.user.find_many(where={'role': 'admin'})

# UPDATE
await db.user.update(
    where={'id': 1},
    data={'name': 'Jane'}
)

# DELETE
await db.user.delete(where={'id': 1})

await db.disconnect()
```

### 5. Composants - Quand et Comment les Utiliser

#### Composants Disponibles

| Composant | Usage | Variables Principales |
|-----------|-------|----------------------|
| `navbar` | Navigation | `app_name`, `nav_items` |
| `footer` | Pied de page | `footer_links`, `copyright_owner` |
| `card` | Carte de contenu | `card_title`, `card_description`, `card_link` |
| `button` | Bouton | `button_text`, `button_style`, `button_onclick` |
| `input` | Champ formulaire | `input_id`, `label`, `input_type` |
| `alert` | Notification | `alert_type`, `message`, `alert_title` |
| `modal` | Fenêtre modale | `modal_id`, `modal_title`, `modal_content` |
| `hero` | Section hero | `hero_title`, `hero_subtitle`, `hero_cta_text` |
| `feature` | Fonctionnalité | `feature_icon`, `feature_title` |
| `testimonial` | Témoignage | `testimonial_text`, `author_name` |

#### Créer un Nouveau Composant

```html
<!-- ✅ BIEN - templates/components/sidebar.html -->
<!-- sidebar - Composant de barre latérale -->

<aside class="w-64 bg-gray-800 text-white min-h-screen {{ sidebar_class|default('') }}">
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

<!-- 
Usage:
{% include 'components/sidebar.html' with {
    sidebar_title: 'Navigation',
    sidebar_items: [
        {'label': 'Dashboard', 'url': '/dashboard', 'active': true}
    ]
} %}
-->
```

### 6. Fichiers de Configuration

#### build.json

```json
{
  "app_name": "MonApplication",
  "main_module": "main",
  "icon": "static/icons/icon_256.png",
  "onefile": true,
  "windowed": false,
  "hidden_imports": [
    "nicegui",
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

#### package.txt

```
nicegui>=1.4.0
prisma>=0.11.0
pywebview>=4.4.0
uvicorn>=0.24.0
```

### 7. NiceGUI - Bonnes Pratiques

#### Pages et Routes

```python
# ✅ BIEN
@ui.page("/")
async def index():
    """Page d'accueil."""
    ui.label("Bienvenue").classes("text-h4")

@ui.page("/user/{user_id:int}")
async def user_profile(user_id: int):
    """Page de profil utilisateur."""
    user = await get_user(user_id)
    if user:
        ui.label(f"Profil de {user['name']}")
    else:
        ui.label("Utilisateur non trouvé").classes("text-red-500")

@ui.page("/protected")
async def protected_page():
    """Page protégée par authentification."""
    if not is_authenticated():
        ui.navigate.to("/login")
        return
    
    ui.label("Contenu protégé")
```

#### Gestion des Formulaires

```python
# ✅ BIEN
@ui.page("/contact")
async def contact_form():
    ui.label("Contactez-nous").classes("text-h4")
    
    name_input = ui.input("Nom").classes("w-full")
    email_input = ui.input("Email").classes("w-full")
    message_input = ui.textarea("Message").classes("w-full")
    
    async def submit():
        # Validation
        if not name_input.value or not email_input.value:
            ui.notify("Tous les champs sont requis", type="warning")
            return
        
        # Traitement
        await save_contact(
            name=name_input.value,
            email=email_input.value,
            message=message_input.value
        )
        
        ui.notify("Message envoyé !", type="positive")
        ui.navigate.to("/")
    
    ui.button("Envoyer", on_click=submit).classes("mt-4")
```

#### Notifications

```python
# ✅ BIEN - Utiliser ui.notify
ui.notify("Opération réussie", type="positive", position="top-right")
ui.notify("Erreur survenue", type="negative", position="top-center")
ui.notify("Information", type="info", position="bottom-right")
```

### 8. Gestion des Erreurs

```python
# ✅ BIEN
from nicegui import ui

@ui.page("/data")
async def load_data():
    try:
        data = await fetch_data()
        ui.label(f"Données chargées: {len(data)}")
    except Exception as e:
        ui.notify(f"Erreur: {str(e)}", type="negative")
        ui.label("Impossible de charger les données").classes("text-red-500")
```

### 9. Classes CSS Tailwind

Utilisez TOUJOURS les classes Tailwind via `.classes()` :

```python
# ✅ BIEN
ui.label("Titre").classes("text-2xl font-bold text-blue-600")
ui.button("Valider").classes("px-4 py-2 bg-blue-600 text-white rounded hover:bg-blue-700")
ui.card().classes("w-full max-w-md p-6 shadow-lg")

# ❌ MAL
ui.label("Titre", style="font-size: 24px; color: blue;")
```

### 10. Structure des Fichiers Static

```
static/
├── css/
│   └── main.css           # CSS global
├── js/
│   └── main.js            # JavaScript global
└── icons/
    ├── icon_16.png
    ├── icon_256.png
    └── icon_512.png
```

**main.css :**

```css
/* Styles globaux */
body {
    font-family: 'Inter', sans-serif;
}

.text-gradient {
    background: linear-gradient(to right, #3b82f6, #8b5cf6);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
```

**main.js :**

```javascript
document.addEventListener('DOMContentLoaded', function() {
    console.log('Application initialisée');
});

function notify(message, type = 'info') {
    // Fonction utilitaire de notification
}
```

---

## 🎯 Checklist de Génération de Code

Avant de fournir du code, vérifiez :

- [ ] La structure de fichiers respecte-t-elle les normes VisionIT ?
- [ ] Les composants HTML existants sont-ils utilisés ?
- [ ] Le code Python est-il dans `actions/` si c'est de la logique métier ?
- [ ] Les classes Tailwind sont-elles utilisées via `.classes()` ?
- [ ] La base de données utilise-t-elle Prisma correctement ?
- [ ] Les templates étendent-ils `base.html` ?
- [ ] Les notifications utilisent-elles `ui.notify()` ?
- [ ] Le code est-il compatible Python 3.9+ ?
- [ ] Les imports sont-ils corrects (nicegui, prisma) ?
- [ ] La gestion d'erreurs est-elle présente ?

---

## 📝 Exemples de Réponses IA

### Exemple 1 : Créer une Page de Contact

**Question :** "Crée une page de contact avec formulaire"

**Réponse :**

```python
# main.py
from nicegui import ui

@ui.page("/contact")
async def contact_page():
    """Page de contact avec formulaire."""
    
    # Utiliser le template de base
    ui.label("Contactez-nous").classes("text-3xl font-bold mb-6")
    
    with ui.card().classes("w-full max-w-md p-6"):
        # Champs du formulaire
        name = ui.input("Nom complet").classes("w-full")
        email = ui.input("Email").classes("w-full")
        message = ui.textarea("Message").classes("w-full").props('rows=5')
        
        async def submit_contact():
            """Soumettre le formulaire."""
            # Validation
            if not name.value or not email.value or not message.value:
                ui.notify("Tous les champs sont requis", type="warning")
                return
            
            # Ici, sauvegarder dans la base de données
            # await db.contact.create(...)
            
            ui.notify("Message envoyé avec succès !", type="positive")
            name.value = ""
            email.value = ""
            message.value = ""
        
        # Bouton de soumission
        ui.button(
            "Envoyer le message",
            on_click=submit_contact,
            color="primary"
        ).classes("w-full mt-4")
```

### Exemple 2 : Créer un Modèle de Données

**Question :** "Ajoute un modèle Product avec categories"

**Réponse :**

```prisma
// db/schema.prisma
// Ajoutez ces modèles au schéma existant

model Category {
  id        Int      @id @default(autoincrement())
  name      String   @unique
  products  Product[]
  createdAt DateTime @default(now())
}

model Product {
  id          Int       @id @default(autoincrement())
  name        String
  description String?
  price       Float
  stock       Int       @default(0)
  categoryId  Int
  category    Category  @relation(fields: [categoryId], references: [id])
  createdAt   DateTime  @default(now())
  updatedAt   DateTime  @updatedAt
}
```

```python
# actions/product_manager.py
"""Gestion des produits."""

from prisma import Prisma
from typing import List, Dict, Optional


class ProductManager:
    """Service de gestion des produits."""
    
    def __init__(self, db: Prisma):
        self.db = db
    
    async def get_all_products(self) -> List[Dict]:
        """Récupérer tous les produits."""
        products = await self.db.product.find_many(include={'category': True})
        return [p.dict() for p in products]
    
    async def get_product(self, product_id: int) -> Optional[Dict]:
        """Récupérer un produit par ID."""
        product = await self.db.product.find_unique(
            where={'id': product_id},
            include={'category': True}
        )
        return product.dict() if product else None
    
    async def create_product(
        self,
        name: str,
        price: float,
        category_id: int,
        description: str = None,
        stock: int = 0
    ) -> Dict:
        """Créer un nouveau produit."""
        product = await self.db.product.create(
            data={
                'name': name,
                'price': price,
                'categoryId': category_id,
                'description': description,
                'stock': stock
            }
        )
        return product.dict()
    
    async def update_product(self, product_id: int, **kwargs) -> Dict:
        """Mettre à jour un produit."""
        product = await self.db.product.update(
            where={'id': product_id},
            data=kwargs
        )
        return product.dict()
    
    async def delete_product(self, product_id: int) -> bool:
        """Supprimer un produit."""
        await self.db.product.delete(where={'id': product_id})
        return True
```

### Exemple 3 : Créer un Dashboard

**Question :** "Crée un dashboard avec des statistiques"

**Réponse :**

```python
# main.py
from nicegui import ui
from datetime import datetime, timedelta

@ui.page("/dashboard")
async def dashboard():
    """Tableau de bord avec statistiques."""
    
    # En-tête
    ui.label("Tableau de Bord").classes("text-3xl font-bold mb-8")
    ui.label(f"Dernière mise à jour: {datetime.now().strftime('%d/%m/%Y %H:%M')}")\
      .classes("text-gray-600 mb-6")
    
    # Cartes de statistiques
    with ui.row().classes("w-full gap-4 mb-8"):
        # Carte 1 - Utilisateurs
        with ui.card().classes("flex-1 p-6"):
            ui.icon("people", size="32px").classes("text-blue-600 mb-2")
            ui.label("Utilisateurs").classes("text-gray-600")
            ui.label("1,234").classes("text-3xl font-bold text-blue-600")
            ui.label("+12% ce mois").classes("text-sm text-green-500")
        
        # Carte 2 - Ventes
        with ui.card().classes("flex-1 p-6"):
            ui.icon("shopping_cart", size="32px").classes("text-green-600 mb-2")
            ui.label("Ventes").classes("text-gray-600")
            ui.label("45,678 €").classes("text-3xl font-bold text-green-600")
            ui.label("+8% ce mois").classes("text-sm text-green-500")
        
        # Carte 3 - Commandes
        with ui.card().classes("flex-1 p-6"):
            ui.icon("receipt", size="32px").classes("text-purple-600 mb-2")
            ui.label("Commandes").classes("text-gray-600")
            ui.label("328").classes("text-3xl font-bold text-purple-600")
            ui.label("+15% ce mois").classes("text-sm text-green-500")
    
    # Section principale
    with ui.row().classes("w-full gap-4"):
        # Tableau des dernières commandes
        with ui.card().classes("flex-2"):
            ui.label("Dernières Commandes").classes("text-xl font-semibold mb-4")
            
            # Ici, ajouter un tableau avec les données
            # Exemple statique :
            columns = [
                {'name': 'id', 'label': 'ID', 'field': 'id'},
                {'name': 'customer', 'label': 'Client', 'field': 'customer'},
                {'name': 'date', 'label': 'Date', 'field': 'date'},
                {'name': 'total', 'label': 'Total', 'field': 'total'}
            ]
            
            rows = [
                {'id': 1, 'customer': 'Jean Dupont', 'date': '2024-01-15', 'total': '120 €'},
                {'id': 2, 'customer': 'Marie Martin', 'date': '2024-01-14', 'total': '85 €'},
                {'id': 3, 'customer': 'Pierre Durand', 'date': '2024-01-13', 'total': '210 €'}
            ]
            
            ui.table(columns=columns, rows=rows).classes("w-full")
        
        # Activités récentes
        with ui.card().classes("flex-1"):
            ui.label("Activités Récentes").classes("text-xl font-semibold mb-4")
            
            activities = [
                "Nouvelle commande #328",
                "Inscription: Sophie Bernard",
                "Paiement reçu - 120€",
                "Produit ajouté: iPhone 15"
            ]
            
            for activity in activities:
                ui.label(activity).classes("text-gray-700 py-1 border-b")
```

---

## 🔧 Commandes CLI à Connaître

Lorsque vous guidez l'utilisateur, utilisez ces commandes :

```bash
# Création de projet
visionit new mon_projet
visionit new mon_projet --no-interactive

# Base de données
visionit db sync
visionit db generate

# Build
visionit build deps
visionit build onefile
visionit build onedir
visionit build clean

# Composants
visionit component list
visionit component create navbar
visionit component new custom_component

# Installation
visionit install
```

---

## 📚 Ressources

- **Documentation complète:** `DOCUMENTATION.md`
- **README:** `README.md`
- **Composants:** `templates/components/`
- **Exemples:** Voir les cas pratiques dans `DOCUMENTATION.md`

---

## ⚠️ Erreurs à Éviter

1. ❌ Ne PAS modifier `info.json` manuellement
2. ❌ Ne PAS utiliser de CSS inline, utiliser Tailwind
3. ❌ Ne PAS recréer des composants qui existent déjà
4. ❌ Ne PAS oublier les `await` pour les appels async
5. ❌ Ne PAS oublier de fermer la connexion DB
6. ❌ Ne PAS mettre de données sensibles dans le code
7. ❌ Ne PAS utiliser `reload=True` pour les exécutables

---

**Objectif :** Générer du code propre, maintenable et compatible avec l'écosystème VisionIT.
