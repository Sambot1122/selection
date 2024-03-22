import tkinter as tk
from PIL import Image , ImageTk
import pygame
from pygame import mixer
from threading import Thread
import time

pygame.mixer.init()
root = tk.Tk()
selection=[]
selection2=[]
selection3=[]


#初始畫面
root.geometry("1060x720+300+200")
root.title("音樂風格喜好測驗")

prologue=tk.Frame(root)
prologue.pack()

page2=tk.Frame(root)

page3=tk.Frame(root)

page4 = tk.Frame(root)

page5 = tk.Frame(root)

page6 = tk.Frame(root)

page7 = tk.Frame(root)

page8 = tk.Frame(root)

page9 = tk.Frame(root)

#首頁

label1 = tk.Label(prologue,text="音樂風格喜好測驗",bg="black",fg="white",padx="1060",
                  pady="300",font=("Bauhaus 93",18,"bold","italic"))



#pic
imageplay=Image.open("playbutton.png")
tk_imageplay=ImageTk.PhotoImage(imageplay)

imagepause=Image.open("pausebutton.png")
tk_imagepause=ImageTk.PhotoImage(imagepause)

imagelemon=Image.open("lemon.jpg")
tk_imagelemon=ImageTk.PhotoImage(imagelemon)

imagerock=Image.open("enter sandman.jpg")
tk_imagerock=ImageTk.PhotoImage(imagerock)

imagecountryroad=Image.open("countryroad.jpg")
tk_imagecountryroad=ImageTk.PhotoImage(imagecountryroad)


imagespectre=Image.open("the_spectre.jpg")
tk_imagespectre=ImageTk.PhotoImage(imagespectre)


imagefirstnote=Image.open("First_Note.jpg")
tk_imagefirstnote=ImageTk.PhotoImage(imagefirstnote)


imagestronger=Image.open("stronger.jpg")
tk_imagestronger=ImageTk.PhotoImage(imagestronger)


imagemoonlight=Image.open("moonlight.jpg")
tk_imagemoonlight=ImageTk.PhotoImage(imagemoonlight)

imagelost_in_a_wave=Image.open("lost_in_a_wave.jpg")
tk_imagelost_in_a_wave=ImageTk.PhotoImage(imagelost_in_a_wave)


#切換頁面
def switch(frame1,frame2):
    frame1.destroy()
    frame2.pack()
    

#播放音樂
class Musicplayer:
    def __init__(self, master, file_path,n,m):
       self.master = master
       self.file_path = file_path
       self.paused = False
       self.paused_pos = 0

       self.mixer = mixer
       self.mixer.init()
       

       self.pause_button = tk.Button(self.master,image=tk_imagepause,width=90,height=90, text="Pause", command=self.pause_music)
       self.pause_button.grid(row=n,column=int(m+1))
       

       self.play_button = tk.Button(self.master,image=tk_imageplay,width=90,height=90, text="Play", command=self.play_music)
       self.play_button.grid(row=n,column=m)
       

       self.thread=Thread(target=self.play_music_thread)

    def play_music_thread(self):
        if self.paused:
            self.mixer.music.play(start=self.paused_pos)
        else:
            self.mixer.music.play()
        
    def play_music(self):
        if  not self.thread.is_alive():
            self.mixer.music.load(self.file_path)
            self.thread = Thread(target=self.play_music_thread)
            self.thread.start()
            
    def pause_music(self):
        self.paused_pos = self.paused_pos+(self.mixer.music.get_pos() / 1000)
        self.mixer.music.pause()
        self.paused = True
        
#音樂選擇
def plus(n,m,p,func):
    selection.append(n)
    m.destroy()
    p.pack()
    func
    
    
def last_plus(n,m,p,func):
    selection.append(n)
    m.destroy()
    p.pack()
    func()
    
def plus2(n,m,p,func):
    selection2.append(n)
    m.destroy()
    p.pack()
    func
    
    
def last_plus2(n,m,p,func):
    selection2.append(n)
    m.destroy()
    p.pack()
    func()

def plus3(n,m,p,func):
    selection3.append(n)
    m.destroy()
    p.pack()
    func()
#開始鍵
B1= tk.Button(prologue,text="開始",relief="groove",activebackground="white",activeforeground="red",
             state=tk.NORMAL,padx="300",pady="100",command=lambda:switch(prologue,page2))



label1.pack()
B1.pack()

#第二頁
def lemon(page,column1,page_2,round,b):
    pic1=tk.Label(page,image=tk_imagelemon,width="450",height="450")
    pic1.grid(row=0,column=column1,padx="40",columnspan=2)
    lemonplay=Musicplayer(page,"lemon.mp3",1,b)
    label2 = tk.Label(page,text="lemon",bg="yellow",font=("Bauhaus 93",30,"bold","italic"))
    label2.grid(row=2,column=column1,columnspan=2)
    B_lemon = tk.Button(page,text="select",font=("Bauhaus 93",30,"bold","italic"),command=lambda:plus("lemon",page,page_2,round))
    B_lemon.grid(row=3,column=column1,columnspan=2)

def entersandman(page,column1,page_2,round,b):
    pic2=tk.Label(page,image=tk_imagerock,width="450",height="450")
    pic2.grid(row=0,column=column1,padx="40",columnspan=2)
    entersandman=Musicplayer(page,"entersandman.mp3",1,b)
    label3 = tk.Label(page,text="entersandman",bg="yellow",font=("Bauhaus 93",30,"bold","italic"))
    label3.grid(row=2,column=column1,columnspan=2)
    B_entersandman = tk.Button(page,text="select",font=("Bauhaus 93",30,"bold","italic"),command=lambda:plus("entersandman",page,page_2,round))
    B_entersandman.grid(row=3,column=column1,columnspan=2)

def lemon2(page,column1,page_2,round,b):
    pic1=tk.Label(page,image=tk_imagelemon,width="450",height="450")
    pic1.grid(row=0,column=column1,padx="40",columnspan=2)
    lemonplay=Musicplayer(page,"lemon.mp3",1,b)
    label2 = tk.Label(page,text="lemon",bg="yellow",font=("Bauhaus 93",30,"bold","italic"))
    label2.grid(row=2,column=column1,columnspan=2)
    B_lemon = tk.Button(page,text="select",font=("Bauhaus 93",30,"bold","italic"),command=lambda:plus2("lemon",page,page_2,round))
    B_lemon.grid(row=3,column=column1,columnspan=2)

def entersandman2(page,column1,page_2,round,b):
    pic2=tk.Label(page,image=tk_imagerock,width="450",height="450")
    pic2.grid(row=0,column=column1,padx="40",columnspan=2)
    entersandman=Musicplayer(page,"entersandman.mp3",1,b)
    label3 = tk.Label(page,text="entersandman",bg="yellow",font=("Bauhaus 93",30,"bold","italic"))
    label3.grid(row=2,column=column1,columnspan=2)
    B_entersandman = tk.Button(page,text="select",font=("Bauhaus 93",30,"bold","italic"),command=lambda:plus2("entersandman",page,page_2,round))
    B_entersandman.grid(row=3,column=column1,columnspan=2)

def lemon3(page,column1,page_2,round,b):
    pic1=tk.Label(page,image=tk_imagelemon,width="450",height="450")
    pic1.grid(row=0,column=column1,padx="40",columnspan=2)
    lemonplay=Musicplayer(page,"lemon.mp3",1,b)
    label2 = tk.Label(page,text="lemon",bg="yellow",font=("Bauhaus 93",30,"bold","italic"))
    label2.grid(row=2,column=column1,columnspan=2)
    B_lemon = tk.Button(page,text="select",font=("Bauhaus 93",30,"bold","italic"),command=lambda:plus3("lemon",page,page_2,round))
    B_lemon.grid(row=3,column=column1,columnspan=2)

def entersandman3(page,column1,page_2,round,b):
    pic2=tk.Label(page,image=tk_imagerock,width="450",height="450")
    pic2.grid(row=0,column=column1,padx="40",columnspan=2)
    entersandman=Musicplayer(page,"entersandman.mp3",1,b)
    label3 = tk.Label(page,text="entersandman",bg="yellow",font=("Bauhaus 93",30,"bold","italic"))
    label3.grid(row=2,column=column1,columnspan=2)
    B_entersandman = tk.Button(page,text="select",font=("Bauhaus 93",30,"bold","italic"),command=lambda:plus3("entersandman",page,page_2,round))
    B_entersandman.grid(row=3,column=column1,columnspan=2)
#第三頁
def countryroad(page,column1,page_2,round,b):
    pic1=tk.Label(page,image=tk_imagecountryroad,width="450",height="450")
    pic1.grid(row=0,column=column1,padx="40",columnspan=2)
    countryroadplay = Musicplayer(page,"countryroad.mp3",1,b)
    label4 = tk.Label(page,text="Take Me Home,Country Road",bg="yellow",font=("Bauhaus 93",25,"bold","italic"))
    label4.grid(row=2,column=column1,columnspan=2)
    B_countryroad = tk.Button(page,text="select",font=("Bauhaus 93",30,"bold","italic"),command=lambda:plus("countryroad",page,page_2,round))
    B_countryroad.grid(row=3,column=column1,columnspan=2)

def spectre(page,column1,page_2,round,b):
    pic2=tk.Label(page,image=tk_imagespectre,width="450",height="450")
    pic2.grid(row=0,column=column1,padx="40",columnspan=2)
    spectreplay = Musicplayer(page,"the_spectre.mp3",1,b)
    label5 = tk.Label(page,text="The Spectre",bg="yellow",font=("Bauhaus 93",30,"bold","italic"))
    label5.grid(row=2,column=column1,columnspan=2)
    B_spectre = tk.Button(page,text="select",font=("Bauhaus 93",30,"bold","italic"),command=lambda:plus("spectre",page,page_2,round))
    B_spectre.grid(row=3,column=column1,columnspan=2)

def countryroad2(page,column1,page_2,round,b):
    pic1=tk.Label(page,image=tk_imagecountryroad,width="450",height="450")
    pic1.grid(row=0,column=column1,padx="40",columnspan=2)
    countryroadplay = Musicplayer(page,"countryroad.mp3",1,b)
    label4 = tk.Label(page,text="Take Me Home,Country Road",bg="yellow",font=("Bauhaus 93",25,"bold","italic"))
    label4.grid(row=2,column=column1,columnspan=2)
    B_countryroad = tk.Button(page,text="select",font=("Bauhaus 93",30,"bold","italic"),command=lambda:plus2("countryroad",page,page_2,round))
    B_countryroad.grid(row=3,column=column1,columnspan=2)

def spectre2_1(page,column1,page_2,round,b):
    pic2=tk.Label(page,image=tk_imagespectre,width="450",height="450")
    pic2.grid(row=0,column=column1,padx="40",columnspan=2)
    spectreplay = Musicplayer(page,"the_spectre.mp3",1,b)
    label5 = tk.Label(page,text="The Spectre",bg="yellow",font=("Bauhaus 93",30,"bold","italic"))
    label5.grid(row=2,column=column1,columnspan=2)
    B_spectre = tk.Button(page,text="select",font=("Bauhaus 93",30,"bold","italic"),command=lambda:last_plus2("spectre",page,page_2,round))
    B_spectre.grid(row=3,column=column1,columnspan=2)

def countryroad2_1(page,column1,page_2,round,b):
    pic1=tk.Label(page,image=tk_imagecountryroad,width="450",height="450")
    pic1.grid(row=0,column=column1,padx="40",columnspan=2)
    countryroadplay = Musicplayer(page,"countryroad.mp3",1,b)
    label4 = tk.Label(page,text="Take Me Home,Country Road",bg="yellow",font=("Bauhaus 93",25,"bold","italic"))
    label4.grid(row=2,column=column1,columnspan=2)
    B_countryroad = tk.Button(page,text="select",font=("Bauhaus 93",30,"bold","italic"),command=lambda:last_plus2("countryroad",page,page_2,round))
    B_countryroad.grid(row=3,column=column1,columnspan=2)

def spectre2(page,column1,page_2,round,b):
    pic2=tk.Label(page,image=tk_imagespectre,width="450",height="450")
    pic2.grid(row=0,column=column1,padx="40",columnspan=2)
    spectreplay = Musicplayer(page,"the_spectre.mp3",1,b)
    label5 = tk.Label(page,text="The Spectre",bg="yellow",font=("Bauhaus 93",30,"bold","italic"))
    label5.grid(row=2,column=column1,columnspan=2)
    B_spectre = tk.Button(page,text="select",font=("Bauhaus 93",30,"bold","italic"),command=lambda:plus2("spectre",page,page_2,round))
    B_spectre.grid(row=3,column=column1,columnspan=2)

def countryroad3(page,column1,page_2,round,b):
    pic1=tk.Label(page,image=tk_imagecountryroad,width="450",height="450")
    pic1.grid(row=0,column=column1,padx="40",columnspan=2)
    countryroadplay = Musicplayer(page,"countryroad.mp3",1,b)
    label4 = tk.Label(page,text="Take Me Home,Country Road",bg="yellow",font=("Bauhaus 93",25,"bold","italic"))
    label4.grid(row=2,column=column1,columnspan=2)
    B_countryroad = tk.Button(page,text="select",font=("Bauhaus 93",30,"bold","italic"),command=lambda:plus3("countryroad",page,page_2,round))
    B_countryroad.grid(row=3,column=column1,columnspan=2)

def spectre3(page,column1,page_2,round,b):
    pic2=tk.Label(page,image=tk_imagespectre,width="450",height="450")
    pic2.grid(row=0,column=column1,padx="40",columnspan=2)
    spectreplay = Musicplayer(page,"the_spectre.mp3",1,b)
    label5 = tk.Label(page,text="The Spectre",bg="yellow",font=("Bauhaus 93",30,"bold","italic"))
    label5.grid(row=2,column=column1,columnspan=2)
    B_spectre = tk.Button(page,text="select",font=("Bauhaus 93",30,"bold","italic"),command=lambda:plus3("spectre",page,page_2,round))
    B_spectre.grid(row=3,column=column1,columnspan=2)
#第四頁
def firstnote(page,column1,page_2,round,b):
    pic1=tk.Label(page,image=tk_imagefirstnote,width="450",height="450")
    pic1.grid(row=0,column=column1,padx="40",columnspan=2)
    firstnoteplay = Musicplayer(page,"FIRST_NOTE.mp3",1,b)
    label6 = tk.Label(page,text="First Note",bg="yellow",font=("Bauhaus 93",30,"bold","italic"))
    label6.grid(row=2,column=column1,columnspan=2)
    B_firstnote = tk.Button(page,text="select",font=("Bauhaus 93",30,"bold","italic"),command=lambda:plus("firstnote",page,page_2,round))
    B_firstnote.grid(row=3,column=column1,columnspan=2)

def stronger(page,column1,page_2,round,b):
    pic2=tk.Label(page,image=tk_imagestronger,width="450",height="450")
    pic2.grid(row=0,column=column1,padx="40",columnspan=2)
    strongerplay = Musicplayer(page,"stronger.mp3",1,b)
    label7 = tk.Label(page,text="Stronger",bg="yellow",font=("Bauhaus 93",30,"bold","italic"))
    label7.grid(row=2,column=column1,columnspan=2)
    B_stronger = tk.Button(page,text="select",font=("Bauhaus 93",30,"bold","italic"),command=lambda:plus("stronger",page,page_2,round))
    B_stronger.grid(row=3,column=column1,columnspan=2)

def firstnote2(page,column1,page_2,round,b):
    pic1=tk.Label(page,image=tk_imagefirstnote,width="450",height="450")
    pic1.grid(row=0,column=column1,padx="40",columnspan=2)
    firstnoteplay = Musicplayer(page,"FIRST_NOTE.mp3",1,b)
    label6 = tk.Label(page,text="First Note",bg="yellow",font=("Bauhaus 93",30,"bold","italic"))
    label6.grid(row=2,column=column1,columnspan=2)
    B_firstnote = tk.Button(page,text="select",font=("Bauhaus 93",30,"bold","italic"),command=lambda:plus2("firstnote",page,page_2,round))
    B_firstnote.grid(row=3,column=column1,columnspan=2)

def stronger2_1(page,column1,page_2,round,b):
    pic2=tk.Label(page,image=tk_imagestronger,width="450",height="450")
    pic2.grid(row=0,column=column1,padx="40",columnspan=2)
    strongerplay = Musicplayer(page,"stronger.mp3",1,b)
    label7 = tk.Label(page,text="Stronger",bg="yellow",font=("Bauhaus 93",30,"bold","italic"))
    label7.grid(row=2,column=column1,columnspan=2)
    B_stronger = tk.Button(page,text="select",font=("Bauhaus 93",30,"bold","italic"),command=lambda:last_plus2("stronger",page,page_2,round))
    B_stronger.grid(row=3,column=column1,columnspan=2)

def firstnote2_1(page,column1,page_2,round,b):
    pic1=tk.Label(page,image=tk_imagefirstnote,width="450",height="450")
    pic1.grid(row=0,column=column1,padx="40",columnspan=2)
    firstnoteplay = Musicplayer(page,"FIRST_NOTE.mp3",1,b)
    label6 = tk.Label(page,text="First Note",bg="yellow",font=("Bauhaus 93",30,"bold","italic"))
    label6.grid(row=2,column=column1,columnspan=2)
    B_firstnote = tk.Button(page,text="select",font=("Bauhaus 93",30,"bold","italic"),command=lambda:last_plus2("firstnote",page,page_2,round))
    B_firstnote.grid(row=3,column=column1,columnspan=2)

def stronger2(page,column1,page_2,round,b):
    pic2=tk.Label(page,image=tk_imagestronger,width="450",height="450")
    pic2.grid(row=0,column=column1,padx="40",columnspan=2)
    strongerplay = Musicplayer(page,"stronger.mp3",1,b)
    label7 = tk.Label(page,text="Stronger",bg="yellow",font=("Bauhaus 93",30,"bold","italic"))
    label7.grid(row=2,column=column1,columnspan=2)
    B_stronger = tk.Button(page,text="select",font=("Bauhaus 93",30,"bold","italic"),command=lambda:plus2("stronger",page,page_2,round))
    B_stronger.grid(row=3,column=column1,columnspan=2)

def firstnote3(page,column1,page_2,round,b):
    pic1=tk.Label(page,image=tk_imagefirstnote,width="450",height="450")
    pic1.grid(row=0,column=column1,padx="40",columnspan=2)
    firstnoteplay = Musicplayer(page,"FIRST_NOTE.mp3",1,b)
    label6 = tk.Label(page,text="First Note",bg="yellow",font=("Bauhaus 93",30,"bold","italic"))
    label6.grid(row=2,column=column1,columnspan=2)
    B_firstnote = tk.Button(page,text="select",font=("Bauhaus 93",30,"bold","italic"),command=lambda:plus3("firstnote",page,page_2,round))
    B_firstnote.grid(row=3,column=column1,columnspan=2)

def stronger3(page,column1,page_2,round,b):
    pic2=tk.Label(page,image=tk_imagestronger,width="450",height="450")
    pic2.grid(row=0,column=column1,padx="40",columnspan=2)
    strongerplay = Musicplayer(page,"stronger.mp3",1,b)
    label7 = tk.Label(page,text="Stronger",bg="yellow",font=("Bauhaus 93",30,"bold","italic"))
    label7.grid(row=2,column=column1,columnspan=2)
    B_stronger = tk.Button(page,text="select",font=("Bauhaus 93",30,"bold","italic"),command=lambda:plus3("stronger",page,page_2,round))
    B_stronger.grid(row=3,column=column1,columnspan=2)

#第五頁
def moonlight(page,column1,page_2,round,b):
    page5pic1=tk.Label(page,image=tk_imagemoonlight,width="450",height="450")
    page5pic1.grid(row=0,column=column1,padx="40",columnspan=2)
    moonlightplay = Musicplayer(page,"moonlight.mp3",1,b)
    label8 = tk.Label(page,text="Moonlight Sonata",bg="yellow",font=("Bauhaus 93",30,"bold","italic"))
    label8.grid(row=2,column=column1,columnspan=2)
    B_moonlight = tk.Button(page,text="select",font=("Bauhaus 93",30,"bold","italic"),command=lambda:last_plus("moonlight",page,page_2,round))
    B_moonlight.grid(row=3,column=column1,columnspan=2)

def lost(page,column1,page_2,round,b):
    page5pic2=tk.Label(page,image=tk_imagelost_in_a_wave,width="450",height="450")
    page5pic2.grid(row=0,column=column1,padx="40",columnspan=2)
    lostplay = Musicplayer(page,"lost_in_a_wave.mp3",1,b)
    label9 = tk.Label(page,text="Lost In The Wave",bg="yellow",font=("Bauhaus 93",30,"bold","italic"))
    label9.grid(row=2,column=column1,columnspan=2)
    B_lost = tk.Button(page,text="select",font=("Bauhaus 93",30,"bold","italic"),command=lambda:last_plus("lost",page,page_2,round))
    B_lost.grid(row=3,column=column1,columnspan=2)


def moonlight2_1(page,column1,page_2,round,b):
    page5pic1=tk.Label(page,image=tk_imagemoonlight,width="450",height="450")
    page5pic1.grid(row=0,column=column1,padx="40",columnspan=2)
    moonlightplay = Musicplayer(page,"moonlight.mp3",1,b)
    label8 = tk.Label(page,text="Moonlight Sonata",bg="yellow",font=("Bauhaus 93",30,"bold","italic"))
    label8.grid(row=2,column=column1,columnspan=2)
    B_moonlight = tk.Button(page,text="select",font=("Bauhaus 93",30,"bold","italic"),command=lambda:last_plus2("moonlight",page,page_2,round))
    B_moonlight.grid(row=3,column=column1,columnspan=2)

def lost2_1(page,column1,page_2,round,b):
    page5pic2=tk.Label(page,image=tk_imagelost_in_a_wave,width="450",height="450")
    page5pic2.grid(row=0,column=column1,padx="40",columnspan=2)
    lostplay = Musicplayer(page,"lost_in_a_wave.mp3",1,b)
    label9 = tk.Label(page,text="Lost In The Wave",bg="yellow",font=("Bauhaus 93",30,"bold","italic"))
    label9.grid(row=2,column=column1,columnspan=2)
    B_lost = tk.Button(page,text="select",font=("Bauhaus 93",30,"bold","italic"),command=lambda:last_plus2("lost",page,page_2,round))
    B_lost.grid(row=3,column=column1,columnspan=2)

def moonlight3(page,column1,page_2,round,b):
    page5pic1=tk.Label(page,image=tk_imagemoonlight,width="450",height="450")
    page5pic1.grid(row=0,column=column1,padx="40",columnspan=2)
    moonlightplay = Musicplayer(page,"moonlight.mp3",1,b)
    label8 = tk.Label(page,text="Moonlight Sonata",bg="yellow",font=("Bauhaus 93",30,"bold","italic"))
    label8.grid(row=2,column=column1,columnspan=2)
    B_moonlight = tk.Button(page,text="select",font=("Bauhaus 93",30,"bold","italic"),command=lambda:plus3("moonlight",page,page_2,round))
    B_moonlight.grid(row=3,column=column1,columnspan=2)

def lost3(page,column1,page_2,round,b):
    page5pic2=tk.Label(page,image=tk_imagelost_in_a_wave,width="450",height="450")
    page5pic2.grid(row=0,column=column1,padx="40",columnspan=2)
    lostplay = Musicplayer(page,"lost_in_a_wave.mp3",1,b)
    label9 = tk.Label(page,text="Lost In The Wave",bg="yellow",font=("Bauhaus 93",30,"bold","italic"))
    label9.grid(row=2,column=column1,columnspan=2)
    B_lost = tk.Button(page,text="select",font=("Bauhaus 93",30,"bold","italic"),command=lambda:plus3("lost",page,page_2,round))
    B_lost.grid(row=3,column=column1,columnspan=2)

def nothing(a):
    a=a+1
    pass
def round_2(n):
    selection2.append(n)

def round_2_1(n):
    selection2.append(n)
    round3()

def round_3(n):
    selection3.append(n)
    ending()

def round2():
    print(selection)
    #page6
    if selection[0] == "lemon":
        lemon2(page6,0,page7,nothing(1),0)
    elif selection[0] == "entersandman":
        entersandman2(page6,0,page7,nothing(1),0)
    elif selection[0] == "countryroad":
        countryroad2(page6,0,page7,nothing(1),0)
    elif selection[0] == "spectre":
        spectre2(page6,0,page7,nothing(1),0)
    elif selection[0] == "firstnote":
        firstnote2(page6,0,page7,nothing(1),0)
    elif selection[0] == "stronger":
        stronger2(page6,0,page7,nothing(1),0)


    if selection[1] == "entersandman":
        entersandman2(page6,2,page7,nothing(1),2)
    elif selection[1] == "countryroad":
        countryroad2(page6,2,page7,nothing(1),2)
    elif selection[1] == "spectre":
        spectre2(page6,2,page7,nothing(1),2)
    elif selection[1] == "firstnote":
        firstnote2(page6,2,page7,nothing(1),2)
    elif selection[1] == "stronger":
        stronger2(page6,2,page7,nothing(1),2)

    #page7
    if selection[2] == "countryroad":
        countryroad2_1(page7,0,page8,round3,0)
    elif selection[2] == "spectre":
        spectre2_1(page7,0,page8,round3,0)
    elif selection[2] == "firstnote":
        firstnote2_1(page7,0,page8,round3,0)
    elif selection[2] == "stronger":
        stronger2_1(page7,0,page8,round3,0)
    elif selection[2] == "moonlight":
        moonlight2_1(page7,0,page8,round3,0)
    elif selection[2] == "lost":
        lost2_1(page7,0,page8,round3,0)
    
    if selection[3] == "spectre":
        spectre2_1(page7,2,page8,round3,2)
    elif selection[3] == "firstnote":
        firstnote2_1(page7,2,page8,round3,2)
    elif selection[3] == "stronger":
        stronger2_1(page7,2,page8,round3,2)
    elif selection[3] == "moonlight":
        moonlight2_1(page7,2,page8,round3,2)
    elif selection[3] == "lost":
        lost2_1(page7,2,page8,round3,2)
    
    print("2.1.",selection2)

def round3():
    
    if selection2[0] == "lemon":
        lemon3(page8,0,page9,ending,0)
    elif selection2[0] == "entersandman":
        entersandman3(page8,0,page9,ending,0)
    elif selection2[0] == "countryroad":
        countryroad3(page8,0,page9,ending,0)
    elif selection2[0] == "spectre":
        spectre3(page8,0,page9,ending,0)
    elif selection2[0] == "firstnote":
        firstnote3(page8,0,page9,ending,0)
    elif selection2[0] == "stronger":
        stronger3(page8,0,page9,ending,0)
    elif selection2[0] == "moonlight":
        moonlight3(page8,0,page9,ending,0)
    elif selection2[0] == "lost":
        lost3(page8,0,page9,ending,0)

    if selection2[1] == "entersandman":
        entersandman3(page8,2,page9,ending,2)
    elif selection2[1] == "countryroad":
        countryroad3(page8,2,page9,ending,2)
    elif selection2[1] == "spectre":
        spectre3(page8,2,page9,ending,2)
    elif selection2[1] == "firstnote":
        firstnote3(page8,2,page9,ending,2)
    elif selection2[1] == "stronger":
        stronger3(page8,2,page9,ending,2)
    elif selection2[1] == "moonlight":
        moonlight3(page8,2,page9,ending,2)
    elif selection2[1] == "lost":
        lost3(page8,2,page9,ending,2)
    

def ending():
    text1 = "根據測驗，您最喜歡的音樂風格是\n"
    page9.pack()
    if selection3[0] == "lemon":
        text2 = "流行(pop)"
        label2 = tk.Label(page9,text=text1,fg="black",width="1060",
                  height="15",font=("Bauhaus 93",18,"bold","italic"))
        label3 = tk.Label(page9,text=text2,bg="yellow",fg="black",width="1060",
                  height="10",font=("Bauhaus 93",30,"bold","italic"))
        label2.pack()
        label3.pack()
    elif selection3[0] == "entersandman":
        text2 = "搖滾(rock)"
        label2 = tk.Label(page9,text=text1,fg="black",width="1060",
                  height="15",font=("Bauhaus 93",18,"bold","italic"))
        label3 = tk.Label(page9,text=text2,bg="yellow",fg="black",width="1060",
                  height="10",font=("Bauhaus 93",30,"bold","italic"))
        label2.pack()
        label3.pack()
    elif selection3[0] == "countryroad":
        text2 = "民謠(folk)"
        label2 = tk.Label(page9,text=text1,fg="black",width="1060",
                  height="15",font=("Bauhaus 93",18,"bold","italic"))
        label3 = tk.Label(page9,text=text2,bg="yellow",fg="black",width="1060",
                  height="10",font=("Bauhaus 93",30,"bold","italic"))
        label2.pack()
        label3.pack()
    elif selection3[0] == "spectre":
        text2 = "電子(electronic)"
        label2 = tk.Label(page9,text=text1,fg="black",width="1060",
                  height="15",font=("Bauhaus 93",18,"bold","italic"))
        label3 = tk.Label(page9,text=text2,bg="yellow",fg="black",width="1060",
                  height="10",font=("Bauhaus 93",30,"bold","italic"))
        label2.pack()
        label3.pack()
    elif selection3[0] == "firstnote":
        text2 = "爵士(jazz)"
        label2 = tk.Label(page9,text=text1,fg="black",width="1060",
                  height="15",font=("Bauhaus 93",18,"bold","italic"))
        label3 = tk.Label(page9,text=text2,bg="yellow",fg="black",width="1060",
                  height="10",font=("Bauhaus 93",30,"bold","italic"))
        label2.pack()
        label3.pack()
    elif selection3[0] == "stronger":
        text2 = "饒舌(rap)"
        label2 = tk.Label(page9,text=text1,fg="black",width="1060",
                  height="15",font=("Bauhaus 93",18,"bold","italic"))
        label3 = tk.Label(page9,text=text2,bg="yellow",fg="black",width="1060",
                  height="10",font=("Bauhaus 93",30,"bold","italic"))
        label2.pack()
        label3.pack()
    elif selection3[0] == "moonlight":
        text2 = "古典(classical)"
        label2 = tk.Label(page9,text=text1,fg="black",width="1060",
                  height="15",font=("Bauhaus 93",18,"bold","italic"))
        label3 = tk.Label(page9,text=text2,bg="yellow",fg="black",width="1060",
                  height="10",font=("Bauhaus 93",30,"bold","italic"))
        label2.pack()
        label3.pack()
    elif selection3[0] == "lost":
        text2 = "金屬(metal)"
        label2 = tk.Label(page9,text=text1,fg="black",width="1060",
                  height="15",font=("Bauhaus 93",18,"bold","italic"))
        label3 = tk.Label(page9,text=text2,bg="yellow",fg="black",width="1060",
                  height="10",font=("Bauhaus 93",30,"bold","italic"))
        label2.pack()
        label3.pack()


 
lemon(page2,0,page3,nothing(0),0)
entersandman(page2,2,page3,nothing(0),2)
countryroad(page3,0,page4,nothing(0),0)
spectre(page3,2,page4,nothing(0),2)
firstnote(page4,0,page5,nothing(0),0)
stronger(page4,2,page5,nothing(0),2)
moonlight(page5,0,page6,round2,0)
lost(page5,2,page6,round2,2)

        
    

    


root.mainloop()



