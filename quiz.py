import time
import speech_recognition as sr
import pyttsx3
from playsound import playsound
import music

r = sr.Recognizer()
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
rate = engine.getProperty('rate')
engine.setProperty('rate',120)
engine.setProperty('voice',voices[0].id)

def alexis_speak(audio_string):
    engine.say(audio_string)
    engine.runAndWait()

def record_voice(ask = False):
    with sr.Microphone() as source:
        if ask:
            alexis_speak(ask)
        else:
            alexis_speak('Please tell me start to begin our quiz')
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
    if 'start' in voice_data:
        music.intro()
        time.sleep(9)
        alexis_speak('who is the father of our nation')
        ans = record_voice('beep')
        print(ans)
        if 'gandhi' in ans:
            music.winner()
            time.sleep(4)
            alexis_speak('wonderful you got 10 points')
            # playsound('C:/Users/HP/Desktop/roboui/quizmusic.mp3')
            #question 2
            alexis_speak('Who was the first President of India?')
            ans = record_voice('beep')
            print(ans)
            if 'rajendra' in ans:
                music.winner2()
                time.sleep(4)
                alexis_speak('wonderful you got 20 points')
                # question 2
                time.sleep(4)
                alexis_speak('Smallest state of India is')
                ans = record_voice('beep')
                print(ans)
                if 'goa' in ans:
                    music.winner2()
                    time.sleep(4)
                    alexis_speak('wonderful you got 30 points')
                else:
                    music.loser()
                    time.sleep(2)
                    alexis_speak('better luck next time')
                    exit()

            else:
                music.loser()
                alexis_speak('better luck next time')
                exit()

        else:
            music.loser()
            time.sleep(2)
            alexis_speak('better luck next time')
            exit()
    elif 'thank you' in voice_data:
        exit()

time.sleep(1)

while 1:
    voice_command = record_voice()
    respond(voice_command)
