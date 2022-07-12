from tkinter import *
from PIL import Image,ImageTk
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random

root = Tk()
root.title("JARVIS GUI")
# root.configure(background="black")
root.minsize(600,400)

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)


def speek(audio):
    engine.say(audio)
    engine.runAndWait()

############################### left side #############################
main_frame_1 = Frame(root,bg="black",width = 720,height = 880,borderwidth=6,relief = SUNKEN)
main_frame_1.place(x=0,y=10)
label = Label(main_frame_1,text="VIRTUAL DESKTOP ASSISTANT",fg = "green",font = "Helvetica 16 bold").place(x=200,y=5)

hour = int(datetime.datetime.now().hour)
if hour>=0 and hour<12:
    label1 = Label(main_frame_1,text="Good morning!",font="arial 10 italic",bg="black",fg="white").place(x = 15,y=40)
elif hour>=12 and hour<17:
    label2 = Label(main_frame_1,text="Good Afternoon!",font="arial 10 italic",bg="black",fg="white").place(x=15,y=40)
else:
    label3 = Label(main_frame_1,text="Good Evening!",font="arial 10 italic",bg="black",fg="white").place(x=15,y=40)
label4 = Label(main_frame_1,text="Hello sir,I am Jarvis.Please tell me how may i help you",font="arial 10 italic",bg="black",fg="white").place(x=15,y=60)
# speek("Hello sir,I am Jarvis.Please tell me how may i help you")

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        # label1 = Label(main_frame_1,text="Good morning!",font="arial 10 italic",bg="black",fg="white").place(x = 15,y=40)
        speek("Good morning!")
    elif hour>=12 and hour<17:
        # label2 = Label(main_frame_1,text="Good Afternoon!",font="arial 10 italic",bg="black",fg="white").place(x=15,y=40)
        speek("Good Afternoon!")
    else:
        # label3 = Label(main_frame_1,text="Good Evening!",font="arial 10 italic",bg="black",fg="white").place(x=15,y=40)
        speek("Good Evening!")
    # label4 = Label(main_frame_1,text="Hello sir,I am Jarvis.Please tell me how may i help you",font="arial 10 italic",bg="black",fg="white").place(x=15,y=60)
    speek("Hello sir,I am Jarvis.Please tell me how may i help you")


def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        label5 = Label(main_frame_1,text="Listening......",font="arial 10 italic",bg="black",fg="white").place(x=15,y=80)
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        label6 = Label(main_frame_1,text="Recognizing......",font="arial 10 italic",bg="black",fg="white").place(x=15,y=100)
        query = r.recognize_google(audio,language='en-in')
        # print(f"User said : {query}\n")
        label6 = Label(main_frame_1,text=f"User said : {query}\n",font="arial 10 italic",bg="black",fg="white").place(x=15,y=100)

    except Exception as e:
        # print(e)
        label7 = Label(main_frame_1,text="Say that again please...",font="arial 10 italic",bg="black",fg="white").place(x=15,y=120)
        return "None"
    return query


def hello():
    # i = 0
    wishMe()
    while True:
          query = takeCommand().lower()
          # logic for executing tasks based on query
          if 'wikipedia' in query:
              speek("Searching Wikipedia...")
              query = query.replace('wikipedia','')
              results = wikipedia.summary(query,sentences = 2)
              speek("According to wikipedia")
              speek(results)
              str = results
              label8 = Label(main_frame_1,text=str[0:100],font="arial 10 italic",bg="black",fg="white").place(x=15,y=140)
              label9 = Label(main_frame_1,text=str[101:len(str)],font="arial 10 italic",bg="black",fg="white").place(x=15,y=160)

          elif 'open youtube' in query:
              webbrowser.open("youtube.com")

          elif 'open google' in query:
              webbrowser.open("google.com")

          elif 'open stackoverflow' in query:
              webbrowser.open("stackoverflow.com")

          elif 'open chrome' in query:
              codepath1 = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
              os.startfile(codepath1)

          elif 'play music' in query:
              music_dir = 'C:\\songs'
              songs = os.listdir(music_dir)
              no = random.randint(0,4)
              os.startfile(os.path.join(music_dir,songs[no]))

          elif 'play video' in query:
              video_dir = 'C:\\Movies'
              movies = os.listdir(video_dir)
              os.startfile(os.path.join(video_dir,movies[0]))

          elif 'time' in query:
              strtime = datetime.datetime.now().strftime("%H:%M:%S")
              speek(f"Sir,the time is {strtime}")

          elif 'open code' in query:
              codepath = "C:\\Users\\prasa\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
              os.startfile(codepath)
            
          elif 'exit' or 'quit' in query:
               break

        #   i+=1
          

f1 = Frame(main_frame_1,bg="gray",width = 715,height = 380,borderwidth=6,relief = SUNKEN)
f1.place(x=6,y=400)
Button(f1,text="START QUERY",compound = CENTER,fg="red",bg="white",width = 20,bd=5,relief = SUNKEN,command=hello).place(x= 260,y=5)

instruction_label = Label(f1,text="INSTRUCTION :-",fg = "PURPLE",font = "Helvetica 16 italic").place(x=10,y=70)
inst_label_1 = Label(f1,text="-->Click on start button to ask your query :-",fg = "black",font = "arial 12 italic").place(x=10,y=110)
inst_label_2 = Label(f1,text="-->Click on start button to ask your query :-",fg = "black",font = "arial 12 italic").place(x=10,y=150)
inst_label_3 = Label(f1,text="-->Click on start button to ask your query :-",fg = "black",font = "arial 12 italic").place(x=10,y=190)
Button(f1,text="PATH",compound = CENTER,fg="red",bg="white",width = 20,bd=5,relief = SUNKEN).place(x= 20,y=300)


############################## right side ##############################
main_frame_2 = Frame(root,bg="white",width = 800,height = 880,borderwidth=6,relief = SUNKEN)
main_frame_2.place(x=730,y=10)
image = Image.open("img//jarvis.jpg")
image = image.resize((787, 800), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(image)
label = Label(image=photo)
label.place(x=735,y=17)

root.mainloop()