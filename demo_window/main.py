"""demo_window - Application Desktop pour macOS.

Utilise pywebview directement pour une vraie fenêtre sur Mac.
"""

import threading
import time
import webview
from nicegui import ui
from pathlib import Path
import json

# === CONFIGURATION ===
WINDOW_TITLE = "🖥️ Démo VisionIT - Mac"
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 700
PORT = 8080


@ui.page("/")
def main_page():
    """Page principale."""
    
    ui.colors(primary='#2563eb', secondary='#64748b', accent='#8b5cf6')
    
    # Charger les infos
    try:
        info_file = Path(__file__).parent / "info.json"
        with open(info_file, "r", encoding="utf-8") as f:
            info = json.load(f)
    except:
        info = {'project_name': 'demo_window', 'author': 'Vision IT', 'version': '1.0.0'}
    
    # En-tête
    with ui.header().classes('w-full bg-blue-600 text-white'):
        with ui.row().classes('w-full items-center px-4 py-2'):
            ui.icon("desktop_windows", size="32px")
            ui.label(f"🎉 {info['project_name']}").classes("text-xl font-bold ml-2")
            ui.label(f"v{info['version']}").classes("text-sm ml-4 opacity-90")
    
    # Contenu
    with ui.column().classes('w-full p-6 gap-6'):
        
        # Message de succès
        with ui.card().classes('w-full p-6 bg-green-50 border-l-4 border-green-500'):
            ui.label("✅ FENÊTRE MAC FONCTIONNELLE !").classes("text-2xl font-bold text-green-700")
            ui.label("pywebview + NiceGUI fonctionnent sur votre Mac !").classes("text-gray-700 mt-2")
        
        # Infos
        with ui.card().classes('w-full p-6'):
            ui.label("📋 Informations").classes("text-xl font-semibold mb-4")
            
            with ui.grid().classes('grid-cols-3 gap-4'):
                with ui.card().classes('p-4 bg-blue-50'):
                    ui.label("Application").classes("text-gray-600 text-sm")
                    ui.label(info.get('project_name', 'N/A')).classes("text-lg font-bold text-blue-600")
                
                with ui.card().classes('p-4 bg-green-50'):
                    ui.label("Auteur").classes("text-gray-600 text-sm")
                    ui.label(info.get('author', 'N/A')).classes("text-lg font-bold text-green-600")
                
                with ui.card().classes('p-4 bg-purple-50'):
                    ui.label("Version").classes("text-gray-600 text-sm")
                    ui.label(info.get('version', '1.0.0')).classes("text-lg font-bold text-purple-600")
        
        # Boutons
        with ui.card().classes('w-full p-6'):
            ui.label("🎮 Test").classes("text-xl font-semibold mb-4")
            
            with ui.row().classes('gap-4 flex-wrap'):
                ui.button("👍 Primaire", color="primary") \
                  .on('click', lambda: ui.notify("✅ Ça marche !", color="positive"))
                ui.button("✅ Succès", color="positive") \
                  .on('click', lambda: ui.notify("🎉 Réussi !", color="positive"))
                ui.button("⚠️ Warning", color="warning") \
                  .on('click', lambda: ui.notify("⚠️ Attention !", color="warning"))
                ui.button("❌ Erreur", color="negative") \
                  .on('click', lambda: ui.notify("❌ Erreur !", color="negative"))
        
        # Inputs
        with ui.card().classes('w-full p-6'):
            ui.label("📝 Champs").classes("text-xl font-semibold mb-4")
            with ui.row().classes('w-full gap-4'):
                ui.input("Nom", placeholder="Votre nom").classes('flex-1')
                ui.input("Email", placeholder="email@mac.com").classes('flex-1')
        
        # Test final
        def show_success():
            ui.notify("🎊 BRAVO ! Mac + VisionIT = ❤️", color="positive", position="center", timeout=4000)
        
        with ui.card().classes('w-full p-8 text-center'):
            ui.label("🚀 Tout Fonctionne !").classes("text-2xl font-bold mb-4")
            ui.button("🎉 CLIQUEZ-MOI !", on_click=show_success, color="primary").classes('text-xl px-12 py-6')
    
    # Footer
    with ui.footer().classes('w-full bg-gray-100'):
        with ui.row().classes('w-full justify-between px-4 py-2'):
            ui.label("© 2024 VisionIT - macOS").classes('text-gray-600 text-sm')
            ui.label("✅ pywebview + NiceGUI").classes('text-green-600 font-bold text-sm')


def start_server():
    """Start NiceGUI server."""
    ui.run(host='127.0.0.1', port=PORT, reload=False, show=False, uvicorn_logging_level='error')


def create_window():
    """Create Mac desktop window with pywebview."""
    
    print("\n" + "="*60)
    print("🍎 VisionIT - Application Desktop Mac")
    print("="*60)
    print(f"📝 Titre: {WINDOW_TITLE}")
    print(f"📐 Taille: {WINDOW_WIDTH}x{WINDOW_HEIGHT}")
    print(f"🌐 Port: {PORT}")
    print("="*60)
    print("\n⏳ Ouverture...\n")
    
    # Start server
    server = threading.Thread(target=start_server, daemon=True)
    server.start()
    time.sleep(2)
    
    # Create window
    window = webview.create_window(
        title=WINDOW_TITLE,
        url=f"http://127.0.0.1:{PORT}",
        width=WINDOW_WIDTH,
        height=WINDOW_HEIGHT,
        resizable=True,
        min_size=(400, 300),
    )
    
    print("✅ Fenêtre ouverte !\n")
    webview.start()


if __name__ == "__main__":
    create_window()
