"""VisionIT Framework - Corrected Desktop Window Support.

This module fixes the native window display issue.
"""

import sys
import webview
import threading
import time
from pathlib import Path

# Check if pywebview is available
try:
    import webview
    WEBVIEW_AVAILABLE = True
except ImportError:
    WEBVIEW_AVAILABLE = False
    print("⚠️  Warning: pywebview not installed. Run: pip install pywebview")


def create_desktop_window(url: str, title: str, width: int, height: int):
    """Create a native desktop window using pywebview."""
    
    if not WEBVIEW_AVAILABLE:
        print("❌ pywebview not available. Opening in browser instead.")
        import webbrowser
        webbrowser.open(url)
        return
    
    print(f"\n🖥️  Creating desktop window...")
    print(f"   Title: {title}")
    print(f"   Size: {width}x{height}")
    print(f"   URL: {url}")
    
    # Create the window
    window = webview.create_window(
        title=title,
        url=url,
        width=width,
        height=height,
        resizable=True,
        fullscreen=False,
        min_size=(400, 300),
    )
    
    print("✅ Window created. Starting webview...\n")
    
    # Start the webview
    webview.start()


def run_desktop_app(app_func, title: str, width: int = 1000, height: int = 800):
    """Run a NiceGUI app in a desktop window."""
    
    from nicegui import ui
    
    # Start NiceGUI server in a thread
    def start_server():
        ui.run(
            host='127.0.0.1',
            port=8080,
            reload=False,
            show=False,  # Don't open browser automatically
            uvicorn_logging_level='error'
        )
    
    # Start server thread
    server_thread = threading.Thread(target=start_server, daemon=True)
    server_thread.start()
    
    # Wait for server to start
    print("⏳ Starting NiceGUI server...")
    time.sleep(2)
    
    # Create desktop window
    url = "http://127.0.0.1:8080"
    create_desktop_window(url, title, width, height)


# Example usage
if __name__ == "__main__":
    from nicegui import ui
    
    @ui.page("/")
    def index():
        ui.label("Hello Desktop!").classes("text-h4")
        ui.button("Click me", on_click=lambda: ui.notify("It works!"))
    
    run_desktop_app(index, "Test Window", 800, 600)
