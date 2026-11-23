import os
import time
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer
from instagrapi import Client

# Render port handler (Isse port error theek ho jayega)
def run_server():
    server = HTTPServer(('0.0.0.0', int(os.environ.get("PORT", 10000))), BaseHTTPRequestHandler)
    server.serve_forever()
threading.Thread(target=run_server, daemon=True).start()

# Aapka Instagram account details
USERNAME = "macedonalxeander"
PASSWORD = "Userdiezade8200680213"
TARGET_THREAD_ID = "12345"
DESIRED_THEME_ID = "default"

cl = Client()

try:
    print("Instagram login ho raha hai...")
    cl.login(USERNAME, PASSWORD)
    print("Login successful!")
except Exception as e:
    print(f"Login fail ho gaya: {e}")

while True:
    try:
        thread_info = cl.direct_thread_info(TARGET_THREAD_ID)
        current_theme = thread_info.get('theme_id')
        
        if current_theme != DESIRED_THEME_ID:
            print("Theme badal gayi! Waapis lock kar raha hoon...")
            cl.direct_thread_set_theme(TARGET_THREAD_ID, DESIRED_THEME_ID)
            print("Theme successfully waapis wahi set ho gayi!")
            
    except Exception as e:
        print(f"Error aaya: {e}")
        
    time.sleep(2)
    
