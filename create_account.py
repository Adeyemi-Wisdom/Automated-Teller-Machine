import random
class Create_account:
    def __init__(self):
        self.num = [0,1,2,3,4,5,6,7,8,9]
        self.gen_num = []
        self.password = 2003
        self.customer_balance = 2000000
        self.user_acc = None
    def create_acc(self):
        print("Let's run through it together")
        name = input("What is your first name?")
        customer_password = int(input("Enter a four digit number to get it saved as your password"))
        self.password = customer_password
        money = int(input("How much are you taking into your account?"))
        for i in range(1,11):
            account_num = random.choice(self.num)
            self.gen_num.append(account_num)
            self.user_acc = ''.join(map(str, self.gen_num))
        person_1 = {
            "person_name": f"{name}",
            "person_password": f"{ customer_password}",
            "person_money": f"{ customer_password}",
            "person_number": f"{self.user_acc}"
        }
        print(f"You are welcome {name}, your account Number is {self.user_acc}")

