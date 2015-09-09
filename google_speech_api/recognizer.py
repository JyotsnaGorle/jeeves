from utils.say import say

import speech_recognition as sr

def recognize():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        audio = r.listen(source)

    try:
        return r.recognize_google(audio)
    except sr.UnknownValueError:
        say("Sorry, I could not understand that.")
    except sr.RequestError:
        say("Sorry, could not connect to the speech service. Check the internet connection.")
