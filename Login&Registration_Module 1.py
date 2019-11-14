from tkinter import *
from tkinter import Toplevel

MainScreen = Tk() #This is how you create Windows
MainScreen.title("MainScreen")
MainScreen.geometry("200x200")

def exit_login():
    LoginScreen.destroy()
def exit_signup():
    SignUpScreen.destroy()

def Login():
    MainScreen.destroy()
    global LoginScreen
    LoginScreen = Tk()
    LoginScreen.title("LOGIN")

    username = Label(LoginScreen, text="USER NAME")
    password = Label(LoginScreen, text="PASSWORD")

    username_entry = Entry(LoginScreen, text="Enter Username")
    password_entry = Entry(LoginScreen, text="Enter Password")

    username.grid(row=0, column=0)
    password.grid(row=1, column=0)
    username_entry.grid(row=0, column=1)
    password_entry.grid(row=1, column=1)

    login = Button(LoginScreen, text="LOGIN", fg="red")
    login.grid(row=3, column=3)
    Exit = Button(LoginScreen, text="EXIT", fg="red", command=exit_login)
    Exit.grid(row=3, column=4)

    LoginScreen.mainloop()

def SignUp():
    MainScreen.destroy()
    global SignUpScreen

    SignUpScreen = Tk()
    SignUpScreen.title("SIGNUP")

    create_username = Label(SignUpScreen, text="CREATE USER NAME")
    create_password = Label(SignUpScreen, text="CREATE PASSWORD")
    re_password = Label(SignUpScreen, text="RE-ENTER PASSWORD")

    username_entry = Entry(SignUpScreen, textvariable = u)
    password_entry = Entry(SignUpScreen, textvariable = p)
    re_password_entry = Entry(SignUpScreen)

    create_username.grid(row=0, column=0)
    create_password.grid(row=1, column=0)
    re_password.grid(row=2, column=0)
    username_entry.grid(row=0, column=1)
    password_entry.grid(row=1, column=1)
    re_password_entry.grid(row=2, column=1)

    signup = Button(SignUpScreen, text="SIGN UP", fg="red", command = Sign_up_file)
    signup.grid(row = 3, column = 3)
    Exit = Button(SignUpScreen, text="EXIT", fg="red", command = exit_signup)
    Exit.grid(row=3, column=4)

    SignUpScreen.mainloop()

Login_button = Button(MainScreen, text = "OLD USER", fg = "red", command = Login)
SignUp_button = Button(MainScreen, text  = "NEW USER", fg = "blue", command = SignUp)

Login_button.grid(row = 0, column = 0)
SignUp_button.grid(row = 0, column = 1)

MainScreen.mainloop()
