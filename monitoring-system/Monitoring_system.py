class User:

    def __init__(self, name, password, role):
        self.name=name
        self.password=password
        self.role=role
        

def auth_user(u):
    n=0
    check=False
    while n<len(users) and check==False:
        if users[n].name!=u:
            n+=1
        else:
            check=True
    return(check)

def auth_pass(u,p):
    i=0
    check=False
    while i<len(users) and i!=-1:
        if u==users[i].name:
            u_p=users[i].password
            i=-1
        else:
            i+=1
    if i==len(users):
        print("Username doesn't exist")
    else:
        if u_p==p:
            check=True
    return(check)

def auth_role(u):
    i=0
    check=False
    while i<len(users) and i!=-1:
        if u==users[i].name:
            u_r=users[i].role
            i=-1
        else:
            i+=1
    if i==len(users):
        print("User doesn't exist")
    else:
        return(u_r)

    

def funcs(role):
    choice=""
    i=""
    if role == "d" or role == "n":
        choice=input ("Choose a function.\na) View ADC info\nb) Exit\n")
        if choice=="a" or choice=="A":
            i="ADC"
        elif choice=="b" or choice=="B":
            i="Exit"
        else:
            i="None"
    if role == "t":
        choice=input ("Choose a function.\na) View ADC info\nb) Alarms\nc) Exit\n")
        if choice=="a" or choice=="A":
            i="ADC"
        elif choice=="b" or choice=="B":
            i="Alarms"
        elif choice=="c" or choice=="C":
            i="Exit"
        else:
            i="None"
    if role == "p":
        choice=input ("Choose a function.\na) View ADC info\nb) Hospital Inventory\nc) Exit\n")
        if choice=="a" or choice=="A":
            i="ADC"
        elif choice=="b" or choice=="B":
            i="Inv"
        elif choice=="c" or choice=="C":
            i="Exit"
        else:
            i="None"
    if role == "a":
        choice=input ("Choose a function.\na) View ADC info\nb) Alarms\nc) History\nd) Generate\ne) Hospital Inventory\nf) Exit\n")
        if choice=="a" or choice=="A":
            i="ADC"
        elif choice=="b" or choice=="B":
            i="Alarms"
        elif choice=="c" or choice=="C":
            i="History"
        elif choice=="d" or choice=="D":
            i="Report"
        elif choice=="e" or choice=="E":
            i="Inv"
        elif choice=="f" or choice=="F":
            i="Exit"
        else:
            i="None"

    if i=="ADC":
        print ("Viewing ADC\n")
        return(0)
    if i=="Alarms":
        print ("Viewing alarms\n")
        return(0)
    if i=="History":
        print("Viewing history\n")
        return(0)
    if i=="Report":
        print("Viewing report\n")
        return(0)
    if i=="Inv":
        print("Viewing inventory\n")
        return(0)
    if i=="Exit":
        print("Exiting\n")
        return(1)
    if i=="" or i=="None":
        print("Please input the letter next to the desired function")
        return(0)

def new_user(new):
    if new == "y" or new == "Y":
        username=input("Select a Username: ")
        pas=input("Select a password: ")
        r=input("Are you an admin(a), technician(t), pharmasist(p), nurse(n) or doctor(d)? Enter role in all lower case: ")
        i=False
        while i!=True:
            if r=="a" or r=="t" or r=="p" or r=="d" or r=="n":
                i=True
            else:
                r=input("Not a valid role, please enter either a for admin, t for technician, p for pharmasist, d for doctor or n for nurse in lower case: ")
        new_user=User(name=username, password=pas, role=r)
        users.append(new_user)
    if new == "n" or new == "N" or new == "y" or new == "Y":
        return(1)
    else:
        return(0)





users=[]
new=input("Are you a new user? y/n: ")
val=new_user(new)
while val==0:
    new=input("Please only use y for yes or n for no. \nAre you a new user? y/n: ")
    val=new_user(new)


u=input("Username: ")
au=auth_user(u)
i=0
while i<3 and au==False:
    u=input("Username does not exist. Please try again: ")
    au=auth_user(u)
    i+=1
if i==3:
    print("Too many attempts, please try again later")
else:
    p=input("Password: ")
    ap=auth_pass(u,p)
    n=0
    while n<3 and ap==False:
        p=input("Username and password don't match. Please try again: ")
        ap=auth_pass(u,p)
        n+=1
    if n==3:
        print("Too many attempts, please try again later")
    else:
        role=auth_role(u)
        n=0
        while n==0:
            n=funcs(role)
        