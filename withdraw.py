from create_account import Create_account
class Withdraw (Create_account):
    def __init__(self):
        super().__init__()
        self.count_it = 0
    def cash_out(self, amount):
        while True:
            password_check = int(input("Enter your password: "))
            wrong_password = str(password_check)
            if password_check != self.password:
                self.count_it += 1
                print("Wrong Password")
            if password_check != self.password and self.count_it == 3:
                print("You have entered the wrong password three times. Please Try again")
                break
            if password_check == self.password:
                self.customer_balance -= amount
                print('LOADING...')
                print(f"Kindly take your cash")
                print(F'Account balance: {self.customer_balance} ')
                break
    def check_balance(self):
        while True:
            try:
                password_check = int(input("Enter your password"))
                if password_check != self.password:
                    self.count_it += 1
                    print("Wrong password")
                if password_check != self.password and self.count_it == 3:
                     print("You have entered the wrong password three times. Please Try again")
                     break
                if password_check == self.password:
                    print(f"Your account balance is: {self.customer_balance}")
                    break
            except ValueError:
                self.count_it += 1
                print("Wrong Password")
                if self.count_it == 3:
                    print("Access Denied. Please try again")
                    break



