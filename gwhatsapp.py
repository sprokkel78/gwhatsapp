#!/usr/bin/env python3
import gi
import os
import sys

gi.require_version("Gtk", "3.0")
gi.require_version("WebKit2", "4.1")

from gi.repository import Gtk, WebKit2, GLib, Gdk

def Key_Event(obj, event):
    if event.keyval == Gdk.KEY_q and event.state & Gdk.ModifierType.CONTROL_MASK:
        Gtk.main_quit()
        sys.exit(0)

    if event.keyval == Gdk.KEY_m and event.state & Gdk.ModifierType.CONTROL_MASK:
        win.iconify()

class BrowserWindow(Gtk.Application):
    def __init__(self):
        super().__init__(application_id="com.sprokkel78.gwhatsapp")
        GLib.set_application_name("gwhatsapp")

    def do_activate(self):
        global win
        win=Gtk.ApplicationWindow(application=self, title="gwhatsapp")
        win.set_default_size(800, 600)
        win.connect("key-press-event", Key_Event)

        # Pick a directory for cache
        cache_dir = os.path.expanduser("~/.gwhatsapp/cache")
        os.makedirs(cache_dir, exist_ok=True)

        # Create WebsiteDataManager with custom directories
        data_manager = WebKit2.WebsiteDataManager(base_cache_directory=cache_dir, base_data_directory=cache_dir)

	    # Create a web context for the WebView
        context = WebKit2.WebContext.new_with_website_data_manager(data_manager)

        # Get the cookie manager
        cookie_manager = context.get_cookie_manager()
        # Store cookies persistently in a local file
        user = ""
        user = os.getlogin()
        cookie_manager.set_persistent_storage(
            "/home/" + user + "/gwhatsapp-cookies.db", WebKit2.CookiePersistentStorage.SQLITE
        )

        # Create WebView using this context
        webview = WebKit2.WebView.new_with_context(context)
        webview.load_uri("https://web.whatsapp.com")
        webview.set_zoom_level(1.5)

	    # Scrolled window (optioneel)
        scrolled = Gtk.ScrolledWindow()
        scrolled.add(webview)

        win.add(scrolled)
        win.present()
        scrolled.show()
        webview.show()

# START THE APPLICATION
def main():
    app = BrowserWindow()
    app.run(None)

if __name__ == "__main__":
    main()
