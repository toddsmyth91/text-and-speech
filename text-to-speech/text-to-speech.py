import pyttsx3
engine = pyttsx3.init()
engine.say("Hello World")
engine.runAndWait() 
# can also do single line usage
pyttsx3.speak("Single line usage") 
