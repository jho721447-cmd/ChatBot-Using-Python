import pyautogui
import time
import pyperclip
from openai import OpenAI

def is_last_message_from_sender(chat_log , sender_name1 = "Papa" , sender_name2 = "_mk_pvt_21" , sender_name3 = "Juvy Ann Magcarang"):
    messages1 = chat_log.strip().split("2025] ")[-1]
    messages2 = chat_log.strip().split("You sent")[-1]
    messages3 = chat_log.strip().split("You sent")[-1]
    
    print(messages1)
    
    if sender_name1 in messages1:  # This is for whatsapp
        return True
    elif sender_name2 in messages2: # This is for instagram
        return True
    elif sender_name3 in messages3: # This is also for instagram
        return True
    
    return False

client = OpenAI(api_key = "YOUR_API_KEY")

# Step 1: Click on the chrome icon at coordinates. (1296 , 1053)
pyautogui.click(1296,1053)
time.sleep(1) # Wait for 1 second to ensure the click is registered.

while True:
    # Step 2: Drag the mouse from (695 , 229) to (1859,908) to select the text.
    pyautogui.moveTo(744 , 294)
    pyautogui.dragTo(1038,960 , duration=1.0 , button="left") # drag for one second.

    # Step 3: Copy the selected text to the clipboard.
    pyautogui.hotkey("ctrl","c")
    time.sleep(5) # Wait for 5 second to ensure copy command is completed.
    pyautogui.click(686,619)

    # Step 4: Retrieve the text from clipboard and store in a variable
    chat_history = pyperclip.paste()

    # Print the chat_history
    print(chat_history)

    if(is_last_message_from_sender(chat_history)):
        completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a person named Cadet Paras Kamboj who speaks English and Hindi . You are from India and you are a good boy who always give respect. You analyze chat history and respond in very short (in 1 to 9 words) like Cadet Paras Kamboj and with sweet and good behaviour always , respect others. Output should be the next chat response as Cadet Paras kamboj but give only reply in short dont write name and date in response."},
                
            {"role": "user","content": chat_history}
        ]
        )
        response =  completion.choices[0].message.content

        pyperclip.copy(response)

        # Step5 : Click at coordinates (1157,953)
        pyautogui.click(1157,953)
        time.sleep(1) # Wait for one second to ensure that the click is registered.

        # Step 6: Paste the text
        pyautogui.hotkey("ctrl","v")
        time.sleep(1) 

        # step 7: Press Enter
        pyautogui.press("enter")


