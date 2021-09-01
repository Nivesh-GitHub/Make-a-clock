import time
import tkinter #For module (pre installed)
import sys #to import system files (pre installed)
from tkinter import *   #whole module is imported
from tkinter import font #importing local time
#Used to display time on the label
def DClock():
    curr_time= time.strftime("%H:%M:%S") #Time 
    clock.config(text=curr_time)
    clock.after(100,DClock)
#making window
window=Tk() #Screen
window.title('Clock') #Title
#Art is from line 13 to 18
message= Label(window, font=("arial",100,"italic"), text="Time", fg="red")
message.grid(row=0,column=0)
clock= Label(window, font=("Clock",150,"bold"),fg="dark blue")
clock.grid(row=2,column=5)
DClock()
mainloop() #loop is closed
#Clock has been made
