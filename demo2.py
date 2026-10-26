# print("hello world")


# def authorize(username, password):
#     if username=="student" and password=="123":
#         print("welcome")
#     else:
#         print("wrong username or password")

# username=input("enter username: ")
# password=input("enter password: ")

# authorize(username,password)


import tkinter as tk
from tkinter import messagebox

# Create the main window
root = tk.Tk()
root.title("Login Application")
root.geometry("400x300")

# Function to clear the current screen
def clear_screen():
    for widget in root.winfo_children():
        widget.destroy()

# Function to display the second screen
def home_screen(username):
    clear_screen()

    tk.Label(
        root,
        text=f"Welcome, {username}!",
        font=("Arial", 20)
    ).pack(pady=40)

    tk.Label(
        root,
        text="You have successfully logged in!"
    ).pack(pady=10)

    tk.Button(
        root,
        text="Logout",
        command=login_screen
    ).pack(pady=20)

# Function to check login credentials
def login():
    username = username_entry.get()
    password = password_entry.get()

    if username == "admin" and password == "1234":
        home_screen(username)
    else:
        messagebox.showerror(
            "Login Failed",
            "Incorrect username or password"
        )

# Function to display the login screen
def login_screen():
    global username_entry, password_entry

    clear_screen()

    tk.Label(
        root,
        text="Login",
        font=("Arial", 24)
    ).pack(pady=20)

    tk.Label(root, text="Username").pack()
    username_entry = tk.Entry(root)
    username_entry.pack(pady=5)

    tk.Label(root, text="Password").pack()
    password_entry = tk.Entry(root, show="*")
    password_entry.pack(pady=5)

    tk.Button(
        root,
        text="Login",
        command=login
    ).pack(pady=20)

# Start on the login screen
login_screen()

# Run the application
root.mainloop()
