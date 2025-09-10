pin = "200748"
info = ["John", "19-09-1999", "Accounting"]
balance = 50000000  

while True:
    print("----------WELCOME TO LOCAL MOBILE BANK----------")
    is_correct = input("Your Pin : ")

    if is_correct == pin:
        while True:
            print("\n1. Info\n2. Balance\n3. Transaction\n4. Back")
            firstAction = input("Choose your action : ")

            if firstAction == "4":
                print("----------THANKS FOR COMING, HAVE A GREAT DAY!----------")
                break  

            elif firstAction == "1":
                print(f"Name : {info[0]}\nBirth : {info[1]}\nJob : {info[2]}")

            elif firstAction == "2":
                print(f"Balance : {balance:,}")

            elif firstAction == "3":
                print("\n1. Top Up\n2. Transfer\n3. Back")
                secondAction = input("Choose your action : ")

                if secondAction == "3":
                    continue 

                if secondAction == "1":  
                    while True:
                        print("Maximum Amount 20,000,000")
                        try:
                            amount = int(input("Input Amount : "))
                        except ValueError:
                            print("Invalid input! Please enter a number.")
                            continue

                        if amount > 20000000:
                            print("Amount is exceed of 20,000,000.")
                        else:
                            balance += amount
                            print(f"Top Up success! New Balance: {balance:,}")
                            break

                if secondAction == "2": 
                    while True:
                        print("Maximum Amount 20,000,000")
                        try:
                            amount = int(input("Input Amount : "))
                        except ValueError:
                            print("Invalid input! Please enter a number.")
                            continue

                        if amount > 20000000:
                            print("Amount is exceed of 20,000,000.")
                        elif amount > balance:
                            print("Not enough balance!")
                        else:
                            balance -= amount
                            print(f"Transfer success! New Balance: {balance:,}")
                            break

            else:
                print("Unable Action!")
        break  
    else:
        print("Wrong PIN! Try again.\n")
