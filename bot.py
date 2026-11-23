import os
import time
from instagrapi import Client

# Aapka Instagram account details (Cloud server isi se chalega)
USERNAME = "AAPKA_USERNAME_YAHAN_LIKHO"
PASSWORD = "AAPKA_PASSWORD_YAHAN_LIKHO"
TARGET_THREAD_ID = "AAPKI_GC_ID_YAHAN_LIKHO"
DESIRED_THEME_ID = "AAPKI_FAVOURITE_THEME_ID"

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
  
