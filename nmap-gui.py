from tkinter import *
from tkinter import messagebox
import os
import tkinter as tk
from tkinter import ttk
tk=Tk()
tk.title("nmap-gui")
tk.geometry("300x200")
def sorgula():
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
    de4=arg4.get()
    de5=arg5.get()
    os.system("nmap -sS -sV {} {} {} {} {} {} -oN nmap.txt {}".format(de,de1,de2,de3,de4,de5,hedefip))
    if os.path.exists("nmap.txt"):
        ac = open("nmap.txt","r")
        icerik=ac.read()
        log.insert(END,icerik)
    else:
        sorgula()
        os.remove("nmap.txt")


#checkbutton
arg=StringVar()
arg1=StringVar()
arg2=StringVar()
arg3=StringVar()
arg4=StringVar()
arg5=StringVar()
c1 = Checkbutton(tk, text = "T4", 
					variable = arg, 
					onvalue = "-T4", 
					offvalue = "",
                    
					)
c1.place(x=0,y=35)
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

c6 = Checkbutton(tk, text = "script", 
					variable = arg4, 
					onvalue = "-sC", 
					offvalue = "",
                    
					)
c6.place(x=130,y=35)

c7 = Checkbutton(tk, text = "online host", 
					variable = arg5, 
					onvalue = "-Pn", 
					offvalue = "",
                    
					)
c7.place(x=130,y=60)
#label
l1=Label(tk,text="nmap")
l1.place(x=2,y=10)
#veri girisi
e1=Entry(tk,width=20)
e1.place(x=50,y=10)
#sorgula
bt= Button(tk, text="sogula",command=sorgula)
bt.place(x=220,y=5)



tk.mainloop()