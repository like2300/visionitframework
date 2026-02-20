"""demo_window - Application Desktop Mac avec HTML Moderne.

Affiche un fichier HTML moderne avec Tailwind CSS dans la fenêtre.
"""

import threading
import time
import webview
from pathlib import Path
from nicegui import ui

# === CONFIGURATION ===
WINDOW_TITLE = "🖥️ VisionIT - Installation HTML"
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 900
PORT = 8080


def start_server():
    """Start NiceGUI server."""
    ui.run(host='127.0.0.1', port=PORT, reload=False, show=False, uvicorn_logging_level='error')


def create_window():
    """Create Mac desktop window with HTML file."""
    
    print("\n" + "="*60)
    print("🍀 VisionIT - Fenêtre Desktop Mac")
    print("="*60)
    print(f"📝 Titre: {WINDOW_TITLE}")
    print(f"📐 Taille: {WINDOW_WIDTH}x{WINDOW_HEIGHT}")
    print(f"🌐 Port: {PORT}")
    print("="*60)
    print("\n⏳ Ouverture de la fenêtre...\n")
    
    # Start server
    server = threading.Thread(target=start_server, daemon=True)
    server.start()
    time.sleep(2)
    
    # Get HTML file path
    html_file = Path(__file__).parent / "templates" / "index.html"
    
    if not html_file.exists():
        print(f"❌ HTML file not found: {html_file}")
        return
    
    print(f"📄 Chargement: {html_file}")
    
    # Create window with HTML file
    window = webview.create_window(
        title=WINDOW_TITLE,
        url=f"file://{html_file.absolute()}",
        width=WINDOW_WIDTH,
        height=WINDOW_HEIGHT,
        resizable=True,
        min_size=(400, 300),
    )
    
    print("✅ Fenêtre ouverte avec HTML moderne !\n")
    print("🎨 Tailwind CSS chargé")
    print("✨ Animations actives")
    print("🎯 Interactivité prête\n")
    
    webview.start()


if __name__ == "__main__":
    create_window()
