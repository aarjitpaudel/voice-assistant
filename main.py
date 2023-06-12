#NAME IS SONIC

import pyttsx3
import pywin32_system32
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser as wb
import os
import random
import pyautogui
import random
import pywhatkit
import requests

engine = pyttsx3.init()
listener = sr.Recognizer()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
a=135
engine.setProperty('rate', a) 

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I %p")
    speak(f'current time is {Time}')
    print("The current time is ", Time)

def date():
    day = int(datetime.datetime.now().day)
    month = int(datetime.datetime.now().month)
    year = int(datetime.datetime.now().year)
    speak("the current date is")
    speak(f"{day} {month} {year}")
    print("The current date is " + str(day) + "/" + str(month) + "/" + str(year))

def wishme():
    print("Welcome!!")
    speak("Welcome!!")
    e = ["How can i assist you?", "How can i help you?", "How may i serve you?"]
    hour = datetime.datetime.now().hour
    if hour >= 4 and hour < 12:
        speak(f"Good morning. {random.choice(e)}")
        print("")
    elif hour >= 12 and hour < 16:
        speak(f"Good afternoon. {random.choice(e)}")
        print("")
    elif hour >= 16 and hour < 24:
        speak(f"Good evening. {random.choice(e)}")
        print("")
    else:
        speak("Good night.")

def screenshot():
    img = pyautogui.screenshot()
    img.save("./ss/ss.png")

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone(device_index=0) as source:
        r.adjust_for_ambient_noise(source, duration=1)
        #r.pause_threshold = 1
        print("Listening...")
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(query)

    except Exception as e:
        print(e)
        speak("")
        return "Try Again"

    return query

if __name__ == "__main__":
    wishme()
    while True:
        a = ["hi", "hello", "greetings", "namaste", "namaskar"]
        d = ["I'm sonic, an AI voice assistant","My name is Sonic and i am an AI assistant robot."]
        b = ["i am in the best of spirits", "i am good, what about you", "thanks for asking, i am good"]
        c = ["ADD JOKES"]
        query = takecommand().lower()
        if "time" in query:
            time()

        elif "date" in query:
            date()
        
        elif 'hello' in query:
            speak(random.choice(a))
        
        elif "who are your creators" in query:
            speak("The people that created me are Reason Pokharel, Sirish Poudel,Aarjit Paudel, Riwaz Acharya, Abhinav Rokaha. ")
        
        elif "who are you" in query:
            speak("I'm sonic, a desktop voice assistant.")
            print("I'm sonic, a desktop voice assistant.")

        elif "how are you" in query:
            speak(random.choice(b))
            print(random.choice(b))

        elif "fine" in query:
            speak("Glad to hear that!!")
            print("Glad to hear that!!")

        elif "good" in query:
            speak("Glad to hear that!!")
            print("Glad to hear that!!")

        elif "tell me about" in query:
            try:
                query = query.replace("tell me about","")
                if "this school" in query:
                    speak("nice school")
                else:
                    speak("wait, let me think...")
                    result = wikipedia.summary(query, sentences=2)
                    print(result)
                    speak(result)
            except:
                speak("Can't find this page, please ask something else.")
    
        elif "open youtube" in query:
            wb.open("youtube.com") 

        elif "open google" in query:
            wb.open("google.com") 
   
        elif "open stack overflow" in query:
            wb.open("stackoverflow.com")

        elif 'play' in query:
            song = query.replace('play', '')
            speak('playing ' + song)
            pywhatkit.playonyt(song)

        elif "remember" in query:
            speak("What should I remember")
            data = takecommand()
            speak("You told me to remember that" + data)
            print("You told me to remember that " + str(data))
            remember = open("data.txt", "w")
            remember.write(data)
            remember.close()

        elif "do you remember anything" in query:
            remember = open("data.txt", "r")
            speak("You told me to remember that" + remember.read())
            print("You told me to remember that " + str(remember))

        elif "screenshot" in query:
            screenshot()
            speak("I've taken the screenshot, please check it")
        
        elif "alarm" in query:
            speak("enter the time")
            time = input("Enter the time(HH:MM:SS):")
            speak(f"alarm set for {time}")
            while True:
                time_now=datetime.datetime.now()
                now = time_now.strftime("%H:%M:%S")
                if now == time:
                    speak("Time is up")
                    break
        elif "weather" in query:
            api_key = "a489106d98db3ccfac1ab48dbd82f83b"
            base_url = "http://api.openweathermap.org/data/2.5/weather?"
            city_name = "Pokhara"
            complete_url = base_url + "appid=" + api_key + "&q=" + city_name
            response = requests.get(complete_url)
            x = response.json()
            y = x["main"]
            z = x["wind"]
            temperature = round((y["temp"] - 273.15), 2)
            wind_speed = z["speed"]
            speak("Temperature in " + city_name + " is " + str(temperature) + "°C.")
            speak("Wind speed in " + city_name + " is " + str(wind_speed) + "meter per second")

        elif "Tell me a joke." in query:
            speak(random.choice(c))

        elif "introduce yourself" in query:
            speak("Hello everyone, I am Sonic, the voice assistant robot. I was designed by Reewaz, Reason, Seerish, Abhinav, and Aarjit. I can provide you with the answers you need within seconds and be of service to you whenever you require assistance.")

        elif "turn off" in query:
            speak("good bye, have a nice day")
            quit()
