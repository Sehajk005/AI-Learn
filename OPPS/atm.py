class Atm:
    
    # __init__ method is a constructor that initializes the attributes of the class every time an object of the class is created.
    
    def __init__(self):
        self.__pin = ""
        self.__balsnce = 0
        
        self.menu()
    
    def menu(self):
        user_input = input("""
                           Hello, how can I help you?
                           1. Enter 1 to create a pin
                           2. Enter 2 to deposit
                           3. Enter 3 to withdraw
                           4. Enter 4 to check balance
                           5. Enter 5 to exit
                           """)
        if user_input == "1":
            self.create_pin()
        elif user_input == "2":
            self.deposit()
        elif user_input == "3":
            self.withdraw()
        elif user_input == "4":
            self.check_balance()
        else:
            print("Thank you for using the ATM. Goodbye!")
            
    def get_pin(self):
        return self.__pin
    
    def set_pin(self, new_pin):
        if len(new_pin) == 4 and new_pin.isdigit() and new_pin != self.__pin and type(new_pin) == str:
            self.__pin = new_pin
            print("Pin updated successfully.")
        else:
            print("Invalid pin. Please enter a 4-digit numeric pin.")

    def create_pin(self):
        self.__pin = input("Enter a new pin: ")
        print("Pin created successfully.")
        
        self.menu()
        
    def deposit(self):
        temp = input("Enter your pin: ")
        if temp == self.__pin:
            amount = int(input("Enter amount to deposit: "))
            self.__balsnce += amount
            print(f"Deposited {amount}. New balance is {self.__balsnce}.")
        else:
            print("Incorrect pin.")
            
        self.menu()
            
    def withdraw(self):
        temp = input("Enter your pin: ")
        if temp == self.__pin:
            amount = int(input("Enter amount to withdraw: "))
            if amount <= self.__balsnce:
                self.__balsnce -= amount
                print(f"Withdrew {amount}. New balance is {self.__balsnce}.")
            else:
                print("Insufficient balance.")
        else:
            print("Incorrect pin.")
            
        self.menu()
            
    def check_balance(self):
        temp = input("Enter your pin: ")
        if temp == self.__pin:
            print(f"Your balance is {self.__balsnce}.")
        else:
            print("Incorrect pin.")
            
        self.menu()
        
sbi_atm = Atm()