# print("hello world")


# def authorize(username, password):
#     if username=="student" and password=="123":
#         print("welcome")
#     else:
#         print("wrong username or password")

# username=input("enter username: ")
# password=input("enter password: ")

# authorize(username,password)


# import tkinter as tk
# from tkinter import messagebox

# Create the main window
# root = tk.Tk()
# root.title("Login Application")
# root.geometry("400x300")

# # Function to clear the current screen
# def clear_screen():
#     for widget in root.winfo_children():
#         widget.destroy()

# # Function to display the second screen
# def home_screen(username):
#     clear_screen()

#     tk.Label(
#         root,
#         text=f"Welcome, {username}!",
#         font=("Arial", 20)
#     ).pack(pady=40)

#     tk.Label(
#         root,
#         text="You have successfully logged in!"
#     ).pack(pady=10)

#     tk.Button(
#         root,
#         text="Logout",
#         command=login_screen
#     ).pack(pady=20)

# # Function to check login credentials
# def login():
#     username = username_entry.get()
#     password = password_entry.get()

#     if username == "admin" and password == "1234":
#         home_screen(username)
#     else:
#         messagebox.showerror(
#             "Login Failed",
#             "Incorrect username or password"
#         )

# # Function to display the login screen
# def login_screen():
#     global username_entry, password_entry

#     clear_screen()

#     tk.Label(
#         root,
#         text="Login",
#         font=("Arial", 24)
#     ).pack(pady=20)

#     tk.Label(root, text="Username").pack()
#     username_entry = tk.Entry(root)
#     username_entry.pack(pady=5)

#     tk.Label(root, text="Password").pack()
#     password_entry = tk.Entry(root, show="*")
#     password_entry.pack(pady=5)

#     tk.Button(
#         root,
#         text="Login",
#         command=login
#     ).pack(pady=20)

# # Start on the login screen
# login_screen()

# # Run the application
# root.mainloop()

# import tkinter as tk

# class Login:
#     def __init__(self, root, show_home):
#         self.frame = tk.Frame(root)

#         self.label = tk.Label(self.frame, text="Log in")
#         self.label.pack()
#         self.username=tk.StringVar()
#         self.password=tk.StringVar()

#         name_label = tk.Label(self.frame, text = 'Username', font=('calibre',10, 'bold'))
#         name_label.pack()
#         # creating a entry for input
#         # name using widget Entry
#         name_entry = tk.Entry(self.frame,textvariable = self.username, font=('calibre',10,'normal'))
#         name_entry.pack()
#         # creating a label for password
#         passw_label = tk.Label(self.frame, text = 'Password', font = ('calibre',10,'bold'))
#         passw_label.pack()
#         # creating a entry for password
#         passw_entry=tk.Entry(self.frame, textvariable = self.password, font = ('calibre',10,'normal'), show = '*')
#         passw_entry.pack()
#         # creating a button using the widget 
#         # Button that will call the submit function 
#         self.button=tk.Button(self.frame,text = 'Submit', command = show_home) #shpw home should be the suthenticate function

#         self.button.pack()
 
 
#     def authenticate(self):
#         if(self.username=='student' and self.password=='123'):
#             return True
#         else:
#             return False
#     def show(self):
#         self.frame.pack()

#     def hide(self):
#         self.frame.pack_forget()


# class Home:
#     def __init__(self, root, show_login):
#         self.frame = tk.Frame(root)

#         self.label = tk.Label(self.frame, text="Home")
#         self.label.pack()

#         self.button = tk.Button(
#             self.frame,
#             text="Back",
#             command=show_login
#         )
#         self.button.pack()

#     def show(self):
#         self.frame.pack()

#     def hide(self):
#         self.frame.pack_forget()


# # Main application
# root = tk.Tk()
# root.geometry("400x300")

# def show_home():
#     login.hide()
#     home.show()

# def show_login():
#     home.hide()
#     login.show()

# login = Login(root, show_home)

# home = Home(root, show_login)


# login.show()

# root.mainloop()

class refill():
    print


# class User:

#     def __init__(self, name, password, role):
#         self.name=name
#         self.password=password
#         self.role=role
        

#     def auth_user(u):
#         n=0
#         check=False
#         while n<len(users) and check==False:
#             if users[n].name!=u:
#                 n+=1
#             else:
#                 check=True
#         return(check)

#     def auth_pass(u,p):
#         i=0
#         check=False
#         while i<len(users) and i!=-1:
#             if u==users[i].name:
#                 u_p=users[i].password
#                 i=-1
#             else:
#                 i+=1
#         if i==len(users):
#             print("Username doesn't exist")
#         else:
#             if u_p==p:
#                 check=True
#         return(check)

#     def auth_role(u):
#         i=0
#         check=False
#         while i<len(users) and i!=-1:
#             if u==users[i].name:
#                 u_r=users[i].role
#                 i=-1
#             else:
#                 i+=1
#         if i==len(users):
#             print("User doesn't exist")
#         else:
#             return(u_r)

        

#     def funcs(role):
#         choice=""
#         i=""
#         if role == "d" or role == "n":
#             choice=input ("Choose a function.\na) View ADC info\nb) Exit\n")
#             if choice=="a" or choice=="A":
#                 i="ADC"
#             elif choice=="b" or choice=="B":
#                 i="Exit"
#             else:
#                 i="None"
#         if role == "t":
#             choice=input ("Choose a function.\na) View ADC info\nb) Alarms\nc) Exit\n")
#             if choice=="a" or choice=="A":
#                 i="ADC"
#             elif choice=="b" or choice=="B":
#                 i="Alarms"
#             elif choice=="c" or choice=="C":
#                 i="Exit"
#             else:
#                 i="None"
#         if role == "p":
#             choice=input ("Choose a function.\na) View ADC info\nb) Hospital Inventory\nc) Exit\n")
#             if choice=="a" or choice=="A":
#                 i="ADC"
#             elif choice=="b" or choice=="B":
#                 i="Inv"
#             elif choice=="c" or choice=="C":
#                 i="Exit"
#             else:
#                 i="None"
#         if role == "a":
#             choice=input ("Choose a function.\na) View ADC info\nb) Alarms\nc) History\nd) Generate\ne) Hospital Inventory\nf) Exit\n")
#             if choice=="a" or choice=="A":
#                 i="ADC"
#             elif choice=="b" or choice=="B":
#                 i="Alarms"
#             elif choice=="c" or choice=="C":
#                 i="History"
#             elif choice=="d" or choice=="D":
#                 i="Report"
#             elif choice=="e" or choice=="E":
#                 i="Inv"
#             elif choice=="f" or choice=="F":
#                 i="Exit"
#             else:
#                 i="None"

#         if i=="ADC":
#             print ("Viewing ADC\n")
#             return(0)
#         if i=="Alarms":
#             print ("Viewing alarms\n")
#             return(0)
#         if i=="History":
#             print("Viewing history\n")
#             return(0)
#         if i=="Report":
#             print("Viewing report\n")
#             return(0)
#         if i=="Inv":
#             print("Viewing inventory\n")
#             return(0)
#         if i=="Exit":
#             print("Exiting\n")
#             return(1)
#         if i=="" or i=="None":
#             print("Please input the letter next to the desired function")
#             return(0)


            

class authenticate:
    def __init__(self):
        self.users=[("nurse", "Vania23", "1234"), 
                    ("pharmacist", "Karman45", "5678"),
                    ("technician", "Anushka12", "1010"),
                    ("admin", "Owen11", "0000")
                    ]

  
    def authenticate(self):
        attempt=0
        while attempt<3:
            username=input("Enter username: ")
            password=input("Enter password: ")
            auth_role=None
            for role,user,user_pass in self.users:
                    if username==user and password==user_pass:
                            auth_role= role
                            break
              
        
            if auth_role is not None:
                print(f"Login successful! Role: {auth_role}")
                return auth_role
            else:
                    print(f"invalid log in. Attempts remaining: {2-attempt}")
                    attempt+=1
     
        print("You have reached max attempts, try again in 20 minutes")
        return None

class dispense():
    print

class maintaince():
    print

class login(): #using tkinter library later on
    print('terminal')

class inventory():
    def __init__(self):
        self.medications = {
            1: {"name": "Acetaminophen", "quantity":30},
            2: {"name": "Aspirin", "quantity":30},
            3: {"name": "Ibuprofen", "quantity":40},
            4: {"name": "Cefazolin", "quantity":20},
            5: {"name": "Alprazolam", "quantity":28},
            6: {"name": "Albuterol", "quantity":33},
            7: {"name": "Bisacodyl", "quantity":15},
            8: {"name": "Famotidine", "quantity":24},
            9: {"name": "Zolpidem", "quantity":35},
            10: {"name": "Diphenhydramine", "quantity":40},
            11: {"name": "Methocarbamol", "quantity":39},
            12: {"name": "Ondansetron", "quantity":45},
            13: {"name": "Gabapentin", "quantity":23},
            14: {"name": "Fentanyl", "quantity":36},
            15: {"name": "Oxycodone", "quantity":19},
            16: {"name": "Hydromorphone", "quantity":24},

        }
    def display_inventory(self):
        print("ID | Medication | Quantity")
        print("--------------------------")
        for ID, medication in self.medications.items():
            print(f"{ID}  |  {medication['name']} | {medication['quantity']}")

    def get_medication_name(self,medication_id):
        if medication_id in self.medications:
            return self.medications[medication_id]["name"]
        else:
            return "Medication not found"
    def get_medication_quantity(self,medication_id):
        if medication_id in self.medications:
            return self.medications[medication_id]["quantity"]
        else:
            return "Medication not found"
        
    def add_stock(self,ID,quantity):
        confirm=input(f"Is this the medication you want to refill? (y/n) {self.medications[ID]['name']}: ")
        if confirm=="y":
            self.medications[ID]["quantity"]+=quantity
            return True
        else:
            return False


class eventlog():
    print()

class comms():
    print()

class fault():
    print()

class hardware():
    print()

def main():

    stock = inventory()
    auth=authenticate()
    role=auth.authenticate()

    if role is not None:
        while True:
                stock.display_inventory()
                id=int(input("enter id to refill: "))
                quant=int(input("enter quanitity: "))
                stock.add_stock(id,quant)
                print(f"{stock.get_medication_name(id)}")
                print(f"{stock.get_medication_quantity(id)}")
                state=input("Would you like to exit? (y/n)")
                if state=="y":
                    break

        
    
if __name__=="__main__":
    main()
