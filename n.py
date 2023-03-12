from tkinter import *
from tkinter import messagebox
import os
import tkinter as tk
from tkinter import ttk
tk=Tk()
tk.title("TheYusa")
tk.geometry("300x200")
"""
pb= ttk.Progressbar(tk,orient="horizontal",
                    mode="determinate",
                    length=320)
pb.place(x=2,y=60)

bt2= Button(tk, text="sogula",command=pb.start)
bt2.place(x=300,y=60)
"""

def sorgula():
    #pb.start
    window=Toplevel(tk)
    window.title("nmap")
    window.geometry("615x350")
    log=Text(window,width=75,height=20)
    log.pack()
    log.bind("<Key>", lambda e: "break")
    hedefip=e1.get()

    de=arg.get()
    de1=arg1.get()
    de2=arg2.get()
    de3=arg3.get()
    os.system("nmap -sS -sV {} {} {} {} -oN nmap.txt {}".format(de,de1,de2,de3,hedefip))
    if os.path.exists("nmap.txt"):
        ac = open("nmap.txt","r")
        icerik=ac.read()
        log.insert(END,icerik)
        #pb.stop
    else:
        sorgula()
        os.remove("nmap.txt")


#checkbutton
arg=StringVar()
arg1=StringVar()
arg2=StringVar()
arg3=StringVar()
c1 = Checkbutton(tk, text = "T4", 
					variable = arg, 
					onvalue = "-T4", 
					offvalue = "",
                    
					)
c1.place(x=0,y=30)
c4 = Checkbutton(tk, text = "Fast", 
					variable = arg, 
					onvalue = "-F", 
					offvalue = "",
                    
					)
c4.place(x=0,y=60)
c2 = Checkbutton(tk, text = "Top Ports", 
					variable = arg1, 
					onvalue = "--top-ports", 
					offvalue = "",
                    
					)
c2.place(x=0,y=90)
c3 = Checkbutton(tk, text = "OS service", 
					variable = arg2, 
					onvalue = "-A", 
					offvalue = "",
                    
					)
c3.place(x=0,y=120)
c5 = Checkbutton(tk, text = "vuln", 
					variable = arg3, 
					onvalue = "-script vuln", 
					offvalue = "",
                    
					)
c5.place(x=0,y=150)

    
#label
l1=Label(tk,text="nmap")
l1.place(x=2,y=10)
#veri girişi
e1=Entry(tk,width=20)
e1.place(x=50,y=10)
#sorgula
bt= Button(tk, text="sogula",command=sorgula)
bt.place(x=220,y=5)



tk.mainloop()