from create_account import Create_account
class Withdraw (Create_account):
    def __init__(self):
        super().__init__()
    def cash_out(self, amount):
        print("loading... ")
        password_check = int(input("Enter your password"))
        if password_check == self.password:
            print("Thank you for banking with us, see you next time")
            self.customer_balance -= amount
            if self.customer_balance > 0:
                print(f"Your remaining balance is: {self.customer_balance}")
            else:
                print("Insufficient funds")
        else:
            print("Wrong Password")
    def check_balance(self):
        password_check = int(input("Enter your password"))
        if password_check == self.password:
            print(f"Your account balance is: {self.customer_balance}")
        else:
            print("Wrong Password")



