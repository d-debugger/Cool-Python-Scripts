from gtts import gTTS
import os


print("\nINPUT THE NUMBER OF TEXT FILES THAT YOU WANT TO CONVERT INTO AUDIO: ",end="")

n=int(input())

for i in range(0,n):

    print("\nGIVE THE TEXT FILE NAME(.txt format): ",end="")
    txt=input()  

    f=open(txt)
    x=f.read()

    language='en'

    audio=gTTS(text=x,lang=language)

    print("\nGIVE THE AUDIO FILE NAME IN WHICH OUTPUT WILL BE SAVED(.wav or .mp3 format): ",end="")
    aud=input()

    audio.save(aud)
    os.system(aud)
