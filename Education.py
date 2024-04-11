from tkinter import *
import time
import sqlite3

count = 0
text = ''

def slide():
    global text, count
    if count == len(s):
        count = 0
        text = ''
    text = text + s[count]
    slideLabel.config(text=text)
    count += 1
    slideLabel.after(200, slide)

def clock():
    date = time.strftime('%d/%m/%Y')
    current_time = time.strftime('%H:%M:%S')
    datetimeLabel.config(text=f"   Date: {date}\nTime: {current_time}")
    window.after(1000, clock)

def connect_to_database():
    try:
        connection = sqlite3.connect('student_database.db')
        cursor = connection.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS students (
                            id INTEGER PRIMARY KEY,
                            name TEXT,
                            age INTEGER,
                            grade TEXT
                          )''')
        connection.commit()
        connection.close()
        print("Connected to the database successfully!")
    except sqlite3.Error as error:
        print("Error connecting to the database:", error)

window = Tk()
window.geometry('1244x700+0+0')
window.title('Student Management System')

datetimeLabel = Label(window, font=('times new Roman', 12, 'bold'))
datetimeLabel.place(x=5, y=5)

clock()

s = 'Student Management System'
slideLabel = Label(window, text=s, font=('Arial', 28, 'bold'))
slideLabel.place(x=200, y=0)
slide()

connectButton = Button(window, text='Connect Database', command=connect_to_database)
connectButton.place(x=980, y=0)

window.mainloop()

