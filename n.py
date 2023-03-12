from tkinter import *
from tkinter import messagebox
import os
import tkinter as tk
from tkinter import ttk
tk=Tk()
tk.title("TheYusa")
tk.geometry("530x400")

pb= ttk.Progressbar(tk,orient="horizontal",
                    mode="determinate",
                    length=320)
pb.place(x=2,y=60)

bt2= Button(tk, text="sogula",command=pb.start)
bt2.place(x=300,y=60)

def sorgula():
    pb.start
    window=Toplevel(tk)
    window.title("nmap")
    window.geometry("530x400")
    log=Text(window,width=65,height=20)
    log.place(x=2,y=20)
    log.bind("<Key>", lambda e: "break")
    hedefip=e1.get()

    de=arg.get()

    os.system("nmap -sS {} -oN nmap.txt {}" .format(de,hedefip))
    if os.path.exists("nmap.txt"):
        ac = open("nmap.txt","r")
        icerik=ac.read()
        log.insert(END,icerik)
        pb.stop
    else:
        sorgula()
        os.remove("nmap.txt")
arg=StringVar()

c1 = Checkbutton(tk, text = "443", 
					variable = arg, 
					onvalue = "-p443", 
					offvalue = "",
                    
					)
c1.place(x=0,y=30)

    


l1=Label(tk,text="nmap")
l1.place(x=2,y=10)

e1=Entry(tk)
e1.place(x=50,y=10)

bt= Button(tk, text="sogula",command=sorgula)
bt.place(x=250,y=5)



tk.mainloop()