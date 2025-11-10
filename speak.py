from gtts import gTTS
from playsound3 import playsound
b=str(input("enter your text \n"))
a=gTTS(text=b,lang="en")
a.save("parham.mp3")
playsound("./parham.mp3")
