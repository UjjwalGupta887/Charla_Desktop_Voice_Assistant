import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5') #voice ko lane ke liye use hua hai window mai inbuilt hoti hai.
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio): # use pyttsx3
    engine.say(audio)
    engine.runAndWait()

def wishme(): # use datetime
    hour = int(datetime.datetime.now().hour) # 0 se 24 tak muje hour mil jayega
    if hour>=0 and hour<12:
        speak('Good Morning Sir')
    elif hour>=12 and hour<18:
        speak('Good Afternoon Sir')
    else:
        speak('Good Evening Sir')
    speak('I am Charla. Please tell me How may I help you')

#use speech_Recognition
def takecommand(): # audio le rha hai microphone se or string mai write kar rha hai
    r = sr.Recognizer()
    with sr.Microphone() as source :
        print('Listening..')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Recognizing..')
        query = r.recognize_google(audio,language='en-in')
        print(f"User said : {query}\n")
    except Exception as e:
        print('Say that again Please..')
        return "None"
    return query

def sendemail(to,content):
    server = smtplib.SMTP()
    server.ehlo()
    server.starttls()
    server.login('youremailid@gmail.com','your password')
    server.sendmail('youremail',to,content)
    server.close()

if __name__ == '__main__':
    wishme()
    while True:
    # if 1:
        query =  takecommand().lower()
        #logic for executing task based on query
        # use wikipedia
        if 'wikipedia' in query:
            speak('Searching Wikipedia..')
            query = query.replace('Wikipedia','')
            results = wikipedia.summary(query,sentences=2)
            speak('According to wikipedia')
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open('youtube.com')
        elif 'open facebook' in query:
            webbrowser.open('facebook.com')
        elif 'open google' in query:
            webbrowser.open('google.com')
        elif 'open stackoverflow' in query:
            webbrowser.open('satckoverflow.com')
        elif 'open netflix' in query:
            webbrowser.open('netflix.com')
        elif 'open instagram' in query:
            webbrowser.open('instagram.com')
        elif 'open music' in query:
            webbrowser.open('music.com')

        # play music in own lapy
        elif 'play music' in query: # os module
            music_dir = 'E:\\Ujjwal Gupta\\Music'
            songs = os.listdir(music_dir)
            print(songs)
            os.stat(os.path.join(music_dir,songs[3]))
        elif 'the time' in query:
            strtime = datetime.datetime.now().strftime('%H:%M:%S')
            speak(f'Sir, the time is {strtime}')
        elif "open code" in query:
            codepath = "C:\\Users\\DELL\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"

        elif 'email to ujjwal' in query:
              try:
                  speak('What should I say ?')
                  content = takecommand()
                  to = 'youremaid@gmail.com'
                  sendemail(to,content)
                  speak('Email has been Sent')
              except Exception as e:
                  print(e)
                  speak('Sorry Sir, I am not able to send this email')
        
        elif "exit" in query:
            exit()
