import cowsay
import gTTS

engine = gTTS.init()
this = input("What's this? ")
cowsay.cow(this)
engine.say(this)
engine.runAndWait()