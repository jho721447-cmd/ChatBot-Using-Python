import os
import time
from instagrapi import Client

# Aapka Instagram account details (Cloud server isi se chalega)
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
        # Group chat ki current settings check karna
        thread_info = cl.direct_thread_info(TARGET_THREAD_ID)
        current_theme = thread_info.get('theme_id')
        
        # Agar kisi ne theme badli toh yeh usko waapis theek karega
        if current_theme != DESIRED_THEME_ID:
            print("Theme badal gayi! Waapis lock kar raha hoon...")
            cl.direct_thread_set_theme(TARGET_THREAD_ID, DESIRED_THEME_ID)
            print("Theme successfully waapis wahi set ho gayi!")
            
    except Exception as e:
        print(f"Error aaya: {e}")
        
    # Har 2 second mein group ko monitor karega
    time.sleep(2)
  
