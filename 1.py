class atm:
    def __init__(self , pin , balance):
        self.pin = pin
        self.balance = balance
        self.attempts = 0 

    def check_pin(self , entered_pin):
        if self.attempts >= 3:
            print("account is banned talk to the bank")
            return False

        if entered_pin == self.pin:
            print("pin is correct")
            return True

        else:
            self.attempts += 1
            print("pin is incorrect")
            print(f"Remaining attempts ", {3 - self.attempts})
            return False


a = atm(pin = 1234 , balance = 1000)
a.check_pin(1222)
a.check_pin(1221)
a.check_pin(1232)
a.check_pin(1232)



    