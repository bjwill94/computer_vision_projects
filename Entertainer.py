import time
import webbrowser
import speech_recognition as sr
from time import ctime
import pyttsx3
import pywhatkit


r = sr.Recognizer()
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
rate = engine.getProperty('rate')
engine.setProperty('rate',130)
engine.setProperty('voice',voices[2].id)

def alexis_speak(audio_string):
    engine.say(audio_string)
    engine.runAndWait()

def record_voice(ask = False):
    with sr.Microphone() as source:
        if ask:
            alexis_speak(ask)
        else:
            alexis_speak('How can i help you')
        r.pause_threshold = 1
        print('listening')

        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
            voice_data = voice_data.lower()
            print(voice_data)
        except:
            pass
        return voice_data


def respond(voice_data):
    if 'what is your name' in voice_data:
        alexis_speak('senorita')
    elif 'play' in voice_data:
        song = voice_data.replace('play','')
        alexis_speak('playing'+song)
        pywhatkit.playonyt(song)
    elif 'what time is it' in voice_data:
        alexis_speak(ctime())
    elif 'search' in voice_data:
        search = record_voice('What do you want to search')
        url = 'https://google.com/search?q=' +search
        webbrowser.get().open(url)
        alexis_speak('here is what i found for'+search)
    elif 'location' in voice_data:
        loc = record_voice('what is the location ?')
        url = 'https://google.nl/maps/place/'+loc+'/&amp;'
        webbrowser.get().open(url)
        alexis_speak('here is the location of '+loc)
    elif 'thank you' in voice_data:
        exit()

time.sleep(1)
while 1:
    voice_command = record_voice()
    respond(voice_command)
