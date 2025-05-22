from gtts import gTTS
import speech_recognition as sr
import os

mytext = "hello, welcome to devil's laptop"

language = 'en'


myobj = gTTS(text=mytext, lang=language, slow=False)

myobj.save("welcome.mp3")

os.system("start welcome.mp3")