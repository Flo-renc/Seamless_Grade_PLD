from tkinter import *
import time
count=0
text=''
def slide():
    global text,count
    text=text+s[count]
    slideLabel.config(text=text)
    count+=1
    slideLabel.after(300,slide)

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
s='Student Management System'
slideLabel=Label(window,text=s,font=('Arial',28,'bold'))
slideLabel.place(x=200,y=0)
slide()
window.mainloop()