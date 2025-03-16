class Bank:
    def __init__(self) -> None:
        self.balance = 0

    def readStartingBalance(self):
        self.balance = float(input("Starting balance: $"))
    
    def deposit(self):
        deposit_amount = float(input("Amount to deposit $"))
        self.balance += deposit_amount
        print(f'Amount deposited: ${deposit_amount:.2f}')
    
    def withdraw(self):
        withdraw_amount = float(input("Amount to withdraw $"))
        if withdraw_amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= withdraw_amount
            print(f'Amount withdrawn: ${withdraw_amount:.2f}')
    
    def show(self):
        print(f"starting balance ${self.balance:.2f}")
    
    def main(self):
        self.readStartingBalance()
        
        action = input("Start Banking (d/w/s/x): ")
        while (action != "x"):
            match action:
                case "s":
                    self.show()
                case "d":
                    self.deposit()
                case "w":
                    self.withdraw()
            
            action = input("Continue Banking (d/w/s/x): ")

    
my_bank = Bank()
my_bank.main()
