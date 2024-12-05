import google.generativeai as ai
from gtts import gTTS
import pyaudio as pd
import os

API_KEY = 'AIzaSyDGe4xSQmnWSBKhigDANxRMdjHbYuzom6Y'
ai.configure(api_key=API_KEY)

model = ai.GenerativeModel('gemini-pro')
chat = model.start_chat()


def speak_text(text):
    tts = gTTS(text=text, lang='en')
    tts.save("response.mp4")
    os.system("start response.mp4") 


while True:
    message = input("You: ") 
    if message.lower() == 'bye':
        print("Chatbot: Goodbye!")
        speak_text("Goodbye!")
        break
    response = chat.send_message(message)
    print("Chatbot:", response.text)
    speak_text(response.text)
