from tkinter import *
from datetime import datetime
from datetime import date

bc = "white"
fc = "blue"

window = Tk()
window.title("Digital Clock")
window.geometry("440x180")
window.resizable(width=False,height=False)
window.configure(bg=bc)

def clock():
    time = datetime.now()
    hour = time.strftime("%H:%M:%S")
    date_now = date.today()
    weekday = time.strftime("%A")

    l1.config(text=hour)
    l1.after(200, clock)
    l2.config(text=weekday + " " + str(date_now))

l1 = Label(window, text="hour", font=("Times 80"), bg=bc)
l1.grid(row=0, column=0, padx=5)

l2 = Label(window, text="weekday, date_now", font=("Times 20"), bg=bc)
l2.grid(row=1, column=0)

clock()

window.mainloop()