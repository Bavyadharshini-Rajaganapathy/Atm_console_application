from Holder import Holder

def print_menu():
    print("Please choose from one of the following options...")
    print("1. Deposit Amount")
    print("2. Withdraw Amount")
    print("3. Show Account Balance")
    print("4. Exit")

def deposit (Holder):
    try:
        deposit = float(input("Type how much amount you want to deposit: "))
        Holder.set_balance(Holder.input_balance() + deposit)
        print("Thank you! Your new balance is: ", str(Holder.input_balance()))
    except:
        print("Invalid input")

def withdraw(Holder):
    try:
        withdraw = float(input("Type how much amount you want to withdraw: "))
        if(Holder.input_balance() < withdraw):
            print("Insufficient balance")
        else:
            Holder.set_balance(Holder.input_balance() - withdraw)
        print("You're good to go! Thank you")
    except:
        print("Invalid input")

def check_balance(Holder):
    print("Your current balance is: ",Holder.input_balance())

if __name__ == "__main__":
    current_user = Holder("", "", "", "", "")

    ### Create a repo of cardholders
    list_of_cardHolders = []
    list_of_cardHolders.append(Holder("4513675993793002", 1234, "Bavya", "dharshini", 15000.31))
    list_of_cardHolders.append(Holder("4525365805676345", 4332, "Sanjay", "dharshan", 32100.13))
    list_of_cardHolders.append(Holder("5125254648699876", 9239, "Danush", "kodi", 54908.59))
    list_of_cardHolders.append(Holder("6011163565789893", 2348, "Mathav", "Ramalingam", 1234567.84))
    list_of_cardHolders.append(Holder ("3490346765687763", 4766, "Ahalya", "R", 12345.27))

    ### Prompt user for debit card number
    debitCardNum = ""
    while True:
        try:
            debitCardNum = input("Please insert your debit card: ")
            ### Check against repo
            debitMatch = [holder for holder in list_of_cardHolders if holder.cardNum == debitCardNum]
            if (len(debitMatch) > 0):
                current_user = debitMatch[0]
                break
            else:
                print("Card number not recognized. Please try again.")
        except:
            print("Card number not recognized. Please try again.")

    ### Prompt for PIN
    while True:
        try:
            userPin = int(input("Please enter your pin: ").strip())
            if (current_user.input_pin() == userPin):
                break
            else:
                print("Invalid PIN. Please try again.")
        except:
            print("Invalid PIN. Please try again.")

    ### Print options
    print("Welcome", current_user.input_firstName(),":)")
    option = 0
    while (option != 4):
        print_menu()

        try:
            option = int(input())
        except:
            print("Invalid input. Please try again.")

        if (option == 1):
            deposit(current_user)
        elif (option == 2):
            withdraw(current_user)
        elif (option == 3):
            check_balance(current_user)
        elif (option == 4):
            break
        else:
            option: 0
    print("Thank you have a nice day!")