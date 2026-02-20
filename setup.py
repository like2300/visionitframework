"""Setup configuration for VisionIT Framework."""

from setuptools import setup, find_packages
from pathlib import Path

# Read README for long description
readme_path = Path(__file__).parent / "README.md"
long_description = ""
if readme_path.exists():
    long_description = readme_path.read_text(encoding="utf-8")

setup(
    name="visionit",
    version="0.1.0",
    author="Vision IT",
    author_email="contact@visionit.com",
    description="VisionIT Framework - Rapid application scaffolding for Python 3.9+",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/visionit/visionit",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.9",
    install_requires=[
        "typer>=0.9.0",
        "questionary>=2.0.0",
        "click>=8.0.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "black>=23.0.0",
            "ruff>=0.1.0",
        ],
        "build": [
            "pyinstaller>=6.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "visionit=visionit.cli:main",
        ],
    },
    include_package_data=True,
    package_data={
        "visionit": ["templates/*"],
    },
    keywords="scaffold boilerplate nicegui prisma rapid-development",
)
