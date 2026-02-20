"""demo_window - macOS Compatible Desktop Application.

Lance une VRAIE fenêtre desktop sur Mac avec pywebview direct.
"""

import threading
import time
import webview
from nicegui import ui

# === CONFIGURATION ===
WINDOW_TITLE = "🖥️ Démo VisionIT - Fenêtre Mac"
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 700
PORT = 8080


@ui.page("/")
def main_page():
    """Page principale."""
    
    ui.colors(primary='#2563eb', secondary='#64748b', accent='#8b5cf6')
    
    # En-tête
    with ui.header().classes('w-full bg-blue-600 text-white'):
        with ui.row().classes('w-full items-center px-4 py-2'):
            ui.icon("desktop_windows", size="32px")
            ui.label("🎉 Application Desktop VisionIT").classes("text-xl font-bold ml-2")
            ui.label("✅ FENÊTRE MAC FONCTIONNELLE").classes("text-sm ml-4 opacity-90")
    
    # Contenu
    with ui.column().classes('w-full p-6 gap-6'):
        
        # Message de succès
        with ui.card().classes('w-full p-6 bg-green-50 border-l-4 border-green-500'):
            ui.label("✅ LA FENÊTRE S'AFFICHE SUR VOTRE MAC !").classes("text-2xl font-bold text-green-700")
            ui.label("Votre framework VisionIT fonctionne parfaitement sur macOS.").classes("text-gray-700 mt-2")
        
        # Infos
        with ui.card().classes('w-full p-6'):
            ui.label("📋 Informations").classes("text-xl font-semibold mb-4")
            
            with ui.grid().classes('grid-cols-3 gap-4'):
                with ui.card().classes('p-4 bg-blue-50'):
                    ui.label("Application").classes("text-gray-600 text-sm")
                    ui.label("demo_window").classes("text-lg font-bold text-blue-600")
                
                with ui.card().classes('p-4 bg-green-50'):
                    ui.label("Auteur").classes("text-gray-600 text-sm")
                    ui.label("Vision IT").classes("text-lg font-bold text-green-600")
                
                with ui.card().classes('p-4 bg-purple-50'):
                    ui.label("Version").classes("text-gray-600 text-sm")
                    ui.label("0.1.0").classes("text-lg font-bold text-purple-600")
        
        # Boutons
        with ui.card().classes('w-full p-6'):
            ui.label("🎮 Test des Boutons").classes("text-xl font-semibold mb-4")
            
            with ui.row().classes('gap-4 flex-wrap'):
                ui.button("👍 Primaire", color="primary") \
                  .on('click', lambda: ui.notify("✅ Bouton cliqué !", color="positive"))
                
                ui.button("✅ Succès", color="positive") \
                  .on('click', lambda: ui.notify("🎉 Réussi !", color="positive"))
                
                ui.button("⚠️ Attention", color="warning") \
                  .on('click', lambda: ui.notify("⚠️ Attention !", color="warning"))
                
                ui.button("❌ Erreur", color="negative") \
                  .on('click', lambda: ui.notify("❌ Erreur !", color="negative"))
        
        # Notification géante
        def show_big_notification():
            ui.notify(
                "🎊 BRAVO ! La fenêtre Mac fonctionne !\n"
                "pywebview + NiceGUI = ❤️",
                color="positive",
                position="center",
                timeout=5000,
                multi_line=True
            )
        
        with ui.card().classes('w-full p-8 text-center'):
            ui.label("🚀 Test Final").classes("text-2xl font-bold mb-4")
            ui.button(
                "🎉 CLIQUEZ-MOI !",
                on_click=show_big_notification,
                color="primary"
            ).classes('text-xl px-12 py-6')
    
    # Footer
    with ui.footer().classes('w-full bg-gray-100'):
        with ui.row().classes('w-full justify-between px-4 py-2'):
            ui.label("© 2024 VisionIT Framework - macOS").classes('text-gray-600 text-sm')
            ui.label("✅ Fenêtre Desktop Fonctionnelle").classes('text-green-600 font-bold text-sm')


def start_nicegui_server():
    """Démarre le serveur NiceGUI en arrière-plan."""
    ui.run(
        host='127.0.0.1',
        port=PORT,
        reload=False,
        show=False,  # Ne pas ouvrir le navigateur
        uvicorn_logging_level='error'
    )


def create_mac_window():
    """Crée une vraie fenêtre Mac avec pywebview."""
    
    print("\n" + "="*60)
    print("🍎 LANCEMENT DE L'APPLICATION MAC")
    print("="*60)
    print(f"📝 Titre: {WINDOW_TITLE}")
    print(f"📐 Taille: {WINDOW_WIDTH}x{WINDOW_HEIGHT}")
    print(f"🌐 Port: {PORT}")
    print(f"🖥️  Mode: pywebview natif macOS")
    print("="*60)
    print("\n⏳ Ouverture de la fenêtre Mac...\n")
    
    # Démarrer le serveur NiceGUI dans un thread
    server_thread = threading.Thread(target=start_nicegui_server, daemon=True)
    server_thread.start()
    
    # Attendre que le serveur démarre
    time.sleep(2)
    
    # Créer la fenêtre avec pywebview (spécial Mac)
    url = f"http://127.0.0.1:{PORT}"
    
    print(f"🌐 Chargement de: {url}")
    
    window = webview.create_window(
        title=WINDOW_TITLE,
        url=url,
        width=WINDOW_WIDTH,
        height=WINDOW_HEIGHT,
        resizable=True,
        fullscreen=False,
        min_size=(400, 300),
        text_select=True,
    )
    
    print("✅ Fenêtre créée ! Démarrage de webview...\n")
    
    # Démarrer la fenêtre (bloque jusqu'à fermeture)
    webview.start()


if __name__ == "__main__":
    # Méthode directe avec pywebview (fonctionne sur Mac)
    create_mac_window()
