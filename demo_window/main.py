"""demo_window - CORRECTED Desktop Application.

Application desktop avec fenêtre native qui s'affiche VRAIMENT !
"""

from nicegui import ui, app
from pathlib import Path
import json

# === CONFIGURATION ===
WINDOW_TITLE = "🖥️ Démo VisionIT - Fenêtre Desktop"
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 700
PORT = 8080


@ui.page("/")
def main_page():
    """Page principale."""
    
    # Style global
    ui.colors(primary='#2563eb', secondary='#64748b', accent='#8b5cf6')
    
    # === EN-TÊTE ===
    with ui.header().classes('w-full bg-blue-600 text-white'):
        with ui.row().classes('w-full items-center px-4 py-2'):
            ui.icon("desktop_windows", size="32px")
            ui.label("🎉 Application Desktop VisionIT").classes("text-xl font-bold ml-2")
            ui.label("✅ FENÊTRE NATIVE FONCTIONNELLE").classes("text-sm ml-4 opacity-90")
    
    # === CONTENU ===
    with ui.column().classes('w-full p-6 gap-6'):
        
        # Message de succès
        with ui.card().classes('w-full p-6 bg-green-50 border-l-4 border-green-500'):
            ui.label("✅ LA FENÊTRE S'AFFICHE CORRECTEMENT !").classes("text-2xl font-bold text-green-700")
            ui.label("Votre framework VisionIT fonctionne parfaitement.").classes("text-gray-700 mt-2")
        
        # Informations
        with ui.card().classes('w-full p-6'):
            ui.label("📋 Informations").classes("text-xl font-semibold mb-4")
            
            try:
                info_file = Path(__file__).parent / "info.json"
                if info_file.exists():
                    with open(info_file, "r", encoding="utf-8") as f:
                        info = json.load(f)
                    
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
            except Exception as e:
                ui.label(f"Erreur lecture info: {e}").classes("text-red-500")
        
        # Boutons de test
        with ui.card().classes('w-full p-6'):
            ui.label("🎮 Test des Boutons").classes("text-xl font-semibold mb-4")
            
            with ui.row().classes('gap-4 flex-wrap'):
                ui.button("👍 Primaire", color="primary") \
                  .on('click', lambda: ui.notify("✅ Bouton primaire cliqué !", color="positive"))
                
                ui.button("✅ Succès", color="positive") \
                  .on('click', lambda: ui.notify("🎉 Action réussie !", color="positive", position="top"))
                
                ui.button("⚠️ Attention", color="warning") \
                  .on('click', lambda: ui.notify("⚠️ Attention !", color="warning", position="top"))
                
                ui.button("❌ Erreur", color="negative") \
                  .on('click', lambda: ui.notify("❌ Erreur !", color="negative", position="top"))
                
                ui.button("ℹ️ Info", color="info") \
                  .on('click', lambda: ui.notify("ℹ️ Information", color="info", position="top"))
        
        # Inputs
        with ui.card().classes('w-full p-6'):
            ui.label("📝 Champs de Saisie").classes("text-xl font-semibold mb-4")
            
            with ui.row().classes('w-full gap-4'):
                ui.input("Nom", placeholder="Votre nom").classes('flex-1')
                ui.input("Email", placeholder="email@exemple.com").classes('flex-1')
            
            with ui.row().classes('w-full mt-4'):
                ui.textarea("Message", placeholder="Votre message...").classes('flex-1')
        
        # Slider et contrôles
        with ui.card().classes('w-full p-6'):
            ui.label("🎚️ Contrôles").classes("text-xl font-semibold mb-4")
            
            with ui.row().classes('gap-8 items-center'):
                slider = ui.slider(min=0, max=100, value=50).props('label')
                ui.label().bind_text_from(slider, 'value', lambda v: f"Valeur: {v}")
                
                ui.checkbox("Activer option")
                ui.switch("Mode sombre")
        
        # Grande notification
        def show_big_notification():
            ui.notify(
                "🎊 BRAVO ! La fenêtre desktop fonctionne parfaitement !\n"
                "Votre application VisionIT est opérationnelle.",
                color="positive",
                position="center",
                timeout=5000,
                multi_line=True
            )
        
        with ui.card().classes('w-full p-8 text-center'):
            ui.label("🚀 Test Final").classes("text-2xl font-bold mb-4")
            ui.button(
                "🎉 CLIQUEZ-MOI POUR TESTER",
                on_click=show_big_notification,
                color="primary"
            ).classes('text-xl px-12 py-6')
        
        # Features
        with ui.row().classes('w-full gap-4'):
            with ui.card().classes('flex-1 p-6 text-center'):
                ui.icon("desktop_windows", size="64px").classes("text-blue-600")
                ui.label("Fenêtre Native").classes("text-xl font-semibold mt-2")
                ui.label("pywebview").classes("text-gray-600")
            
            with ui.card().classes('flex-1 p-6 text-center'):
                ui.icon("palette", size="64px").classes("text-green-600")
                ui.label("UI Moderne").classes("text-xl font-semibold mt-2")
                ui.label("NiceGUI + Tailwind").classes("text-gray-600")
            
            with ui.card().classes('flex-1 p-6 text-center'):
                ui.icon("build", size="64px").classes("text-purple-600")
                ui.label("Exécutable").classes("text-xl font-semibold mt-2")
                ui.label("PyInstaller").classes("text-gray-600")
    
    # === PIED DE PAGE ===
    with ui.footer().classes('w-full bg-gray-100'):
        with ui.row().classes('w-full justify-between px-4 py-2'):
            ui.label("© 2024 VisionIT Framework").classes('text-gray-600 text-sm')
            ui.label("✅ Fenêtre Desktop Fonctionnelle").classes('text-green-600 font-bold text-sm')


# === POINT D'ENTRÉE ===
if __name__ == "__main__":
    print("\n" + "="*70)
    print("🚀 LANCEMENT DE L'APPLICATION DESKTOP VISIONIT")
    print("="*70)
    print(f"📝 Titre: {WINDOW_TITLE}")
    print(f"📐 Taille: {WINDOW_WIDTH}x{WINDOW_HEIGHT}")
    print(f"🌐 Port: {PORT}")
    print(f"🖥️  Mode: NATIF (fenêtre desktop avec pywebview)")
    print("="*70)
    print("\n⏳ Ouverture de la fenêtre...")
    print("Si la fenêtre ne s'ouvre pas, allez sur: http://127.0.0.1:8080\n")
    
    # Configuration pour fenêtre native
    app.native.title = WINDOW_TITLE
    app.native.width = WINDOW_WIDTH
    app.native.height = WINDOW_HEIGHT
    
    # Lancement AVEC support natif
    ui.run(
        title=WINDOW_TITLE,
        host="127.0.0.1",
        port=PORT,
        reload=False,
        show=True,  # Ouvre automatiquement
        native=True,  # Mode fenêtre desktop
        window_size=(WINDOW_WIDTH, WINDOW_HEIGHT),
        fullscreen=False,
        frameless=False,
    )
