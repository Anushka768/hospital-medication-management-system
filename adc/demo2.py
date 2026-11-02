import random
import sqlite3
from datetime import datetime

class authenticate:
    def __init__(self, eventlog_object):
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
            password=input("Enter password: ")
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
    def __init__(self, fault_object, eventlog_object):
        self.fault_system=fault_object
        self.event_log = eventlog_object
        self.__active = False

    @property
    def is_active (self):
        return self.__active

    def start_maintenance (self, username):
        if self.__active:
            print ("Maintenance is already active.")
            return
        self.__active = True

        print("Maintenance mode enabled.")

        self.event_log.add_event(
            "MAINTENANCE START", 
            username, 
            details = "ADC entered maintenance mode."
        )

    def end_maintenance(self, username):
        if not self.__active:
            print("Maintenance is not currently active")
            return
        self.__active = False

        print("Maintenance more disabled")

        self.event_log.add_event(
            "MAINTENANCE END", 
            username,
            details = "ADC exited maintenance mode."
        )



    def clear_faults(self, username):
        if not self.__active:
            print("Maintenance mode must be active.")
            return
        
        active_faults =0

        for item in self.fault_system.faults:
            if item['status']=='Active':
                item['status']='Resolved'
                active_faults +=1
        print("All active faults marked as resolved")

        self.event_log.add_event(
            "FAULT RESOLUTION", 
            username,
            details=f"{active_faults} active faults resolved."
        )


class login(): #using tkinter library later on
    pass

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
            f"Confirm refill of {medication_name}? (y/n): "
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


# go over this stuff still

class comms():
    pass

from datetime import datetime






class fault():
    def __init__(self, eventlog_object):
        self.faults=[]
        self.event_log = eventlog_object

    def add_fault(self,description, username = "system"):
        new_fault={
            "id" : len(self.faults)+1,
            "description" : description,
            "time" : datetime.now().isoformat(timespec="seconds"),
            "status" : "Active"
        }
        self.faults.append(new_fault)
        print("Fault detected and logged")

        self.event_log.add_event(
            "FAULT", 
            username, 
            details = description
        )

    def display_faults(self):
        print("\nFAULT HISTORY")
        print("-" * 75)
        if not self.faults:
            print("No faults recorded.")
            return
        
        for item in self.faults:
            print(
                f"{item['id']} | {item['description']} | "
                f"{item['status']} | {item['time']}"
            )

        
    print()

class hardware():
    pass

def get_integer_input(prompt):
    try:
        return int(input(prompt))
    except ValueError:
        print("Please enter a valid whole number.")
        return None

def main():

    event_history = eventlog() 

    stock = inventory()
    auth=authenticate(event_history)
 
    faults=fault(event_history)

    maintaince_system=maintaince(faults, event_history)

    refill_system = refill(
        stock,
        event_history
    )

    dispense_system = dispense(
        stock, 
        event_history,
        maintaince_system
    )

    try:
        while True:
            print("\n------------ADC LOGIN-------------- ")
            role = auth.authenticate()

            if role is None:
                break

            username = auth.current_username


            while True:
                print(f"\n ---------{role.upper()} MENU -----------")
                print("\n1. Display Inventory")
                print("2. Refill Medication")
                print("3. Dispense Medication")
                print("4. View Faults")
                print("5. Start Maintenance")
                print("6. Resolve Faults")
                print("7. End Maintenance")
                print("8. View Last 10 Event Entries")
                print("9. Exit")

                choice = get_integer_input("Select an option: ")

                if choice is None:
                    continue
                if choice==1:
                    stock.display_inventory()
                
                elif choice==2:
                    if role == "pharmacist" or role == "admin":
                        stock.display_inventory()
                        medication_id = get_integer_input(
                            "Enter ID to refill:"
                        )

                        quantity = get_integer_input("" \
                        "Enter quantity: ")

                        if medication_id is None or quantity is None:
                            continue

                        success = refill_system.refill_medication(
                            medication_id,
                            quantity, 
                            username
                        )

                     #   if success:
                     #       number = random.randint(1,10)

                         #   if number ==5:
                        faults.add_fault("Drawer malufunction", username)
                    else:
                        print("You are not authorized to refill medication.")
                elif choice ==3:
                    if role == "nurse" or role =="admin" or role=="pharmacist":
                        stock.display_inventory()

                        medication_id = get_integer_input(
                            "Enter ID to dispense: "
                        )

                        quantity = get_integer_input(
                            "Enter quantity:"
                        )

                        if medication_id is None or quantity is None:
                            continue

                        dispense_system.dispense_medication(
                            medication_id= medication_id,
                            quantity=quantity, 
                            username=username
                        )
                    else:
                        print("Your are not authorized to dispense medication.")
                elif choice ==4:
                    if role == "technician" or role=="admin":
                        faults.display_faults()
                    else:
                        print("Your are not authorized to view faults.")
                elif choice ==5:
                    if role == "technician":
                        maintaince_system.start_maintenance(username)
                    else:
                        print("You are not authorized to perform maintenance")

                elif choice ==6:
                    if role == "technician":
                        maintaince_system.clear_faults(username)
                    else:
                        print("Your are not authroized to resolve faults. ")
                elif choice ==7:
                    if role == "technician":
                        maintaince_system.end_maintenance(username)
                    else:
                        print("You are not authorized to end maintenance.")
                elif choice ==8:
                    if role =="admin":
                        event_history.display_log(10)
                    else:
                        print("You are not authorized to view the event log.")
                elif choice ==9:
                    print(f"\n{username} has logged out.")

                    event_history.add_event(
                        "LOGOUT", 
                        username, 
                        details=f"{role} logged out of the ADC."
                    )

                    break

                else:
                    print("Invalid option. PLease enter a number from 1 to 9.")
    finally:
                    event_history.close()

if __name__ == "__main__":
                    main()
                    
                
