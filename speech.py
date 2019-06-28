import speech_recognition as sr
import gtts
from gtts import gTTS
import os

r=sr.Recognizer()
with sr.Microphone() as source:
    print("say something:")
    audio=r.listen(source)
try:
    print("system predicts:",r.reconize_google(audio))
except:
     print("something is wrong") 