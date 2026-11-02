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




import random
import sqlite3
from datetime import datetime

class authenticate:
    def __init__(self):
        self.users=[("nurse", "vania23", "1234"), 
                    ("pharmacist", "karman45", "5678"),
                    ("technician", "anushka12", "1010"),
                    ("admin", "owen11", "0000")
                    ]
        self.event_log = eventlog_object
        self.current_username = None
  
    def authenticate(self):
        attempt=0
        while attempt<3:
            username=input("Enter username: ").lower()
            password=input("Enter password: ").lower()
            auth_role=None
            for role,user,user_pass in self.users:
                    if username==user and password==user_pass:
                            auth_role= role
                            break
              
        
            if auth_role is not None:
                self.current_username = username
                print(f"\nLogin successful! Role: {auth_role}")
                self.event_log.add_event(
                    "LOGIN",
                    username, 
                    details = f"{auth_role} logged into the ADC."
                )
                return auth_role
            else:
                    attempt +=1
                    print(f"Invalid log in. Attempts remaining: {3-attempt}")

                    self.event_log.add_event(
                        "LOGIN FAILED",
                        username, 
                        details = "Invalid username or password."
                    )
                
     
        print("You have reached max attempts, try again in 20 minutes")
        return None


class maintaince():
    def __init__(self, fault_object):
        self.fault_system=fault_object

    def clear_faults(self):
        for item in self.fault_system.faults:
            if item['status']=='Active':
                item['status']='Resolved'
        print("All active faults marked as resolved")

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
        print("\nID | Medication | Quantity")
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

    # used by the refill class
    def add_stock(self,medication_id,quantity):
        if medication_id not in self.medications or quantity<=0:
            return False
        else:
            self.medications[medication_id]["quantity"] += quantity
            return True
    
    #used by the dispense class
    def remove_stock(self, medication_id, quantity):
        if medication_id not in self.medications or quantity <=0:
            return False
        if self.medications[medication_id]["quantity"] < quantity:
            return False
        else:
            self.medications[medication_id]["quantity"]-=quantity
            return True


class eventlog():
    def __init__(self, database_name = "adc_events.db"):
        self.__database_name = database_name
        self.__connection = sqlite3.connect(self.__database_name)

        self.__connection.execute("""
        CREATE TABLE IF NOT EXISTS events(
        event_id INTEGER PRIMARY KEY AUTOINCREMENT,
        event_type TEXT,
        username TEXT, 
        medication_id INTEGER,
        medication_name TEXT, 
        quantity INTEGER, 
        details TEXT, 
        timestamp TEXT
        )
        """)

        columns = {
            row[1]
            for row in self.__connection.execute(
                "PRAGMA table_info(events)"
            )
        }

        if "medication_name" not in columns:
            self.__connection.execute(
                "ALTER TABLE events ADD COLUMN medication_name TEXT"
            )
        self.__connection.commit()

    def add_event(
            self,
            event_type, 
            username,
            medication_id = None, 
            medication_name = None, 
            quantity = None, 
            details = ""
    ):
        timestamp = datetime.now().isoformat(timespec="seconds")

        self.__connection.execute("""
        INSERT INTO events(
        event_type, 
        username, 
        medication_id, 
        medication_name,
        quantity, 
        details, 
        timestamp
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            event_type,
            username, 
            medication_id,
            medication_name,
            quantity,
            details,
            timestamp
        ))

        self.__connection.commit()

    def display_log(self, limit=10):
        cursor = self.__connection.execute("""
        SELECT * 
        FROM events 
        ORDER BY event_id DESC 
        LIMIT ?
        """, (limit,))


        events = cursor.fetchall()

        print("\nLast 10 Event Entries")
        print("-"*75)

        if not events:
            print ("No events recorded.")
            return

        for event in events:
            print(
                f"Event ID: {event[0]} |"
                f"Type: {event[1]} |"
                f"User: {event[2]}"
            )

            print(
                f"Medication: {event[4] or 'N/A'} |"
                f"Quantity: {event[5] if event[5] is not None else 'N/A'}"
            )

            print(f"Details: {event[6]}")
            print(f"Time: {event[7]}")
            print("-"*75)

    def close(self):
        self.__connection.close()





class refill():
    def __init__(self, inventory_object, eventlog_object):
        self.inventory = inventory_object
        self.event_log = eventlog_object

    def refill_medication (self, medication_id, quantity, username):

        if medication_id not in self.inventory.medications:
            print("Invalid medication ID. ")
            return False
        
        if quantity <=0:
            print("Quantity must be greater than zero. ")
            return False
        
        medication_name = self.inventory.get_medication_name(
            medication_id
        )

        confirm = input(
            f"Confirm refill or {medication_name}? (y/n):"
        ).lower()

        if confirm !="y":
            print ("Refill cancelled.")
            return False

        self.inventory.add_stock(medication_id, quantity)

        self.event_log.add_event(
            "REFILL", 
            username,
            medication_id, 
            medication_name, 
            quantity,
            "Medication inventory replenished."
        )

        print("\n Refill successfull!")
        print(
            f"Updated quantity:"
            f"{self.inventory.get_medication_quantity(medication_id)}"
        )

        return True


    
    
class dispense():
    def __init__(self, inventory_object, eventlog_object, maintenance_object):
        self.inventory = inventory_object
        self.event_log = eventlog_object
        self.maintenance = maintenance_object

    def dispense_medication (self, medication_id, quantity, username):
        if self.maintenance.is_active:
            print("Dispensing unavailable. ADC is in maintenance mode.")
            return False
        
        
        if medication_id not in self.inventory.medications:
            print("Invalid medication ID.")
            return False
        
        if quantity <=0:
            print("Quantity must be greater than 0.")
            return False

        medication_name = self.inventory.get_medication_name(
            medication_id
        )

        available = self.inventory.get_medication_quantity(
            medication_id
        )

        if available < quantity:
            print(f"Low stock. Available quantity: {available}")
            return False

        confirm = input(
            f"Confirm dispensing {quantity} units of " f"{medication_name}? (y/n)"
        ).lower()

        if confirm !="y":
            print("Dispensing cancelled.")
            return False

        self.inventory.remove_stock(medication_id, quantity)

        self.event_log.add_event(
            "DISPENSE", 
            username, 
            medication_id, 
            medication_name,
            quantity, 
            "Medication successfully dispensed. "
        )

        print ("\nDispensing successful!")
        print(f"Remaining quantity: " f"{self.inventory.get_medication_quantity(medication_id)}")

        return True




class comms():
    print()

from datetime import datetime






class fault():
    def __init__(self):
        self.faults=[]
    def add_fault(self,description):
        new_fault={
            "id" : len(self.faults)+1,
            "description" : description,
            "time" : datetime.now().isoformat(timespec="seconds"),
            "status" : "Active"
        }
        self.faults.append(new_fault)
        print("Fault detected and logged")
    def display_faults(self):
        for item in self.faults:
            print(
                f"{item['id']} | {item['description']} | "
                f"{item['status']} | {item['time']}"
            )

        
    print()

class hardware():
    print()

def main():

    stock = inventory()
    auth=authenticate()
    role=auth.authenticate()
    faults=fault()
    maintaince_system=maintaince(faults)
    if role is not None:
        while True:
                print("\n1. Display Inventory")
                print("2. Refill Medication")
                print("3. Dispense Medication")
                print("4. View Faults")
                print("5. Perform Maintenance")
                print("6. Exit")
                choice = int(input("Select an option: "))
                if choice==1:
                    stock.display_inventory()
                elif choice==2:

                    id=int(input("enter id to refill: "))
                    quant=int(input("enter quanitity: "))
                    success=stock.add_stock(id,quant)
                    print(f"{stock.get_medication_name(id)}")
                    print(f"{stock.get_medication_quantity(id)}")
                    if success:
                        number = random.randint(1,10)
                        print(f"number generated: {number}")
                        if number==5:
                            faults.add_fault("Drawer malfunction")
                #choice equals 3
                elif choice==4:
                    if role == 'technician' or role =='admin':
                        faults.display_faults()
                    else:
                        print("You are not authorized to view the faults")
                elif choice==5:
                    if role == 'technician':
                        maintaince_system.clear_faults()
                    else:
                        print("You are not autherized to perform maintainence")
                        
                elif choice==6:
                    break

        
    
if __name__=="__main__":
    main()
