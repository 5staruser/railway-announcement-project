import os
import pandas as pd
from pydub import AudioSegment
from gtts import gTTS
def texttospeech(text,filename):
    mytext=str(text)
    language="hi"
    myobj=gTTS(text=mytext,lang=language,slow=True)
    myobj.save(filename)
# this function return pydub audio segment
def mergeaudios(audios):
    combined=AudioSegment.empty()
    for audio in audios:
        combined+=AudioSegment.from_mp3(audio)
    return combined
def generateskeleton():
    audio=AudioSegment.from_mp3("railway.mp3")
    #generating kripiya dhyan dijiye
    start=88000
    finish=90200
    audioproccessed=audio[start:finish]
    audioproccessed.export("hindi1.mp3",format="mp3")
    #generate from city
    #generate se chalkar
    start = 91000
    finish = 92200
    audioproccessed = audio[start:finish]
    audioproccessed.export("hindi3.mp3", format="mp3")
    #via city
    #ke raaste
    start = 94000
    finish = 95000
    audioproccessed = audio[start:finish]
    audioproccessed.export("hindi5.mp3", format="mp3")
    #to city
    #generate ko jaane waali gaaadi sankhya
    start = 96000
    finish = 98900
    audioproccessed = audio[start:finish]
    audioproccessed.export("hindi7.mp3", format="mp3")
    #train no and name
    #generate kuch hi samay mei platform sankhaya
    start = 105500
    finish = 108200
    audioproccessed = audio[start:finish]
    audioproccessed.export("hindi9.mp3", format="mp3")
    #platform no
    #generate par aa rhi hai
    start = 109000
    finish = 112250
    audioproccessed = audio[start:finish]
    audioproccessed.export("hindi11.mp3", format="mp3")
def generateannouncement(filename):
    df=pd.read_excel(filename)
    for index,items in df.iterrows():
        # generate from city
        texttospeech(items["from"],"hindi2.mp3")
        # via city
        texttospeech(items["via"], "hindi4.mp3")
        # to city
        texttospeech(items["to"], "hindi6.mp3")
        # train no and name
        texttospeech(items["train_no"]+" "+items["train_name"], "hindi8.mp3")
        # platform no
        texttospeech(items["platform"], "hindi10.mp3")
        audios=[f"hindi{i}.mp3" for i in range(1,12)]
        announcement=mergeaudios(audios)
        announcement.export(f"announcement_{items['train_no']}{index+1}.mp3",format="mp3")
if __name__ == '__main__':
    print("Generating skeleton")
    generateskeleton()
    print("Generating announcement")
    generateannouncement("announce_hindi.xlsx")
