"""Tests for VisionIT CLI."""

import os
import json
import shutil
import tempfile
from pathlib import Path

import pytest
from typer.testing import CliRunner

from visionit.cli import app

runner = CliRunner()


@pytest.fixture
def temp_dir():
    """Create a temporary directory for tests."""
    directory = tempfile.mkdtemp()
    original_dir = os.getcwd()
    os.chdir(directory)
    yield directory
    os.chdir(original_dir)
    shutil.rmtree(directory)


def test_version_command():
    """Test the version command."""
    result = runner.invoke(app, ["version"])
    assert result.exit_code == 0
    assert "VisionIT Framework" in result.stdout
    assert "0.1.0" in result.stdout


def test_new_project_interactive(temp_dir):
    """Test creating a new project in non-interactive mode."""
    project_name = "test_app"
    
    result = runner.invoke(
        app,
        ["new", project_name, "--no-interactive"],
        input=""
    )
    
    assert result.exit_code == 0
    
    # Check project directory was created
    project_path = Path(temp_dir) / project_name
    assert project_path.exists()
    
    # Check all expected files and folders exist
    expected_files = [
        "info.json",
        "package.txt",
        "build.json",
        "main.py",
        ".gitignore",
        "README.md",
        "db/schema.prisma",
        "templates",
        "static/css",
        "static/js",
        "actions",
    ]
    
    for file_path in expected_files:
        full_path = project_path / file_path
        assert full_path.exists(), f"Missing: {file_path}"


def test_new_project_info_json(temp_dir):
    """Test that info.json is correctly generated."""
    project_name = "test_app"
    
    result = runner.invoke(
        app,
        ["new", project_name, "--no-interactive"],
        input=""
    )
    
    assert result.exit_code == 0
    
    project_path = Path(temp_dir) / project_name
    info_file = project_path / "info.json"
    
    with open(info_file, "r", encoding="utf-8") as f:
        info = json.load(f)
    
    assert info["project_name"] == project_name
    assert "author" in info
    assert "version" in info
    assert info["orm"] == "Prisma"
    assert info["database"] == "SQLite"


def test_new_project_package_txt(temp_dir):
    """Test that package.txt is correctly generated."""
    project_name = "test_app"
    
    result = runner.invoke(
        app,
        ["new", project_name, "--no-interactive"],
        input=""
    )
    
    assert result.exit_code == 0
    
    project_path = Path(temp_dir) / project_name
    package_file = project_path / "package.txt"
    
    with open(package_file, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Check for expected dependencies
    assert "nicegui" in content
    assert "prisma" in content


def test_new_project_prisma_schema(temp_dir):
    """Test that schema.prisma is correctly generated."""
    project_name = "test_app"
    
    result = runner.invoke(
        app,
        ["new", project_name, "--no-interactive"],
        input=""
    )
    
    assert result.exit_code == 0
    
    project_path = Path(temp_dir) / project_name
    schema_file = project_path / "db" / "schema.prisma"
    
    with open(schema_file, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Check for Prisma schema elements
    assert "datasource db" in content
    assert "provider = \"sqlite\"" in content
    assert "generator client" in content
    assert "model User" in content


def test_new_project_main_py(temp_dir):
    """Test that main.py is correctly generated."""
    project_name = "test_app"
    
    result = runner.invoke(
        app,
        ["new", project_name, "--no-interactive"],
        input=""
    )
    
    assert result.exit_code == 0
    
    project_path = Path(temp_dir) / project_name
    main_file = project_path / "main.py"
    
    with open(main_file, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Check for NiceGUI elements
    assert "from nicegui import ui" in content
    assert "@ui.page" in content
    assert "ui.run" in content


def test_new_project_existing_directory(temp_dir):
    """Test error handling when project directory already exists."""
    project_name = "test_app"
    project_path = Path(temp_dir) / project_name
    project_path.mkdir()
    
    result = runner.invoke(
        app,
        ["new", project_name, "--no-interactive"],
        input=""
    )
    
    assert result.exit_code != 0
    assert "already exists" in result.stdout


def test_db_sync_no_schema(temp_dir):
    """Test db sync command when schema doesn't exist."""
    result = runner.invoke(
        app,
        ["db", "sync", "--path", temp_dir],
        catch_exceptions=False,
    )
    
    assert result.exit_code != 0
    # Check for error message in output
    assert "schema.prisma" in result.output


def test_install_no_package_file(temp_dir):
    """Test install command when package.txt doesn't exist."""
    result = runner.invoke(
        app,
        ["install", "--path", temp_dir],
    )

    assert result.exit_code != 0
    assert "package.txt not found" in result.stdout


def test_new_project_build_json(temp_dir):
    """Test that build.json is correctly generated."""
    project_name = "test_app"
    
    result = runner.invoke(
        app,
        ["new", project_name, "--no-interactive"],
        input=""
    )
    
    assert result.exit_code == 0
    
    project_path = Path(temp_dir) / project_name
    build_file = project_path / "build.json"
    
    with open(build_file, "r", encoding="utf-8") as f:
        config = json.load(f)
    
    assert config["app_name"] == project_name
    assert config["main_module"] == "main"
    assert "hidden_imports" in config
    assert "add_data" in config


def test_build_config_command(temp_dir):
    """Test build config command."""
    project_name = "test_app"
    
    # Create project first
    runner.invoke(app, ["new", project_name, "--no-interactive"])
    
    project_path = Path(temp_dir) / project_name
    
    result = runner.invoke(
        app,
        ["build", "config", "--path", str(project_path)],
    )
    
    assert result.exit_code == 0
    assert "app_name" in result.output
    assert project_name in result.output


def test_component_list_command():
    """Test component list command."""
    result = runner.invoke(app, ["component", "list"])
    
    assert result.exit_code == 0
    assert "navbar" in result.output
    assert "footer" in result.output
    assert "card" in result.output


def test_component_create_command(temp_dir):
    """Test component create command."""
    project_name = "test_app"
    
    # Create project first
    runner.invoke(app, ["new", project_name, "--no-interactive"])
    
    project_path = Path(temp_dir) / project_name
    
    result = runner.invoke(
        app,
        ["component", "create", "hero", "--path", str(project_path)],
    )
    
    assert result.exit_code == 0
    assert "hero.html" in result.output
    
    # Check component file was created
    component_file = project_path / "templates" / "components" / "hero.html"
    assert component_file.exists()


def test_new_project_components(temp_dir):
    """Test that components are generated with new project."""
    project_name = "test_app"
    
    result = runner.invoke(
        app,
        ["new", project_name, "--no-interactive"],
        input=""
    )
    
    assert result.exit_code == 0
    
    project_path = Path(temp_dir) / project_name
    components_dir = project_path / "templates" / "components"
    
    assert components_dir.exists()
    
    # Check for some expected components
    expected_components = ["navbar.html", "footer.html", "card.html"]
    for component in expected_components:
        assert (components_dir / component).exists(), f"Missing: {component}"


def test_new_project_icons(temp_dir):
    """Test that icons directory is generated with new project."""
    project_name = "test_app"
    
    result = runner.invoke(
        app,
        ["new", project_name, "--no-interactive"],
        input=""
    )
    
    assert result.exit_code == 0
    
    project_path = Path(temp_dir) / project_name
    icons_dir = project_path / "static" / "icons"
    
    assert icons_dir.exists()
    assert (icons_dir / "README.md").exists()
