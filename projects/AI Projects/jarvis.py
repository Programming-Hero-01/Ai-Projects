import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Jarvis, an intelligent Artificial Intelligence. I am created by Sri Ram. "
    "Please tell me how can I help you?")

def takeCommand():
    """It takes microphone input from the user and returns string output"""

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")

        except Exception as e:
            print("Can you please say that again...")
            return "None"
        return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("pittarekha26@gmail.com", "Saisriram@2007")
    server.sendmail("pittarekha26@gmail.com", to, content)
    server.close()

if __name__ == '__main__':
    wishMe()
    while True:
        query = takeCommand().lower()
        
        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=5)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music_dir = 'C:\\Users\\scien\\Fav_Songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"The time is {strTime}")

        elif 'open visual studio code' in query:
            codePath = "C:\\Users\\scien\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'open python charm' in query:
            pycharmPath = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2021.1\\bin\\pycharm64.exe"
            os.startfile(pycharmPath)

        elif 'open visual studio' in query:
            studioPath = "C:\\Program Files (x86)\\Microsoft Visual Studio\\2019\\Community\\Common7\\IDE\\devenv.exe"
            os.startfile(studioPath)

        elif 'open sub' in query:
            subPath = "C:\Program Files\Sublime Text 3\sublime_text.exe"
            os.startfile(subPath)

        elif 'email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = input(str("Enter email: "))
                sendEmail(to, content)
                speak("Email sent buddy!")
            
            except Exception as e:
                print(e)
                speak("Sorry my friend. I am not able to send this email."
                "Sorry for the inconvenience")

        elif 'bye' or 'end session' in query:
            break
