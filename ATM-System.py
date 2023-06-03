import time
Acc_1 = 9500000
Acc_2 = 16500000
Acc_3 = 56000
Acc_4 = 160000
Acc_5 = 659000
pwd_1 = 123
pwd_2 = 234
pwd_3 = 345
pwd_4 = 456
pwd_5 = 567
banker_pwd = 9826
loop = True
while loop:
    print("Welcome to my ATM System")
    time.sleep(1)
    print("1 - Change Password")
    print("2 - Proceed to Money Management")
    print("3 - Change Owner Accounts (FOR BANKER'S USE ONLY)")
    action_on_startup = int(input("Action : "))
    if action_on_startup == 1:
        Acc_Num_1 = int(input("Enter Account Number : "))
        if Acc_Num_1 == 1:
            Temp_PWD = int(input("Enter Current Password :"))
            if Temp_PWD == pwd_1:
                New_PWD = int(input("Enter New Password : "))
                pwd_1 = New_PWD
                print("Password Changed Successfully")
            else:
                print("Wrong Password")
        elif Acc_Num_1 == 2:
            Temp_PWD = int(input("Enter Current Password :"))
            if Temp_PWD == pwd_2:
                New_PWD = int(input("Enter New Password : "))
                pwd_2 = New_PWD
                print("Password Changed Successfully")
            else:
                print("Wrong Password")
        elif Acc_Num_1 == 3:
            Temp_PWD = int(input("Enter Current Password :"))
            if Temp_PWD == pwd_3:
                New_PWD = int(input("Enter New Password : "))
                pwd_3 = New_PWD
                print("Password Changed Successfully")
            else:
                print("Wrong Password")
        elif Acc_Num_1 == 4:
            Temp_PWD = int(input("Enter Current Password :"))
            if Temp_PWD == pwd_4:
                New_PWD = int(input("Enter New Password : "))
                pwd_4 = New_PWD
                print("Password Changed Successfully")
            else:
                print("Wrong Password")
        elif Acc_Num_1 == 5:
            Temp_PWD = int(input("Enter Current Password :"))
            if Temp_PWD == pwd_5:
                New_PWD = int(input("Enter New Password : "))
                pwd_5 = New_PWD
                print("Password Changed Successfully")
            else:
                print("Wrong Password")
    elif action_on_startup == 2:
        Acc_Num = int(input("Enter Account number : "))
        time.sleep(1)
        if Acc_Num == 1:
            print("Hello, George")
            time.sleep(1)
            print("1 - Check Balance")
            print("2 - Withdraw Money")
            print("3 - Deposit Money")
            print("Enter the number only")
            WhatToday = int(input("What do you want to do today? : "))
            if WhatToday == 1:
                print("Your Balance is:", Acc_1)
            elif WhatToday == 2:
                print("Selected : Take Money")
                time.sleep(1)
                pwd=int(input("Enter the password : "))
                if pwd == pwd_1:
                    amount_take = float(input("Enter the amount to take : "))
                    if amount_take <= Acc_1:
                        bill_5000 = (amount_take - (amount_take % 5000)) / 5000
                        bill_1000 =((amount_take - 5000 * bill_5000) - (amount_take % 1000)) / 1000
                        bill_500 = ((amount_take - (1000 * bill_1000 + 5000 * bill_5000)) - (amount_take % 500)) / 500
                        bill_100 = ((amount_take - (500 * bill_500 + 1000 * bill_1000 + 5000 * bill_5000)) - (amount_take % 100)) / 100
                        bill_50 = ((amount_take - (100 * bill_100+  500 * bill_500 + 1000 * bill_1000 + 5000 * bill_5000)) - (amount_take % 50)) / 50
                        bill_20 = ((amount_take - (50 * bill_50 + 100 * bill_100 + 500 * bill_500 + 1000 * bill_1000 + 5000 * bill_5000)) - (amount_take % 20)) / 20
                        print("5000 Bills", bill_5000)
                        print("1000 Bills", bill_1000)
                        print("500 Bills", bill_500)
                        print("100 Bills", bill_100)
                        print("50 Bills", bill_50)
                        print("20 Bills", bill_20)
                        Acc_1 = Acc_1 - amount_take
                        print("Your Balance is:", Acc_1)
                        time.sleep(3)
                    else:
                        print("Insufficient Balance")
                        time.sleep(3)
                else:
                    print("Wrong Password")
            elif WhatToday == 3:
                print("Selected : Deposit Money")
                time.sleep(1)
                No_5000 = float(input("Number of 5000 Bills : "))
                No_1000 = float(input("Number of 1000 Bills : "))
                No_500 = float(input("Number of 500 Bills : "))
                No_100 = float(input("Number of 100 Bills : "))
                No_50 = float(input("Number of 50 Bills : "))
                No_20 = float(input("Number of 20 Bills : "))
                Acc_1 = Acc_1 + 5000 * No_5000 + 1000 * No_1000 + 500 * No_500 + 100 * No_100 + 50 * No_50 + 20 * No_20
                print("Your Balance is:", Acc_1)
                time.sleep(3)
            else:
                print("Invalid Response")
        elif Acc_Num == 2:
            print("Hello, Steve")
            time.sleep(1)
            print("1 - Check Balance")
            print("2 - Withdraw Money")
            print("3 - Deposit Money")
            print("Enter the number only")
            WhatToday = int(input("What do you want to do today? : "))
            if WhatToday == 1:
                print("Your Balance is:", Acc_2)
            elif WhatToday == 2:
                print("Selected : Take Money")
                time.sleep(1)
                pwd=int(input("Enter the password : "))
                if pwd == pwd_2:
                    amount_take = float(input("Enter the amount to take : "))
                    bill_5000 = (amount_take - (amount_take % 5000)) / 5000
                    bill_1000 =((amount_take - 5000 * bill_5000) - (amount_take % 1000)) / 1000
                    bill_500 = ((amount_take - (1000 * bill_1000 + 5000 * bill_5000)) - (amount_take % 500)) / 500
                    bill_100 = ((amount_take - (500 * bill_500 + 1000 * bill_1000 + 5000 * bill_5000)) - (amount_take % 100)) / 100
                    bill_50 = ((amount_take - (100 * bill_100+  500 * bill_500 + 1000 * bill_1000 + 5000 * bill_5000)) - (amount_take % 50)) / 50
                    bill_20 = ((amount_take - (50 * bill_50 + 100 * bill_100 + 500 * bill_500 + 1000 * bill_1000 + 5000 * bill_5000)) - (amount_take % 20)) / 20
                    print("5000 Bills", bill_5000)
                    print("1000 Bills", bill_1000)
                    print("500 Bills", bill_500)
                    print("100 Bills", bill_100)
                    print("50 Bills", bill_50)
                    print("20 Bills", bill_20)
                    Acc_2 = Acc_2 - amount_take
                    print("Your Balance is:", Acc_2)
                    time.sleep(3)
                else:
                    print("Wrong Password")
            elif WhatToday == 3:
                print("Selected : Deposit Money")
                time.sleep(1)
                No_5000 = int(input("Number of 5000 Bills : "))
                No_1000 = int(input("Number of 1000 Bills : "))
                No_500 = int(input("Number of 500 Bills : "))
                No_100 = int(input("Number of 100 Bills : "))
                No_50 = int(input("Number of 50 Bills : "))
                No_20 = int(input("Number of 20 Bills : "))
                Acc_2 = Acc_2 + 5000 * No_5000 + 1000 * No_1000 + 500 * No_500 + 100 * No_100 + 50 * No_50 + 20 * No_20
                print("Your Balance is:", Acc_2)
                time.sleep(3)
            else:
                print("Invalid Response")
        elif Acc_Num == 3:
            print("Hello, Tony!")
            time.sleep(1)
            print("1 - Check Balance")
            print("2 - Withdraw Money")
            print("3 - Deposit Money")
            print("Enter the number only")
            WhatToday = int(input("What do you want to do today? : "))
            if WhatToday == 1:
                print("Your Balance is:", Acc_3)
            elif WhatToday == 2:
                print("Selected : Take Money")
                time.sleep(1)
                pwd=int(input("Enter the password : "))
                if pwd == pwd_3:
                    amount_take = float(input("Enter the amount to take : "))
                    bill_5000 = (amount_take - (amount_take % 5000)) / 5000
                    bill_1000 =((amount_take - 5000 * bill_5000) - (amount_take % 1000)) / 1000
                    bill_500 = ((amount_take - (1000 * bill_1000 + 5000 * bill_5000)) - (amount_take % 500)) / 500
                    bill_100 = ((amount_take - (500 * bill_500 + 1000 * bill_1000 + 5000 * bill_5000)) - (amount_take % 100)) / 100
                    bill_50 = ((amount_take - (100 * bill_100+  500 * bill_500 + 1000 * bill_1000 + 5000 * bill_5000)) - (amount_take % 50)) / 50
                    bill_20 = ((amount_take - (50 * bill_50 + 100 * bill_100 + 500 * bill_500 + 1000 * bill_1000 + 5000 * bill_5000)) - (amount_take % 20)) / 20
                    print("5000 Bills", bill_5000)
                    print("1000 Bills", bill_1000)
                    print("500 Bills", bill_500)
                    print("100 Bills", bill_100)
                    print("50 Bills", bill_50)
                    print("20 Bills", bill_20)
                    Acc_3 = Acc_3 - amount_take
                    print("Your Balance is:", Acc_3)
                    time.sleep(3)
                else:
                    print("Wrong Password")
            elif WhatToday == 3:
                print("Selected : Deposit Money")
                time.sleep(1)
                No_5000 = int(input("Number of 5000 Bills : "))
                No_1000 = int(input("Number of 1000 Bills : "))
                No_500 = int(input("Number of 500 Bills : "))
                No_100 = int(input("Number of 100 Bills : "))
                No_50 = int(input("Number of 50 Bills : "))
                No_20 = int(input("Number of 20 Bills : "))
                Acc_3 = Acc_3 + 5000 * No_5000 + 1000 * No_1000 + 500 * No_500 + 100 * No_100 + 50 * No_50 + 20 * No_20
                print("Your Balance is:", Acc_3)
                time.sleep(3)
            else:
                print("Invalid Response")
        elif Acc_Num == 4:
            print("Hello, Peter")
            time.sleep(1)
            print("1 - Check Balance")
            print("2 - Withdraw Money")
            print("3 - Deposit Money")
            print("Enter the number only")
            WhatToday = int(input("What do you want to do today? : "))
            if WhatToday == 1:
                print("Your Balance is:", Acc_4)
            elif WhatToday == 2:
                print("Selected : Take Money")
                time.sleep(1)
                pwd=int(input("Enter the password : "))
                if pwd == pwd_4:
                    amount_take = float(input("Enter the amount to take : "))
                    bill_5000 = (amount_take - (amount_take % 5000)) / 5000
                    bill_1000 =((amount_take - 5000 * bill_5000) - (amount_take % 1000)) / 1000
                    bill_500 = ((amount_take - (1000 * bill_1000 + 5000 * bill_5000)) - (amount_take % 500)) / 500
                    bill_100 = ((amount_take - (500 * bill_500 + 1000 * bill_1000 + 5000 * bill_5000)) - (amount_take % 100)) / 100
                    bill_50 = ((amount_take - (100 * bill_100+  500 * bill_500 + 1000 * bill_1000 + 5000 * bill_5000)) - (amount_take % 50)) / 50
                    bill_20 = ((amount_take - (50 * bill_50 + 100 * bill_100 + 500 * bill_500 + 1000 * bill_1000 + 5000 * bill_5000)) - (amount_take % 20)) / 20
                    print("5000 Bills", bill_5000)
                    print("1000 Bills", bill_1000)
                    print("500 Bills", bill_500)
                    print("100 Bills", bill_100)
                    print("50 Bills", bill_50)
                    print("20 Bills", bill_20)
                    Acc_4 = Acc_4 - amount_take
                    print("Your Balance is:", Acc_4)
                    time.sleep(3)
                else:
                    print("Wrong Password")
            elif WhatToday == 3:
                print("Selected : Deposit Money")
                time.sleep(1)
                No_5000 = int(input("Number of 5000 Bills : "))
                No_1000 = int(input("Number of 1000 Bills : "))
                No_500 = int(input("Number of 500 Bills : "))
                No_100 = int(input("Number of 100 Bills : "))
                No_50 = int(input("Number of 50 Bills : "))
                No_20 = int(input("Number of 20 Bills : "))
                Acc_4 = Acc_4 + 5000 * No_5000 + 1000 * No_1000 + 500 * No_500 + 100 * No_100 + 50 * No_50 + 20 * No_20
                print("Your Balance is:", Acc_4)
                time.sleep(3)
            else:
                print("Invalid Response")
        elif Acc_Num == 5:
            print("Hello, William")
            time.sleep(1)
            print("1 - Check Balance")
            print("2 - Withdraw Money")
            print("3 - Deposit Money")
            print("Enter the number only")
            WhatToday = int(input("What do you want to do today? : "))
            if WhatToday == 1:
                print("Your Balance is:", Acc_5)
            elif WhatToday == 2:
                print("Selected : Take Money")
                time.sleep(1)
                pwd=int(input("Enter the password : "))
                if pwd == pwd_5:
                    amount_take = float(input("Enter the amount to take : "))
                    bill_5000 = (amount_take - (amount_take % 5000)) / 5000
                    bill_1000 =((amount_take - 5000 * bill_5000) - (amount_take % 1000)) / 1000
                    bill_500 = ((amount_take - (1000 * bill_1000 + 5000 * bill_5000)) - (amount_take % 500)) / 500
                    bill_100 = ((amount_take - (500 * bill_500 + 1000 * bill_1000 + 5000 * bill_5000)) - (amount_take % 100)) / 100
                    bill_50 = ((amount_take - (100 * bill_100+  500 * bill_500 + 1000 * bill_1000 + 5000 * bill_5000)) - (amount_take % 50)) / 50
                    bill_20 = ((amount_take - (50 * bill_50 + 100 * bill_100 + 500 * bill_500 + 1000 * bill_1000 + 5000 * bill_5000)) - (amount_take % 20)) / 20
                    print("5000 Bills", bill_5000)
                    print("1000 Bills", bill_1000)
                    print("500 Bills", bill_500)
                    print("100 Bills", bill_100)
                    print("50 Bills", bill_50)
                    print("20 Bills", bill_20)
                    Acc_5 = Acc_5 - amount_take
                    print("Your Balance is:", Acc_5)
                    time.sleep(3)
                else:
                    print("Wrong Password")
            elif WhatToday == 3:
                print("Selected : Deposit Money")
                time.sleep(1)
                No_5000 = int(input("Number of 5000 Bills : "))
                No_1000 = int(input("Number of 1000 Bills : "))
                No_500 = int(input("Number of 500 Bills : "))
                No_100 = int(input("Number of 100 Bills : "))
                No_50 = int(input("Number of 50 Bills : "))
                No_20 = int(input("Number of 20 Bills : "))
                Acc_5 = Acc_5 + 5000 * No_5000 + 1000 * No_1000 + 500 * No_500 + 100 * No_100 + 50 * No_50 + 20 * No_20
                print("Your Balance is:", Acc_5)
                time.sleep(3)
            else:
                print("Invalid Response")
        else:
            print("Invalid Response")
    elif action_on_startup == 3:
        Banker_pwd_1 = int(input("Enter Banker's Password : "))
        if banker_pwd == banker_pwd:
            print("Welcome Banker!")
            Acc_Num_2 = int(input("Enter Account Number : "))
            if Acc_Num_2 == 1:
                print("The Balance is", Acc_1)
                time.sleep(1)
                Acc_1 = int(input("Enter New Amount : "))
                print("Your Balance is", Acc_1)
                time.sleep(3)
            elif Acc_Num_2 == 2:
                print("The Balance is", Acc_2)
                time.sleep(1)
                Acc_2 = int(input("Enter New Amount : "))
                print("Your Balance is", Acc_2)
                time.sleep(3)
            elif Acc_Num_2 == 3:
                print("The Balance is", Acc_3)
                time.sleep(1)
                Acc_3 = int(input("Enter New Amount : "))
                print("Your Balance is", Acc_3)
                time.sleep(3)
            elif Acc_Num_2 == 4:
                print("The Balance is", Acc_4)
                time.sleep(1)
                Acc_4 = int(input("Enter New Amount : "))
                print("Your Balance is", Acc_4)
                time.sleep(3)
            elif Acc_Num_2 == 5:
                print("The Balance is", Acc_5)
                time.sleep(1)
                Acc_5 = int(input("Enter New Amount : "))
                print("Your Balance is", Acc_5)
                time.sleep(3)
            else:
                print("Invalid Response")
        else:
            print("Wrong Password")
