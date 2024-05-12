class Holder():
    def __init__(self, cardNum,  pin, firstname, lastname, balance):
        self.cardNum = cardNum
        self.pin = pin
        self.firstname = firstname
        self.lastname = lastname
        self.balance = balance


    def input_cardNum(self):
        return self.cardNum

    def input_pin(self):
        return self.pin

    def input_firstName(self):
        return self.firstname

    def input_lastName(self):
        return self.lastname

    def input_balance(self):
        return self.balance

    def set_cardNum(self, newVal):
        self.cardNum = newVal
    def set_pin(self, newVal):
        self.pin = newVal
    def set_firstName (self, newVal):
        self.firstname = newVal
    def set_lastName(self, newVal):
        self.lastname = newVal
    def set_balance(self, newVal):
        self.balance = newVal

def print_out(self):
    print("Card #: ", self.cardNum)
    print("Pin: ", self.pin)
    print("First Name: ", self.firstname)
    print("Last Name: ", self.lastname)
    print("Balance: ", self.balance)