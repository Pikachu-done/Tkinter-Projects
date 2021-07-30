# Alarm Clock

from tkinter import *
import datetime
import time
from playsound import playsound

def alarm(set_alarm_timer):
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        date = current_time.strftime("%d/%m/%Y")
        print("The Set Date is:",date)
        print(now)
        if now == set_alarm_timer:
            print("Time to Wake up")
            playsound("sound.mp3")
            break

def actual_time():
    set_alarm_timer = f"{hour.get()}:{min.get()}:{sec.get()}"
    alarm(set_alarm_timer)

clock = Tk()

clock.title("DataFlair Alarm Clock")
clock.geometry("400x200")
clock.config(bg = 'black')

time_format=Label(clock, text= "Enter time in 24 hour format!",relief = 'solid',fg="red",bg="black",font="Arial").place(x=80,y=160)
addTime = Label(clock,text = "Hour   Min    Sec",font=(110)).place(x = 110)
setYourAlarm = Label(clock,text = "When to wake you up",fg="blue",relief = "solid",font=("Helevetica",14,"bold")).place(x=80, y=70)

# The Variables we require to set the alarm(initialization):
hour = StringVar()
min = StringVar()
sec = StringVar()

#Time required to set the alarm clock:
hourTime= Entry(clock,textvariable = hour,bg = "green",width = 4,font = ('arial',10,'bold')).place(x=109,y=30)
minTime= Entry(clock,textvariable = min,bg = "green",width = 4,font = ('arial',10,'bold')).place(x=153,y=30)
secTime = Entry(clock,textvariable = sec,bg = "green",width = 4,font = ('arial',10,'bold')).place(x=197,y=30)

#To take the time input by user:
submit = Button(clock,text = "Set Alarm",fg="red",width = 10,font = ('arial',10,'bold'),command = actual_time).place(x =130,y=120)

clock.mainloop()
