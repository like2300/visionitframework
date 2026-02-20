#!/usr/bin/env python3
"""Test rapide - Vérifie que la fenêtre s'ouvre sur Mac."""

import sys
import threading
import time

print("="*60)
print("🧪 TEST FENÊTRE MAC - VisionIT Framework")
print("="*60)

# Test 1: pywebview
print("\n1️⃣ Test pywebview...")
try:
    import webview
    print("   ✅ pywebview installé")
except Exception as e:
    print(f"   ❌ pywebview ERROR: {e}")
    print("   Solution: pip install pywebview")
    sys.exit(1)

# Test 2: nicegui
print("\n2️⃣ Test nicegui...")
try:
    from nicegui import ui
    print("   ✅ nicegui installé")
except Exception as e:
    print(f"   ❌ nicegui ERROR: {e}")
    print("   Solution: pip install nicegui")
    sys.exit(1)

# Test 3: Création fenêtre
print("\n3️⃣ Test création fenêtre...")

def start_server():
    from nicegui import ui
    ui.run(host='127.0.0.1', port=8080, reload=False, show=False)

try:
    # Start server
    server = threading.Thread(target=start_server, daemon=True)
    server.start()
    time.sleep(2)
    
    # Create window
    window = webview.create_window(
        title="✅ TEST VISIONIT - Mac",
        url="http://127.0.0.1:8080",
        width=800,
        height=600,
    )
    
    print("   ✅ Fenêtre créée avec succès !")
    print("\n" + "="*60)
    print("🎉 TEST RÉUSSI !")
    print("="*60)
    print("\nLa fenêtre devrait s'ouvrir sur votre Mac.")
    print("Si vous voyez cette fenêtre, tout fonctionne !\n")
    
    # Simple page for test
    from nicegui import ui
    
    @ui.page("/")
    def test_page():
        ui.label("✅ TEST RÉUSSI !").classes("text-h4 text-green-600")
        ui.label("La fenêtre Mac fonctionne avec VisionIT").classes("text-body1")
        ui.button("🎉 Cliquer", on_click=lambda: ui.notify("Ça marche !"))
    
    webview.start()
    
except Exception as e:
    print(f"   ❌ ERROR: {e}")
    print("\n" + "="*60)
    print("❌ TEST ÉCHOUÉ")
    print("="*60)
    
    print("\nSolutions possibles :")
    print("1. Réinstaller pywebview: pip install --upgrade pywebview")
    print("2. Vérifier macOS: System Preferences → Security → Allow")
    print("3. Tester en mode navigateur: python -m http.server 8080")
    
    sys.exit(1)
