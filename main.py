from withdraw import Withdraw
from create_account import Create_account
from authentication import Authentication
withdraw = Withdraw()
create_account = Create_account()
operation_is_on = True
def main_operation():
    print("You are welcome!")
    operation = input(
        "To withdraw enter 1 \n"
        "To check your balance enter 2 \n"
        "To transfer enter 3 \n"
        "To request a loan enter 4 \n"
        "To make a loan payment enter 5 \n"
        "To create an account enter 6 \n"
    )
    match operation:
        case "1":
            amount = int(input("How much are you withdrawing? #___"))
            withdraw.cash_out(amount)
        case "2":
            withdraw.check_balance()
        case "3":
            print("Transfer functionality is not yet implemented.")
        case "4":
            print("Loan request functionality is not yet implemented.")
        case "5":
            print("Loan payment functionality is not yet implemented.")
        case "6":
            create_account.create_acc()
        case _:
            print("Check through our menu again and input the right thing.")
while operation_is_on:
    main_operation()
    user_pref = input("Do you want to exit: yes/no").lower()
    if user_pref == "no":
        main_operation()
    else:
        print("Thank you for banking with us. Good-Bye and Enjoy your day!")
        break



