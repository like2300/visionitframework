"""VisionIT CLI - Command Line Interface for project scaffolding."""

import os
import json
import shutil
import subprocess
from pathlib import Path
from typing import Optional

import typer
import questionary

app = typer.Typer(
    name="visionit",
    help="VisionIT Framework CLI - Rapid application scaffolding",
    add_completion=False,
)

# Create subcommand groups
db_app = typer.Typer(help="Database management commands")
app.add_typer(db_app, name="db")

build_app = typer.Typer(help="Build executable commands")
app.add_typer(build_app, name="build")

component_app = typer.Typer(help="Component generation commands")
app.add_typer(component_app, name="component")


def get_template_path() -> Path:
    """Get the path to the templates directory."""
    return Path(__file__).parent / "templates"


def create_project_structure(base_path: Path) -> None:
    """Create the basic project folder structure."""
    folders = ['db', 'templates', 'static/css', 'static/js', 'actions']
    for folder in folders:
        (base_path / folder).mkdir(parents=True, exist_ok=True)
        print(f"  ✓ Created: {folder}/")


def generate_info_json(base_path: Path, project_name: str, author: str, 
                       version: str, orm: str, db_type: str) -> None:
    """Generate info.json with project metadata."""
    info = {
        "project_name": project_name,
        "author": author,
        "version": version,
        "orm": orm,
        "database": db_type
    }
    with open(base_path / "info.json", "w", encoding="utf-8") as f:
        json.dump(info, f, indent=4)
    print("  ✓ Created: info.json")


def generate_package_txt(base_path: Path) -> None:
    """Generate package.txt with default dependencies."""
    dependencies = [
        "nicegui>=1.4.0",
        "prisma>=0.11.0",
        "pywebview>=4.4.0",
        "uvicorn>=0.24.0",
    ]
    with open(base_path / "package.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(dependencies) + "\n")
    print("  ✓ Created: package.txt")


def generate_build_config(base_path: Path, project_name: str) -> None:
    """Generate build configuration file for PyInstaller."""
    config = {
        "app_name": project_name,
        "main_module": "main",
        "icon": None,
        "onefile": True,
        "windowed": False,
        "hidden_imports": [
            "nicegui",
            "nicegui.elements",
            "nicegui.page",
            "uvicorn",
            "webview",
        ],
        "exclude_modules": [
            "matplotlib",
            "numpy",
            "pandas",
            "scipy",
        ],
        "add_data": [
            ("templates", "templates"),
            ("static", "static"),
            ("db", "db"),
        ],
    }
    import json
    with open(base_path / "build.json", "w", encoding="utf-8") as f:
        json.dump(config, f, indent=4)
    print("  ✓ Created: build.json")


def generate_icon_placeholder(base_path: Path) -> None:
    """Create icon placeholder directory and instructions."""
    icons_dir = base_path / "static" / "icons"
    icons_dir.mkdir(parents=True, exist_ok=True)
    
    # Create README for icons
    readme_content = """# Icons Directory

Place your app icons here for building executables.

## Recommended Icon Sizes

- `icon_16.png` - 16x16px (favicon small)
- `icon_32.png` - 32x32px (favicon)
- `icon_128.png` - 128x128px (macOS)
- `icon_256.png` - 256x256px (macOS, Windows)
- `icon_512.png` - 512x512px (high DPI)
- `icon_1024.png` - 1024x1024px (app store)

## For Windows (.ico)
Create a multi-size .ico file containing:
16x16, 32x32, 48x48, 256x256 pixels

## For macOS (.icns)
Use iconutil to create .icns from iconset:
```bash
mkdir icon.iconset
# Copy icons as icon_16x16.png, icon_32x32.png, etc.
iconutil -c icns icon.iconset
```

## Update build.json
After adding your icon, update build.json:
```json
{
  "icon": "static/icons/icon_256.png"
}
```
"""
    with open(icons_dir / "README.md", "w", encoding="utf-8") as f:
        f.write(readme_content)
    
    print("  ✓ Created: static/icons/ (placeholder)")


def generate_components(base_path: Path) -> None:
    """Copy component templates to the project."""
    framework_components = get_template_path() / "components"
    project_components = base_path / "templates" / "components"
    
    if framework_components.exists():
        project_components.mkdir(parents=True, exist_ok=True)
        
        # Copy each component template
        for component_file in framework_components.glob("*.html"):
            dest_file = project_components / component_file.name
            with open(dest_file, "w", encoding="utf-8") as f:
                f.write(component_file.read_text(encoding="utf-8"))
        
        print(f"  ✓ Created: templates/components/ ({len(list(framework_components.glob('*.html')))} components)")


def generate_prisma_schema(base_path: Path, db_type: str = "sqlite") -> None:
    """Generate Prisma schema.prisma file."""
    schema = '''datasource db {
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
'''
    schema_path = base_path / "db" / "schema.prisma"
    with open(schema_path, "w", encoding="utf-8") as f:
        f.write(schema)
    print("  ✓ Created: db/schema.prisma")


def generate_main_py(base_path: Path, project_name: str) -> None:
    """Generate the main.py entry point with NiceGUI boilerplate."""
    main_code = f'''"""{project_name} - Main Application Entry Point.

Generated by VisionIT Framework
"""

from nicegui import ui, app
from pathlib import Path
import json
import sys

# PyInstaller resource path helper
def get_resource_path(relative_path: str) -> Path:
    """Get absolute path to resource, works for dev and PyInstaller."""
    if hasattr(sys, "_MEIPASS"):
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = Path(sys._MEIPASS)
    else:
        base_path = Path(__file__).parent
    return base_path / relative_path


# Load project info
INFO_FILE = get_resource_path("info.json")
with open(INFO_FILE, "r", encoding="utf-8") as f:
    project_info = json.load(f)


@ui.page("/")
def index():
    """Main page route."""
    ui.label("Welcome to {project_name}!").classes("text-h4")
    ui.label(f"Author: {{project_info.get('author', 'N/A')}}").classes("text-body1")
    ui.label(f"Version: {{project_info.get('version', '1.0.0')}}").classes("text-body2")
    
    ui.separator()
    
    ui.label("Get Started:").classes("text-h6")
    ui.markdown("""
    - Edit `templates/index.html` for your HTML content
    - Add your NiceGUI logic in `actions/`
    - Run `visionit db sync` to initialize the database
    """)


def create_app() -> ui.app:
    """Create and configure the NiceGUI application."""
    # Add custom CSS from static folder
    static_path = get_resource_path("static") / "css"
    if static_path.exists():
        for css_file in static_path.glob("*.css"):
            ui.add_css(str(css_file))
    
    return ui


if __name__ == "__main__":
    # Run the application
    ui.run(
        title=project_info.get("project_name", "{project_name}"),
        host="0.0.0.0",
        port=8080,
        reload=False,  # Disable reload for executable
        native=False,  # Set to True for native window
    )
'''
    with open(base_path / "main.py", "w", encoding="utf-8") as f:
        f.write(main_code)
    print("  ✓ Created: main.py")


def generate_gitignore(base_path: Path) -> None:
    """Generate .gitignore file."""
    gitignore = """# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/
ENV/
*.egg-info/
dist/
build/

# Database
*.db
*.sqlite
*.sqlite3

# Prisma
prisma/schema.prisma
!db/schema.prisma

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Project specific
info.json
"""
    with open(base_path / ".gitignore", "w", encoding="utf-8") as f:
        f.write(gitignore)
    print("  ✓ Created: .gitignore")


def generate_readme(base_path: Path, project_name: str) -> None:
    """Generate README.md file."""
    readme = f"""# {project_name}

Project generated with **VisionIT Framework**.

## Setup

1. Install dependencies:
```bash
pip install -r package.txt
```

2. Initialize the database:
```bash
visionit db sync
```

3. Run the application:
```bash
python main.py
```

## Project Structure

- `actions/` - NiceGUI logic and handlers
- `templates/` - HTML templates
- `static/` - Static assets (CSS, JS)
- `db/` - Database schema (Prisma)

## Development

- Edit `main.py` to add routes and pages
- Add your business logic in `actions/`
- Use Prisma for database operations
"""
    with open(base_path / "README.md", "w", encoding="utf-8") as f:
        f.write(readme)
    print("  ✓ Created: README.md")


@app.command("new")
def new_project(
    project_name: str = typer.Argument(..., help="Name of the new project"),
    interactive: bool = typer.Option(True, "--interactive/--no-interactive", "-i/-ni", help="Run in interactive mode"),
):
    """Create a new VisionIT project."""
    typer.echo(f"\n🚀 Creating new project: {project_name}\n")
    
    base_path = Path(project_name)
    
    if base_path.exists():
        typer.echo(f"❌ Error: Directory '{project_name}' already exists!")
        raise typer.Exit(1)
    
    if interactive:
        # Interactive questions
        author = questionary.text("Nom du développeur :").ask()
        if not author:
            author = "Vision IT"
        
        version = questionary.text("Version de l'app :", default="1.0.0").ask()
        
        orm = questionary.select(
            "Choisir l'ORM :",
            choices=["Prisma"]
        ).ask()
        
        db_type = questionary.select(
            "Choisir la base de données :",
            choices=["SQLite"]
        ).ask()
    else:
        # Default values for non-interactive mode
        author = "Vision IT"
        version = "1.0.0"
        orm = "Prisma"
        db_type = "SQLite"
    
    typer.echo("\n📁 Creating project structure...\n")
    
    # Create base directory
    base_path.mkdir(parents=True, exist_ok=True)
    
    # Generate all files
    create_project_structure(base_path)
    generate_info_json(base_path, project_name, author, version, orm, db_type)
    generate_package_txt(base_path)
    generate_prisma_schema(base_path, db_type)
    generate_main_py(base_path, project_name)
    generate_gitignore(base_path)
    generate_readme(base_path, project_name)
    generate_build_config(base_path, project_name)
    generate_icon_placeholder(base_path)
    generate_components(base_path)
    
    typer.echo(f"\n✅ Project '{project_name}' created successfully!")
    typer.echo(f"\n📝 Next steps:")
    typer.echo(f"   cd {project_name}")
    typer.echo(f"   pip install -r package.txt")
    typer.echo(f"   visionit db sync")
    typer.echo(f"   python main.py")


@db_app.command("sync")
def db_sync(
    project_path: str = typer.Option(".", "--path", "-p", help="Path to the project"),
):
    """Synchronize database with Prisma schema."""
    path = Path(project_path)
    schema_path = path / "db" / "schema.prisma"
    
    if not schema_path.exists():
        typer.echo(f"❌ Error: schema.prisma not found at {schema_path}")
        raise typer.Exit(1)
    
    typer.echo("🔄 Syncing database with Prisma...\n")
    
    try:
        # Run Prisma db push
        result = subprocess.run(
            ["prisma", "db", "push", "--schema", str(schema_path)],
            cwd=path,
            capture_output=True,
            text=True,
        )
        
        if result.returncode == 0:
            typer.echo("✅ Database synced successfully!")
            if result.stdout:
                typer.echo(result.stdout)
        else:
            typer.echo(f"❌ Error syncing database:")
            typer.echo(result.stderr)
            raise typer.Exit(1)
    except FileNotFoundError:
        typer.echo("❌ Error: Prisma CLI not found. Install it with:")
        typer.echo("   pip install prisma")
        typer.echo("   prisma generate")
        raise typer.Exit(1)


@db_app.command("generate")
def db_generate(
    project_path: str = typer.Option(".", "--path", "-p", help="Path to the project"),
):
    """Generate Prisma client."""
    path = Path(project_path)
    schema_path = path / "db" / "schema.prisma"
    
    if not schema_path.exists():
        typer.echo(f"❌ Error: schema.prisma not found at {schema_path}")
        raise typer.Exit(1)
    
    typer.echo("🔄 Generating Prisma client...\n")
    
    try:
        result = subprocess.run(
            ["prisma", "generate", "--schema", str(schema_path)],
            cwd=path,
            capture_output=True,
            text=True,
        )
        
        if result.returncode == 0:
            typer.echo("✅ Prisma client generated successfully!")
            if result.stdout:
                typer.echo(result.stdout)
        else:
            typer.echo(f"❌ Error generating Prisma client:")
            typer.echo(result.stderr)
            raise typer.Exit(1)
    except FileNotFoundError:
        typer.echo("❌ Error: Prisma CLI not found. Install it with:")
        typer.echo("   pip install prisma")
        raise typer.Exit(1)


@app.command("install")
def install_deps(
    project_path: str = typer.Option(".", "--path", "-p", help="Path to the project"),
    upgrade: bool = typer.Option(False, "--upgrade/-U", help="Upgrade dependencies"),
):
    """Install project dependencies from package.txt."""
    path = Path(project_path)
    package_file = path / "package.txt"
    
    if not package_file.exists():
        typer.echo(f"❌ Error: package.txt not found at {package_file}")
        raise typer.Exit(1)
    
    typer.echo("📦 Installing dependencies...\n")
    
    cmd = ["pip", "install", "-r", str(package_file)]
    if upgrade:
        cmd.insert(2, "--upgrade")
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode == 0:
            typer.echo("✅ Dependencies installed successfully!")
            if result.stdout:
                typer.echo(result.stdout)
        else:
            typer.echo(f"❌ Error installing dependencies:")
            typer.echo(result.stderr)
            raise typer.Exit(1)
    except Exception as e:
        typer.echo(f"❌ Error: {e}")
        raise typer.Exit(1)


@app.command("version")
def show_version():
    """Show VisionIT Framework version."""
    from visionit import __version__
    typer.echo(f"VisionIT Framework v{__version__}")


def load_build_config(project_path: Path) -> dict:
    """Load build configuration from build.json."""
    config_file = project_path / "build.json"
    if not config_file.exists():
        return None
    import json
    with open(config_file, "r", encoding="utf-8") as f:
        return json.load(f)


def generate_pyinstaller_spec(project_path: Path, config: dict) -> Path:
    """Generate PyInstaller spec file."""
    app_name = config.get("app_name", "app")
    main_module = config.get("main_module", "main")
    hidden_imports = config.get("hidden_imports", [])
    exclude_modules = config.get("exclude_modules", [])
    add_data = config.get("add_data", [])
    windowed = config.get("windowed", False)
    onefile = config.get("onefile", False)
    icon = config.get("icon")

    # Format data for PyInstaller
    data_tuples = []
    for src, dst in add_data:
        data_tuples.append(f'("{src}", "{dst}")')

    # Format hidden imports
    hidden_imports_str = ", ".join(f'"{imp}"' for imp in hidden_imports)

    # Format excluded modules
    exclude_str = ", ".join(f'"{mod}"' for mod in exclude_modules)

    # Handle icon
    icon_str = f'"{icon}"' if icon else "None"

    spec_content = f'''# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ["{main_module}.py"],
    pathex=[],
    binaries=[],
    data=[{", ".join(data_tuples)}],
    hiddenimports=[{hidden_imports_str}],
    hookspath=[],
    hooksconfig={{}},
    runtime_hooks=[],
    excludes=[{exclude_str}],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name="{app_name}",
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon={icon_str},
)
'''
    
    spec_path = project_path / f"{app_name}.spec"
    with open(spec_path, "w", encoding="utf-8") as f:
        f.write(spec_content)
    
    return spec_path


@build_app.command("config")
def build_config(
    project_path: str = typer.Option(".", "--path", "-p", help="Path to the project"),
):
    """Show current build configuration."""
    path = Path(project_path)
    config = load_build_config(path)
    
    if not config:
        typer.echo("❌ Error: build.json not found. Run 'visionit new' or create build.json")
        raise typer.Exit(1)
    
    typer.echo("📋 Build Configuration:\n")
    import json
    typer.echo(json.dumps(config, indent=2))


@build_app.command("spec")
def build_spec(
    project_path: str = typer.Option(".", "--path", "-p", help="Path to the project"),
):
    """Generate PyInstaller spec file."""
    path = Path(project_path)
    config = load_build_config(path)
    
    if not config:
        typer.echo("❌ Error: build.json not found. Run 'visionit new' or create build.json")
        raise typer.Exit(1)
    
    typer.echo("📝 Generating PyInstaller spec file...\n")
    spec_path = generate_pyinstaller_spec(path, config)
    typer.echo(f"✅ Spec file created: {spec_path}")


@build_app.command("onefile")
def build_onefile(
    project_path: str = typer.Option(".", "--path", "-p", help="Path to the project"),
    clean: bool = typer.Option(False, "--clean", "-c", help="Clean build artifacts"),
):
    """Build a single executable file (onefile mode)."""
    path = Path(project_path)
    
    # Update config for onefile mode
    config = load_build_config(path)
    if config:
        config["onefile"] = True
        import json
        with open(path / "build.json", "w", encoding="utf-8") as f:
            json.dump(config, f, indent=4)
    
    typer.echo("🔨 Building executable (onefile mode)...\n")
    
    try:
        cmd = ["pyinstaller", "--onefile"]
        
        if config:
            # Add hidden imports
            for imp in config.get("hidden_imports", []):
                cmd.extend(["--hidden-import", imp])
            
            # Add data files
            for src, dst in config.get("add_data", []):
                cmd.extend(["--add-data", f"{src}{os.pathsep}{dst}"])
        
        cmd.append(str(path / "main.py"))
        
        result = subprocess.run(cmd, cwd=path, capture_output=True, text=True)
        
        if result.returncode == 0:
            typer.echo(f"✅ Executable built successfully!")
            typer.echo(f"📦 Output: {path / 'dist' / config.get('app_name', 'app')}")
            if result.stdout:
                typer.echo(result.stdout)
        else:
            typer.echo(f"❌ Error building executable:")
            typer.echo(result.stderr)
            raise typer.Exit(1)
    except FileNotFoundError:
        typer.echo("❌ Error: PyInstaller not found. Install it with:")
        typer.echo("   pip install pyinstaller")
        raise typer.Exit(1)


@build_app.command("onedir")
def build_onedir(
    project_path: str = typer.Option(".", "--path", "-p", help="Path to the project"),
    clean: bool = typer.Option(False, "--clean", "-c", help="Clean build artifacts"),
):
    """Build an executable with separate directory (onedir mode)."""
    path = Path(project_path)
    
    # Update config for onedir mode
    config = load_build_config(path)
    if config:
        config["onefile"] = False
        import json
        with open(path / "build.json", "w", encoding="utf-8") as f:
            json.dump(config, f, indent=4)
    
    typer.echo("🔨 Building executable (onedir mode)...\n")
    
    try:
        cmd = ["pyinstaller", "--onedir"]
        
        if config:
            # Add hidden imports
            for imp in config.get("hidden_imports", []):
                cmd.extend(["--hidden-import", imp])
            
            # Add data files
            for src, dst in config.get("add_data", []):
                cmd.extend(["--add-data", f"{src}{os.pathsep}{dst}"])
        
        cmd.append(str(path / "main.py"))
        
        result = subprocess.run(cmd, cwd=path, capture_output=True, text=True)
        
        if result.returncode == 0:
            app_name = config.get("app_name", "app")
            typer.echo(f"✅ Executable built successfully!")
            typer.echo(f"📦 Output: {path / 'dist' / app_name}/")
            if result.stdout:
                typer.echo(result.stdout)
        else:
            typer.echo(f"❌ Error building executable:")
            typer.echo(result.stderr)
            raise typer.Exit(1)
    except FileNotFoundError:
        typer.echo("❌ Error: PyInstaller not found. Install it with:")
        typer.echo("   pip install pyinstaller")
        raise typer.Exit(1)


@build_app.command("all")
def build_all(
    project_path: str = typer.Option(".", "--path", "-p", help="Path to the project"),
    clean: bool = typer.Option(False, "--clean", "-c", help="Clean build artifacts"),
):
    """Build executables for current platform with all modes."""
    path = Path(project_path)
    
    typer.echo("🔨 Building executables (onefile + onedir)...\n")
    
    # Build onefile
    build_onefile(project_path, clean)
    typer.echo("\n" + "="*50 + "\n")
    
    # Build onedir
    build_onedir(project_path, clean)
    
    typer.echo("\n✅ All builds completed!")


@build_app.command("clean")
def build_clean(
    project_path: str = typer.Option(".", "--path", "-p", help="Path to the project"),
):
    """Clean build artifacts (build, dist folders)."""
    path = Path(project_path)
    
    typer.echo("🧹 Cleaning build artifacts...\n")
    
    folders_to_remove = ["build", "dist", "__pycache__"]
    for folder in folders_to_remove:
        folder_path = path / folder
        if folder_path.exists():
            shutil.rmtree(folder_path)
            typer.echo(f"  ✓ Removed: {folder}/")
    
    # Remove spec files
    for spec_file in path.glob("*.spec"):
        spec_file.unlink()
        typer.echo(f"  ✓ Removed: {spec_file.name}")
    
    typer.echo("\n✅ Clean completed!")


@build_app.command("deps")
def build_deps(
    project_path: str = typer.Option(".", "--path", "-p", help="Path to the project"),
):
    """Install build dependencies (PyInstaller)."""
    typer.echo("📦 Installing build dependencies...\n")
    
    try:
        cmd = ["pip", "install", "pyinstaller>=6.0.0"]
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode == 0:
            typer.echo("✅ Build dependencies installed!")
            typer.echo("   - PyInstaller")
            if result.stdout:
                typer.echo(result.stdout)
        else:
            typer.echo(f"❌ Error installing dependencies:")
            typer.echo(result.stderr)
            raise typer.Exit(1)
    except Exception as e:
        typer.echo(f"❌ Error: {e}")
        raise typer.Exit(1)


# Component templates
COMPONENT_TEMPLATES = {
    "navbar": """<!-- Navigation Bar -->
<nav class="bg-white shadow-lg">
    <div class="container mx-auto px-4">
        <div class="flex justify-between items-center py-4">
            <a href="/" class="text-xl font-bold text-gray-800">{{ app_name }}</a>
            <div class="hidden md:flex space-x-6">
                {% for item in nav_items %}
                <a href="{{ item.url }}" class="text-gray-600 hover:text-blue-600">{{ item.label }}</a>
                {% endfor %}
            </div>
        </div>
    </div>
</nav>
""",
    "footer": """<!-- Footer -->
<footer class="bg-gray-800 text-white py-8 mt-16">
    <div class="container mx-auto px-4 text-center">
        <p>&copy; {{ year }} {{ copyright_owner }}. Tous droits réservés.</p>
    </div>
</footer>
""",
    "card": """<!-- Card Component -->
<div class="bg-white rounded-lg shadow-md p-6 {{ card_class }}">
    <h3 class="text-xl font-semibold text-gray-800 mb-2">{{ card_title }}</h3>
    <p class="text-gray-600 mb-4">{{ card_description }}</p>
    <a href="{{ card_link }}" class="text-blue-600 hover:text-blue-800">En savoir plus →</a>
</div>
""",
    "button": """<!-- Button Component -->
<button class="px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition-colors">
    {{ button_text }}
</button>
""",
    "input": """<!-- Input Component -->
<div class="mb-4">
    <label for="{{ input_id }}" class="block text-sm font-medium text-gray-700 mb-2">{{ label }}</label>
    <input type="{{ input_type|default('text') }}" 
           id="{{ input_id }}" 
           name="{{ input_name }}"
           class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500">
</div>
""",
    "alert": """<!-- Alert Component -->
<div class="border-l-4 rounded-md p-4 bg-{{ alert_type }}-50 border-{{ alert_type }}-200 text-{{ alert_type }}-800">
    <p class="font-medium">{{ alert_title }}</p>
    <p class="text-sm">{{ message }}</p>
</div>
""",
    "modal": """<!-- Modal Component -->
<div id="{{ modal_id }}" class="hidden fixed inset-0 z-50 overflow-y-auto">
    <div class="flex items-center justify-center min-h-screen px-4">
        <div class="fixed inset-0 bg-gray-900 bg-opacity-75"></div>
        <div class="bg-white rounded-lg shadow-xl p-6 z-10 max-w-md w-full">
            <h3 class="text-lg font-medium mb-4">{{ modal_title }}</h3>
            <p class="text-gray-600 mb-4">{{ modal_content }}</p>
            <div class="flex justify-end space-x-2">
                <button onclick="document.getElementById('{{ modal_id }}').classList.add('hidden')"
                        class="px-4 py-2 text-gray-600 hover:text-gray-800">Fermer</button>
                <button class="px-4 py-2 bg-blue-600 text-white rounded-lg">{{ modal_confirm }}</button>
            </div>
        </div>
    </div>
</div>
""",
    "hero": """<!-- Hero Section -->
<section class="bg-gradient-to-r from-blue-600 to-purple-600 text-white py-20">
    <div class="container mx-auto px-4 text-center">
        <h1 class="text-5xl font-bold mb-4">{{ hero_title }}</h1>
        <p class="text-xl mb-8">{{ hero_subtitle }}</p>
        <a href="{{ hero_cta_link }}" class="inline-block px-8 py-3 bg-white text-blue-600 rounded-lg font-semibold hover:bg-gray-100">
            {{ hero_cta_text }}
        </a>
    </div>
</section>
""",
    "feature": """<!-- Feature Item -->
<div class="text-center p-6">
    <div class="w-16 h-16 mx-auto mb-4 bg-blue-100 rounded-full flex items-center justify-center">
        <svg class="w-8 h-8 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            {{ feature_icon }}
        </svg>
    </div>
    <h3 class="text-xl font-semibold mb-2">{{ feature_title }}</h3>
    <p class="text-gray-600">{{ feature_description }}</p>
</div>
""",
    "testimonial": """<!-- Testimonial -->
<div class="bg-gray-50 rounded-lg p-6">
    <p class="text-gray-700 italic mb-4">"{{ testimonial_text }}"</p>
    <div class="flex items-center">
        <img src="{{ author_avatar }}" alt="{{ author_name }}" class="w-12 h-12 rounded-full mr-4">
        <div>
            <p class="font-semibold">{{ author_name }}</p>
            <p class="text-sm text-gray-500">{{ author_title }}</p>
        </div>
    </div>
</div>
"""
}


@component_app.command("list")
def component_list():
    """List available component templates."""
    typer.echo("📦 Available Component Templates:\n")
    
    for name, description in [
        ("navbar", "Navigation bar with responsive menu"),
        ("footer", "Footer with links and copyright"),
        ("card", "Content card with image and link"),
        ("button", "Styled button with variants"),
        ("input", "Form input with label and validation"),
        ("alert", "Alert/notification message"),
        ("modal", "Modal dialog/popup"),
        ("hero", "Hero section for landing pages"),
        ("feature", "Feature item for product sections"),
        ("testimonial", "Customer testimonial card"),
    ]:
        typer.echo(f"  • {name:15} - {description}")
    
    typer.echo("\n💡 Usage: visionit component create <name> [output_path]")


@component_app.command("create")
def component_create(
    component_name: str = typer.Argument(..., help="Name of the component to create"),
    output_path: str = typer.Argument("templates/components", help="Output path for the component"),
    project_path: str = typer.Option(".", "--path", "-p", help="Path to the project"),
):
    """Create a new HTML component from template."""
    path = Path(project_path)
    output_dir = path / output_path
    
    # Check if component template exists
    if component_name not in COMPONENT_TEMPLATES:
        typer.echo(f"❌ Component '{component_name}' not found.")
        typer.echo(f"   Available components: {', '.join(COMPONENT_TEMPLATES.keys())}")
        raise typer.Exit(1)
    
    # Create output directory if it doesn't exist
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Write component file
    component_file = output_dir / f"{component_name}.html"
    template_content = COMPONENT_TEMPLATES[component_name]
    
    with open(component_file, "w", encoding="utf-8") as f:
        f.write(template_content)
    
    typer.echo(f"✅ Component '{component_name}' created: {component_file}")


@component_app.command("new")
def component_new(
    component_name: str = typer.Argument(..., help="Name of the new custom component"),
    project_path: str = typer.Option(".", "--path", "-p", help="Path to the project"),
):
    """Create a new custom component from scratch."""
    path = Path(project_path)
    output_dir = path / "templates" / "components"
    
    # Create output directory if it doesn't exist
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Create component file
    component_file = output_dir / f"{component_name}.html"
    
    template_content = f"""<!-- {component_name} Component -->
<!-- Created with VisionIT Framework -->

<div class="{{{{ {component_name}_class|default('') }}}}">
    <h3 class="{{{{ {component_name}_title_class|default('text-xl font-semibold') }}}}"">
        {{{{ {component_name}_title }}}}
    </h3>
    <p class="{{{{ {component_name}_content_class|default('text-gray-600') }}}}"">
        {{{{ {component_name}_content }}}}
    </p>
</div>

<!-- Usage example:
{{% include 'components/{component_name}.html' with {{
    {component_name}_title: 'My Component',
    {component_name}_content: 'Component content here'
}} %}}
-->
"""
    
    with open(component_file, "w", encoding="utf-8") as f:
        f.write(template_content)
    
    typer.echo(f"✅ Custom component '{component_name}' created: {component_file}")
    typer.echo(f"\n📝 Edit the component at: {component_file}")


@component_app.command("install")
def component_install(
    component_name: str = typer.Argument(..., help="Name of the component to install"),
    project_path: str = typer.Option(".", "--path", "-p", help="Path to the project"),
):
    """Install a component from the VisionIT library to your project."""
    path = Path(project_path)
    output_dir = path / "templates" / "components"
    
    # Create output directory if it doesn't exist
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Check if component template exists
    if component_name not in COMPONENT_TEMPLATES:
        typer.echo(f"❌ Component '{component_name}' not found.")
        typer.echo(f"   Available: {', '.join(COMPONENT_TEMPLATES.keys())}")
        raise typer.Exit(1)
    
    # Copy component from framework templates
    component_file = output_dir / f"{component_name}.html"
    template_content = COMPONENT_TEMPLATES[component_name]
    
    with open(component_file, "w", encoding="utf-8") as f:
        f.write(template_content)
    
    typer.echo(f"✅ Component '{component_name}' installed to: {component_file}")


def main():
    """Main entry point for the CLI."""
    app()


if __name__ == "__main__":
    main()
