from tkinter import *
from tkinter import messagebox

# a function to check and produce error if password and username fields are empty

def login():
    if username_entry.get() == '' or password_entry.get() == '':
        messagebox.showerror('Error', 'Fields cannnot be empty')
    elif username_entry.get() == 'Florence' and password_entry.get() == '1304':
        messagebox.showinfo('Success', 'Welcome')
        window.destroy()
        import Education
       
    else:
        messagebox.showerror('Error', 'Please enter correct credentials')

#creating window of login page

window = Tk()

window.geometry('1244x700+0+0') # the measurements (width and height) of the window the 0s make sure it stars

window.resizable(False, False) #this makes sure that the window cannot be maximized
 
window.title('Student Management System')

back_ground_image = PhotoImage(file='background.jpeg.png') # image path

back_ground_label = Label(window, image = back_ground_image)

back_ground_label.place(x=0, y=0) # this places the image to match the window size

# creating frame for login in details

login_frame = Frame(window, bg= 'white')
login_frame.place(x=500, y=150) #frame size

logo_image = PhotoImage(file='main_user.png')

logo_label = Label(login_frame, image= logo_image)
logo_label.grid(row= 0, column= 0, columnspan= 2, pady= 15) #this places the logo in the login frame column span allows the logo label to take 2 column spaces

# creating login field username

username_image = PhotoImage(file= 'user.png')
username_label = Label(login_frame, image= username_image, text= 'Username', compound=LEFT
                       , font=('times new roman', 16, 'bold'), bg= 'white') # this makes sure that the image, frame , logo and username all appear on the window and gives a font style
username_label.grid(row= 1, column= 0, pady= 15, padx= 20) #this places the image on the window

# creating a space where to type the username using entry class

username_entry = Entry(login_frame, font=('times new roman', 16, 'bold'), bd= 5)
username_entry.grid(row= 1, column= 1, pady=15, padx= 20)

# creating password field and image

password_image = PhotoImage(file= 'padlock.png')
password_label = Label(login_frame, image= password_image, text= 'Password', compound=LEFT
                       , font=('times new roman', 16, 'bold'), bg= 'white') # this makes sure that the image, frame , logo and username all appear on the window and gives a font style
password_label.grid(row= 2, column= 0, pady= 15, padx= 20) #this places the image on the window

# creating a space where to type the password using entry class

password_entry = Entry(login_frame, font=('times new roman', 16, 'bold'), bd= 5)
password_entry.grid(row= 2, column= 1, pady=15, padx= 20)

#creating login button using button class

login_button = Button(login_frame, text= 'Login', font=('times new roman', 16, 'bold'), width= 15
                      , bg= 'green', cursor= 'hand2', command= login)
login_button.grid(row= 3, column= 1, columnspan= 2, pady= 20, padx= 20)

window.mainloop() #keeps window on a loop and shows a window