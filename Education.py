from tkinter import *
import time

def clock():
    date = time.strftime('%d/%m/%Y')
    current_time = time.strftime('%H:%M:%S')
    datetimeLabel.config(text=f"   date: {date}\nTime:{current_time}")  # Update label text
    window.after(1000, clock)  # Update the clock every second

window = Tk()
window.geometry('1244x700+0+0')
window.title('Student Management System')

datetimeLabel = Label(window, font=('times new Roman', 12, 'bold')) 
datetimeLabel.place(x=5, y=5)

clock()  # Start the clock function

window.mainloop()