# VisionIT Framework

**VisionIT Framework** est un framework Python pour créer des **applications desktop modernes** avec interface graphique. Il génère des projets boilerplate avec [NiceGUI](https://nicegui.io/), [Prisma ORM](https://prisma.io/), et SQLite, permettant un développement rapide d'applications de bureau multi-plateformes.

## 🖥️ Framework pour Applications Desktop

VisionIT est spécialisé dans la création d'applications desktop avec :

- **Interface Graphique Moderne** - NiceGUI avec Tailwind CSS
- **Base de Données Intégrée** - Prisma ORM + SQLite
- **Exécutables Natifs** - PyInstaller pour Mac, Linux, Windows
- **Composants Réutilisables** - Bibliothèque de composants UI
- **CLI Puissant** - Outils de génération et build

## 📚 Documentation

- **[DOCUMENTATION.md](DOCUMENTATION.md)** - Documentation complète avec exemples et cas pratiques
- **[AI_GUIDE.md](AI_GUIDE.md)** - Guide pour les IA afin de générer du code compatible VisionIT
- **[README.md](README.md)** - Ce fichier (documentation rapide)

## Features

- ⚡ **Quick Project Setup** - Generate a complete project structure in seconds
- 🎨 **NiceGUI Integration** - Ready-to-use UI framework for Python web apps
- 🗄️ **Prisma ORM** - Type-safe database access with SQLite
- 📦 **Dependency Management** - Auto-generated package.txt for pip
- 🔧 **CLI Commands** - Built-in commands for DB sync, install, and more

## Installation

### From Source (Development)

```bash
cd visionit
pip install -e .
```

### From PyPI (Coming Soon)

```bash
pip install visionit
```

## Usage

### Create a New Project

```bash
visionit new my_app
```

This will:
1. Ask you interactive questions (author, version, ORM, database)
2. Create the project structure
3. Generate all necessary files

### Project Structure

```
my_app/
├── db/
│   └── schema.prisma      # Prisma schema configuration
├── templates/
│   └── index.html         # HTML templates
├── static/
│   ├── css/               # Compiled CSS (Tailwind, etc.)
│   └── js/                # JavaScript files
├── actions/
│   └── main_logic.py      # NiceGUI business logic
├── dev.db                 # SQLite database (auto-generated)
├── info.json              # Project metadata
├── package.txt            # pip dependencies
├── main.py                # Application entry point
└── README.md              # Project documentation
```

### CLI Commands

#### Project Commands
| Command | Description |
|---------|-------------|
| `visionit new <name>` | Create a new project |
| `visionit new <name> -i false` | Create a project with defaults (non-interactive) |
| `visionit install` | Install dependencies from package.txt |
| `visionit version` | Show framework version |

#### Database Commands
| Command | Description |
|---------|-------------|
| `visionit db sync` | Sync database with Prisma schema |
| `visionit db generate` | Generate Prisma client |

#### Build Commands (Exécutables)
| Command | Description |
|---------|-------------|
| `visionit build deps` | Install build dependencies (PyInstaller) |
| `visionit build onefile` | Build a single executable file |
| `visionit build onedir` | Build an executable with separate directory |
| `visionit build all` | Build both onefile and onedir modes |
| `visionit build spec` | Generate PyInstaller spec file |
| `visionit build config` | Show build configuration |
| `visionit build clean` | Clean build artifacts |

#### Component Commands
| Command | Description |
|---------|-------------|
| `visionit component list` | List available component templates |
| `visionit component create <name>` | Create a component from template |
| `visionit component new <name>` | Create a custom component from scratch |
| `visionit component install <name>` | Install a component to your project |

### Examples

**Create a project in interactive mode:**
```bash
visionit new my_app
```

**Create a project with defaults (non-interactive):**
```bash
visionit new my_app -i false
```

**Sync the database:**
```bash
cd my_app
visionit db sync
```

**Install dependencies:**
```bash
visionit install
```

**Install build dependencies:**
```bash
visionit build deps
```

**Build a standalone executable:**
```bash
# Build single executable file (recommended for distribution)
visionit build onefile

# Build with separate directory (better performance)
visionit build onedir

# Build both modes
visionit build all
```

**Clean build artifacts:**
```bash
visionit build clean
```

**Run the application:**
```bash
python main.py
```

## Composants HTML Réutilisables

VisionIT inclut un système de composants HTML pour accélérer le développement.

### Composants Disponibles

- **navbar** - Barre de navigation responsive
- **footer** - Pied de page avec liens
- **card** - Carte de contenu
- **button** - Bouton stylisé
- **input** - Champ de formulaire
- **alert** - Message d'alerte
- **modal** - Fenêtre modale
- **hero** - Section hero pour landing pages
- **feature** - Élément de fonctionnalité
- **testimonial** - Témoignage client

### Utilisation des Composants

**Lister les composants disponibles:**
```bash
visionit component list
```

**Ajouter un composant à votre projet:**
```bash
visionit component create navbar
visionit component create hero
```

**Créer un composant personnalisé:**
```bash
visionit component new my_custom_component
```

**Exemple d'utilisation dans un template:**
```html
{% include 'components/navbar.html' %}

<div class="container">
    {% include 'components/card.html' with {
        card_title: 'Mon Titre',
        card_description: 'Description'
    } %}
</div>

{% include 'components/footer.html' %}
```

## Icônes d'Application

Pour ajouter une icône à votre exécutable :

1. **Placez vos icônes dans** `static/icons/`
2. **Formats recommandés :**
   - PNG : 256x256px ou 512x512px
   - ICO (Windows) : multi-tailles (16, 32, 48, 256)
   - ICNS (macOS) : utiliser iconutil

3. **Mettez à jour `build.json` :**
```json
{
  "icon": "static/icons/icon_256.png"
}
```

4. **Générez le spec PyInstaller :**
```bash
visionit build spec
visionit build onefile
```

## Development

### Prérequis

- Python 3.9+
- pip

### Installation du Développement

```bash
# Cloner le repository
git clone https://github.com/visionit/visionit.git
cd visionit

# Installer en mode editable avec dépendances dev
pip install -e ".[dev]"
```

### Exécution des Tests

```bash
pytest
```

### Formatage du Code

```bash
# Formater avec Black
black visionit/

# Linter avec Ruff
ruff check visionit/
```

## Configuration

### info.json

Métadonnées du projet dans `info.json` :

```json
{
  "project_name": "my_app",
  "author": "Your Name",
  "version": "1.0.0",
  "orm": "Prisma",
  "database": "SQLite"
}
```

### package.txt

List your pip dependencies:

```
nicegui>=1.4.0
prisma>=0.11.0
pywebview>=4.4.0
uvicorn>=0.24.0
```

### schema.prisma

Define your database models:

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
  createdAt DateTime @default(now())
  updatedAt DateTime @updatedAt
}
```

## Cross-Platform Builds

### Build for Current Platform

```bash
# Install build dependencies
visionit build deps

# Build executable
visionit build onefile
```

### Build for Multiple Platforms

PyInstaller creates executables for the **current platform only**. To build for multiple platforms:

#### macOS (Intel/Apple Silicon)
```bash
# On macOS
visionit build onefile
# Output: dist/my_app (macOS executable)
```

#### Linux
```bash
# On Linux
visionit build onefile
# Output: dist/my_app (Linux executable)
```

#### Windows
```bash
# On Windows
visionit build onefile
# Output: dist/my_app.exe (Windows executable)
```

### Cross-Compilation Options

**Option 1: Use CI/CD (Recommended)**
Set up GitHub Actions or similar to build on each platform:

```yaml
# .github/workflows/build.yml
strategy:
  matrix:
    os: [ubuntu-latest, macos-latest, windows-latest]
```

**Option 2: Use Docker for Linux builds**
```bash
docker run --rm -v $(pwd):/app python:3.11 \
  bash -c "pip install visionit pyinstaller && visionit build onefile"
```

**Option 3: Virtual Machines**
- Use Parallels/VMware for running Windows/Linux on macOS
- Use WSL2 for running Linux on Windows

### Build Configuration (build.json)

```json
{
  "app_name": "my_app",
  "main_module": "main",
  "icon": "icon.ico",
  "onefile": true,
  "windowed": false,
  "hidden_imports": ["nicegui", "uvicorn"],
  "exclude_modules": ["matplotlib", "numpy"],
  "add_data": [
    ["templates", "templates"],
    ["static", "static"],
    ["db", "db"]
  ]
}
```

### Platform-Specific Notes

| Platform | Output | Notes |
|----------|--------|-------|
| macOS | `dist/my_app` | May require code signing for distribution |
| Linux | `dist/my_app` | Works on most modern distributions |
| Windows | `dist/my_app.exe` | Can add `.ico` icon |

### Troubleshooting

**Missing modules in executable:**
```bash
# Add hidden imports in build.json
"hidden_imports": ["module_name"]
```

**Missing data files:**
```bash
# Add data files in build.json
"add_data": [["source_folder", "destination_folder"]]
```

**Large executable size:**
```bash
# Use onedir mode instead of onefile
visionit build onedir
```

## Roadmap

- [ ] Add support for PostgreSQL/MySQL
- [ ] Template system for custom project templates
- [ ] Plugin architecture for extensions
- [ ] Admin panel generator
- [ ] API endpoint scaffolding
- [ ] Docker integration
- [ ] CI/CD configuration

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/my-feature`
3. Commit your changes: `git commit -am 'Add new feature'`
4. Push to the branch: `git push origin feature/my-feature`
5. Submit a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For issues, questions, or contributions, please:
- Open an issue on [GitHub](https://github.com/visionit/visionit/issues)
- Contact us at contact@visionit.com

## Credits

- [NiceGUI](https://nicegui.io/) - UI framework
- [Prisma](https://prisma.io/) - Database ORM
- [Typer](https://typer.tiangolo.com/) - CLI framework
- [Questionary](https://github.com/tmbo/questionary) - Interactive prompts

---

**VisionIT Framework** - Built with ❤️ by Vision IT
