class Bank:
    balance = 1000

    def main(self):
        action = input("Start Banking (d/w/s/x): ")

        while action != "x":
            if action == "s":
                print(f"starting balance ${self.balance:.2f}")
            elif action == "d":
                deposit_amount = float(input("Amount to deposit $"))
                self.balance += deposit_amount
                print(f'Amount deposited: ${deposit_amount:.2f}')
            elif action == "w":
                withdraw_amount = float(input("Amount to withdraw $"))
                if withdraw_amount > self.balance:
                    print("Insufficient funds")
                else:
                    self.balance -= withdraw_amount
                    print(f'Amount withdrawn: ${withdraw_amount:.2f}')
            
            action = input("Continue Banking (d/w/s/x): ")

    
my_bank = Bank()
my_bank.main()
