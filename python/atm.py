import datetime
from datetime import datetime
from datetime import date

class atm:
    def __init__(self):
        self.set_pin = ''
        self.bank = 0
        self.transaction = []
        self.atm_menu()
    
    def atm_menu(self):
        user_input = int(input("""
        Press 1 for Generate Pin                       
        Press 2 Deposite Amount                       
        Press 3 Widthdrawl Amount                       
        Press 4 for Check Balance 
        Press 5 for print Transaction                                        
        Press 0 for Exit                      
        """))
        
        if user_input == 1:
            self.generate_pin()
        elif user_input == 2:
            self.deposite_amount()
        elif user_input == 3:
            self.withdrawl_amount()
        elif user_input == 4:
            self.check_balance()
        elif user_input == 5:
            self.transaction_detail()
        
    def generate_pin(self):
        self.set_pin = input("set your pin:-")
        print("pin generated successfully")

        self.atm_menu()

    def deposite_amount(self):
        user_pin = input("enter your pin:-")

        if self.set_pin == user_pin:
            amount = int(input("enter your amount:"))
            current_time = datetime.now()
            all_detail = [amount,"Cr",current_time,self.bank]
            self.bank += amount
            self.transaction.append(all_detail)
        else:
            print("entered pin is wrong ....please check!")

        self.atm_menu()

    def withdrawl_amount(self):
        user_pin = input("enter your pin:")

        if self.set_pin == user_pin:
            amount = int(input("enter the withdrawl amount:"))
            current_time = datetime.now()
            all_detail = [amount,"Dr",current_time,self.bank]
            self.bank -= amount
            self.transaction.append(all_detail)
            
        else:
           print("entered pin is wrong ....please check!") 

        self.atm_menu()

    def check_balance(self):
        user_pin = input("enter your pin:")

        if self.set_pin == user_pin:
            print("your saving account balance is:",self.bank)
        else:
           print("entered pin is wrong ....please check!")
        self.atm_menu()

    def transaction_detail(self):
        user_pin = input("enter your pin:-")
        if self.set_pin == user_pin:
            for i in self.transaction:
                print(i)

        self.atm_menu()

         

O1=atm()