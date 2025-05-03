from withdraw import Withdraw
from create_account import Create_account
# from authentication import Authentication
withdraw = Withdraw()
create_account = Create_account()
operation_is_on = True
def main_operation():
    count = 0
    print("You are welcome!")
    operation = input(
        "To withdraw enter 1 \n"
        "To check your balance enter 2 \n"
        "To create an account enter 3 \n"
    )
    if operation == "1":
        while True:
            try:
                amount = int(input("Amount: #"))
                if amount == int(amount) and amount > 0:
                    withdraw.cash_out(amount)
                    break
                else:
                    print("You can only withdraw more than zero amount")
            except ValueError:
                count += 1
                print("Wrong Input. Start again by inputting the right entry ")
                if count == 3:
                    print("You have inputted what is wrong three times. You are a Thief. Get out!!!")
                    break
    elif operation == "2":
        withdraw.check_balance()
    elif operation == "3":
        create_account.create_acc()
    else:
        print("Go through the menu again and input what's right")
while operation_is_on:
    main_operation()
    user_pref = input("Do you want to exit: yes/no").lower()
    if user_pref == "no":
        main_operation()
    else:
        print("Thank you for banking with us. Good-Bye and Enjoy your day!")
        break