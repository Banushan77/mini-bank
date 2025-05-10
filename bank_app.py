#====================================BANK APP==========================================================
#ACCOUNT CREATE.=======================================================================================

import random

def create_random_num():
    return random.randint(1000,9000)

ACC_details={}
balance=0

def create_account ():
    print("----create account----")
    account_number= create_random_num()
    user_name=input("Enter your name: ")
    create_password=input("Enter your password: ")
    initial_balance = float(input("Enter your initial balance: "))
    if initial_balance > 0:
        with open ("ACC_details.txt","w")as file:
            file.write(f"{account_number},{user_name},{create_password},{initial_balance}\n ")
            print(f" *your account create successfully...Your account number is {account_number}* ")
    else:
        print("your initial balance is must be non negative")



#====================================================================================================
#LOG IN ACCOUNT =====================================================================================

def login_account ():
    print("----login_account----")
    user_name =input("Enter your name: ")
    password =input("Enter your password: ")

    with open ("ACC_details.txt","r")as file:
        for i in file :
            user_data = i.strip().split(",")
            if len(user_data) >=3: 
                stored_user_name , stored_create_password  =user_data[1],user_data[2]
                if stored_user_name==user_name and stored_create_password==password:
                    print("----login successfully----")
                else:
                    print("Invalid user name or password")
        
                

#======================================================================================================
#transaction_history===================================================================================

def transaction_history(acc_num):
    with open ("transaction_history.txt","r")as file:
        for i in file :
            user_data = i.strip().split(",")
            if user_data[0] == str(acc_num): 
                stored_deposit , stored_withdraw  = user_data[1], user_data[2]
                print(f"Your Deposit amount is {stored_deposit}\n Your Withdraw amount is {stored_withdraw}")


def All_transaction_history():
    with open ("transaction_history.txt","r")as file:
        for i in file :
            user_data = i.strip().split(",")
            if len(user_data) :
                acc_number , stored_deposit , stored_withdraw  = user_data[0],user_data[1], user_data[2]
                print(f"user account number is {acc_number}, user Deposit amount is {stored_deposit}, user Withdraw amount is {stored_withdraw}\n")

   #===================================================================================================
   #deposit_money======================================================================================        

def deposit_money(acc_num):
    deposit_amount = float(input("Enter your amount: "))
    history_updated = False

    updated_history = []
    try:
        with open("transaction_history.txt", "r") as file:
            for line in file:
                data = line.strip().split(",")
                if data[0] == str(acc_num):
                    current_deposit = float(data[1])
                    new_deposit = current_deposit + deposit_amount
                    data[1] = str(new_deposit)
                    updated_line = ",".join(data)
                    updated_history.append(updated_line + "\n")
                    history_updated = True
                else:
                    updated_history.append(line)
    except FileNotFoundError:
        pass

    if not history_updated:
        updated_history.append(f"{acc_num},{deposit_amount},0.0\n")

    with open("transaction_history.txt", "w") as file:
        file.writelines(updated_history)

    updated_lines = []
    with open("ACC_details.txt", "r") as file:
        for line in file:
            data = line.strip().split(",")
            if data[0] == str(acc_num):
                current_balance = float(data[3])
                new_balance = current_balance + deposit_amount
                data[3] = str(new_balance)
                updated_line = ",".join(data)
                updated_lines.append(updated_line + "\n")
            else:
                updated_lines.append(line)

    with open("ACC_details.txt", "w") as file:
        file.writelines(updated_lines)

    print("Deposit successful. Account balance and transaction history updated.")



#=========================================================================================================
#withdraw_money===========================================================================================

def withdraw_money(acc_num):
    withdraw_amount = float(input("Enter your amount: "))

    updated_lines = []
    account_found = False


    with open("ACC_details.txt", "r") as file:
        for line in file:
            data = line.strip().split(",")
            if data[0] == str(acc_num):
                current_balance = float(data[3])
                if withdraw_amount > current_balance:
                    print("Insufficient balance.")
                    return
                new_balance = current_balance - withdraw_amount
                data[3] = str(new_balance)
                updated_line = ",".join(data)
                updated_lines.append(updated_line + "\n")
                account_found = True
            else:
                updated_lines.append(line)

    if not account_found:
        print("Account number not found.")
        return

    with open("ACC_details.txt", "w") as file:
        file.writelines(updated_lines)

    print("Withdrawal successful. Account balance updated.")

  #=========================================================================================================
  # updated_history=========================================================================================

    updated_history = []
    with open("transaction_history.txt", "r") as file:
        for line in file:
            data = line.strip().split(",")
            if data[0] == str(acc_num):
                current_withdraw = float(data[2])
                new_withdraw = current_withdraw + withdraw_amount
                data[2] = str(new_withdraw)
                updated_line = ",".join(data)
                updated_history.append(updated_line + "\n")
            else:
                updated_history.append(line)

    with open("transaction_history.txt", "w") as file:
        file.writelines(updated_history)

    print("Transaction history updated.")

    
#============================================================================================================
#check_balance===============================================================================================    


def check_balance(acc_num):
     with open ("ACC_details.txt","r")as file:
        for i in file :
            user_data = i.strip().split(",")
            if user_data[0] == str(acc_num): 
                stored_balance  = user_data[3]
                print(f"Your balance is {stored_balance}")


#=============================================================================================================
#admin========================================================================================================

admin_name = "Banu1"
password = "12345"

def admin ():
    while True:
        print(" 1. create account ")
        print(" 2. Transaction History ")
        print(" 3. exit ")
 
        choice = input("Choose an option (1-3): ")

        if choice == '1':
            input_admin_name = input("Enter your admin name: ")
            input_admin_password = input("Enter your admin password: ")
            if  admin_name == input_admin_name and password == input_admin_password :
                print("Login Suggesfully!!")
                create_account()
            else:
                print("Admin username or password invalid")
        elif choice == '2':
            All_transaction_history ()
        elif choice == '3':
            main_menu()
        else:
            print("Invalid choice.")

#==========================================================================================================
#user======================================================================================================

def user():
    while True:
        print(" 1. Login account ")
        print(" 2.  Deposit Account")
        print(" 3. Withdraw Account ")
        print(" 4. check Balance")
        print(" 5. Trassaction History ")
        print(" 6. Exit")
 
        choice = input("Choose an option (1-6): ")

        if choice == '1':
            login_account ()
        elif choice == '2':
            acc_num = input("Enter your account number ")
            deposit_money (acc_num)
        elif choice == '3':
            acc_num = input("Enter your account number ")
            withdraw_money(acc_num)
        elif choice == '4':
            acc_num = input("Enter your account number ")
            check_balance(acc_num)
        elif choice == '5':
            acc_num = input("Enter your account number ")
            transaction_history(acc_num)
        elif choice == '6':
            main_menu()
        else:
            print("Invalid choice.")

#==========================================================================================================
#main menu=================================================================================================

def main_menu():
    while True:
        print(" 1. Admin ")
        print(" 2. User")
        print(" 3. exit ")
 
        choice = input("Choose an option (1-3): ")

        if choice == '1':
            admin ()
        elif choice == '2':
            user ()
        elif choice == '3':
            break
        else:
            print("Invalid choice.")


main_menu()
  

#===========================================================================================================
#===========================================================================================================
