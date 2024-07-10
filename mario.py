from datetime import datetime
from threading import main_thread
from unicodedata import name

from pip import main
import pyttsx3
import datetime
import wikipedia
import webbrowser
import speech_recognition as sr


engine=pyttsx3.init('sapi5')
voice = engine.getProperty('voices')
engine.setProperty('voice',voice[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning!")

    elif hour>=12 and hour<18:
        speak("good afternoon!")

    else:
        speak("good evening!")

    speak("i am mario sir how can i help you")



    
def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold=1
        audio=r.listen(source)

    try:
        print("recognizing")
        query = r.recognize_google(audio,language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
         print("say that again please...")
         return "none"
    return query



if __name__=="__main__":
    wishMe()
    while True:
       query=takecommand().lower()
       if "wikipedia" in query:
           speak("searching wikipedia...")
           query=query.replace("wikipedia","")
           results=wikipedia.summary(query, sentences=2)
           print(results)
           speak(results)
       elif "open youtube" in query:
            webbrowser.open("youtube.com") 
       elif "open google" in query:
            webbrowser.open("google.com")
       elif "stop" in query:
            break
    
speak("thank you")