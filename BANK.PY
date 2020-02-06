#Defining class Bankapp
class Bankapp:
    #initializin constuctor
    def __init__(self):
        while True:
            print("WELCOME TO HDFC BANK")
            n=input("Name: ")
            acc=int(input("Account Number: "))
            self.cb=5000
            print("Current Balance: ",self.cb)
            print("1 for widraw\n0 for deposit")
            a=input('Enter here: ')
            if a=='1':
                print("Current balance",self.withdraw())
            elif a=='0':
                print("Current balance",self.deposit())
            else:
               break
     #Defining function to withdraw      
    def withdraw(self):
        amount=float(input("Enter amount to widraw: "))
        return self.cb-amount
    #Defining function for deposit
    def deposit(self):
        amount=float(input("Enter amount to deposit: "))
        return self.cb+amount
Bankapp()

