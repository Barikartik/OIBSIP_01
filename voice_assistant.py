import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os

#Initialize the recognizer and text-to-speech
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def open_chrome():
    speak("Opening Chrome")
    os.system('start chrome') 

def listen():
    with sr.Microphone() as source:
        print("Listening..")
        audio = recognizer.listen(source)
        try:
            command=recognizer.recognize_google(audio)
            print(f"You said :{command}")
            return command.lower()
        except sr.UnknownValueError:
            speak("Sorry,I didn`t catch that:")
        except sr.RequestError:
            speak("Sorry, my speech service is down")

def perform_task(command):
    if "hello" in command:
        speak("Hello! How can I help you today?")
    elif "chrome" in command:
        open_chrome()
    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {current_time}")
    elif "date" in command:
        current_date = datetime.datetime.now().strftime("%B %d %Y")
        speak(f"Today`s date is {current_date}")
    elif "search for" in command:
        query = command.replace("search for","")
        speak(f"Searching for {query}")
        webbrowser.open(f"https://www.google.com/search?q={query}")
    else:
        speak("Sorry,I can`t help with that") 

if __name__=="_main_":
    while True:
        command = listen()
        if command:
         perform_task(command)


                                   

