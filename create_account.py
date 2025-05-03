import re
from datetime import datetime
import random
class Create_account:
    def __init__(self):
        self.not_allowed = ['1','2','3','4','5','6','7','8','9','0','!','@','#','$','%','^','^','&','(',')','-','_','+','}','{','[',']','"',"'",';',':',
             ';','/','>','<','.',',','?','/',"|",'~','`']
        self.not_allowed_two = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b',
                                'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        self.regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        self.date = datetime.now()
        self.error_count = 0
        self.num = [0,1,2,3,4,5,6,7,8,9]
        self.gen_num = []
        self.password = 2003
        self.customer_balance = 2000000
        self.user_acc = None
    def create_acc(self):
        print("Let's run through it together")
        while True:
            name = input("First Name: ")
            if any(char in self.not_allowed for char in name):
                print("Enter a valid name")
            else:
                print(f"Welcome {name}!")
                break
        while True:
            try:
                customer_password = int(input("Enter a four digit number to get it saved as your password"))
                custom_password = str(customer_password)
                if customer_password == int(customer_password) and len(custom_password) == 4:
                    self.password = customer_password
                    break
            except ValueError:
                print("Enter only four figure")
        while True:
            try:
                money = int(input("How much are you taking into your account? #"))
                if money == int(money) and money >= 500:
                 break
                else:
                    print("You must deposit at least #500")
            except ValueError:
                print("Wrong Input, try again")
        while True:
            user_birth = input("Enter your date of birth (DD-MM-YYYY)")
            format_to_verify = "%d-%m-%Y"
            try:
                if datetime.strptime(user_birth, format_to_verify):
                    break
            except ValueError:
                print("Follow this order please: Day-Month-Year")
        while True:
            mail = input("Enter your G_mail")
            if re.fullmatch(self.regex,mail):
                break
            else:
                print("Enter a correct Email address")
        for i in range(1,11):
            account_num = random.choice(self.num)
            self.gen_num.append(account_num)
            self.user_acc = ''.join(map(str, self.gen_num))
        person_1 = {
            "person_name": f"{name}",
            "person_password": f"{ customer_password}",
            "person_money": f"{money}",
            "person_acc_number": f"{self.user_acc}",
            "person_dob": f"{user_birth}"
        }
        print(f"You are welcome {name}, your account Number is {self.user_acc}. \n Account Creation Date and Time: {self.date}")