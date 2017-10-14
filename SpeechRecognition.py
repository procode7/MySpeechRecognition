#A simple speech recocgnition system
import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()
engine.setProperty('rate',95)
engine.setProperty('volume',1.0*10)
print("App is running")

while (True):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        engine.say("Say Something ")
        engine.runAndWait()
        audio = r.listen(source)
    try:
        engine.say("You said" + r.recognize_google(audio))
        engine.runAndWait()
    except sr.UnknownValueError:
        engine.say("Google Speech Recognition could not understand audio")
        engine.runAndWait()
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))










