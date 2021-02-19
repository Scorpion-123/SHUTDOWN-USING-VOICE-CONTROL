import pyttsx3
# importing speech_recognition
import speech_recognition as sr
# importing os module
import os

# Initializing the voice engine.
engine = pyttsx3.init()

def Speak(audio):
    engine.say(audio)
    engine.runAndWait()


def take_commands():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 0.7
        #for adjusting the pause threshold.
        audio = r.listen(source)
        try:
            print("Recognizing..")
            # Recognizing audio using google api
            Query = r.recognize_google(audio)
            print("the user said :'", Query, "'")
        except Exception as e:
            print(e)
            Speak("say that again please")
            # returning none if there are errors
            return "None"
    return Query


Speak("Do you want to shutdown your computer boss?")
while True:
    command = take_commands()
    if "no" in command:
        Speak("Thank u sir I will not shut down the computer")
        break
    if "yes" in command:
        Speak("Shutting down your computer boss")
        os.system("shutdown /s /t 30")
        break
    Speak("Can't understand say that again sir")