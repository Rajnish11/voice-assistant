import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
import os
import smtplib
import pyaudio

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!Rajnish ")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!Rajnish ")   

    else:
        speak("Good Evening!Rajnish ")  

    speak(" how may i help you")       

def takeCommand():
    

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query



if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
            
        elif 'what are you doing' in query:
            speak('nothing, just wasteing my time with you.')  
        
        elif 'gf' in query:
            speak('sorry Rajnish, i have a boyfriend ')
        elif 'boyfriend' in query:
            speak('i do not want to tale you, because you cant keep my secret')
        elif 'suno na' in query:
            speak('Bolo')                  

        # elif 'open youtube' in query:
        #     webbrowser.open("youtube.com")

        

        elif 'music' in query:
            music_dir = 'G:\my music'
            songs = os.listdir(music_dir)
            # print(songs) 
            speak("enjoy! your favorite song")
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'chrome open' in query:
            codePath = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
            os.startfile(codePath)

        # elif 'email to rajnish' in query:
        #     try:
        #         speak("What should I say?")
        #         content = takeCommand()
        #         to = "mail.krrajnish@gmail.com"    
        #         sendEmail(to, content)
        #         speak("Email has been sent!")
        #     except Exception as e:
        #         print(e)
        #         speak("Sorry my friend Rajnish . I am not able to send this email")    
