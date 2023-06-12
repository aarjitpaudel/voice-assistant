import pyttsx3
engine = pyttsx3.init()
a=135
engine.setProperty('rate', a) 
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.say('Hello everyone, I am Sonic, the voice assistant robot. I was designed by Reewaz, Reason, Seerish, Abhinav, and Aarjit. I can provide you with the answers you need within seconds and be of service to you whenever you require assistance.')
engine.runAndWait()
