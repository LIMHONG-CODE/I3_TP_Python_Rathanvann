class ATM:
    def __init__(self):
        self.balance = 2490

        self.case ={
            100 : 50,
            50 : 20,
            20 : 300,
            10 : 0,
            5 : 200,
            1 : 10
        }

    def withdraw (self, amount):

        #Check withdrawal amount
        if amount <= 0 :
            print(f"-> Invalid withdrawal amount !")
            return

        #Check customer balance
        if amount > self.balance :
            print("-> Insufficient bank account balance !")
            return

        #Check available banknotes
        remaining = amount
        note_to_give = {}

        for bill, quantity in self.case.items():
            notes = min(remaining // bill, quantity)

            if notes > 0:
                note_to_give[bill] = notes
                remaining -= notes * bill

        #Check whether ATM can provude exact amount
        if remaining != 0:
            print(f"-> ATM can't provide exact amount !")
            return

        #Update bank account balance
        self.balance -= amount

         #Update ATM banknote
        for bill, notes in note_to_give.items():
            self.case[bill] -= notes

        #Display transaction result 
        print(f"-> Transaction Successfull !")
        print(f"-> You have received : {amount}$")

        for bill, notes in note_to_give.items():
            print(f"{notes} of ${bill} bill")

        print(f"-> Your remaining balance: {self.balance}")

        print(f"-> Remaining in this machine: ")
        for bill, quantity in self.case.items():
            print(f"$ {bill} -> {quantity}")

while True:
    #Creat ATM object
    atm = ATM()

    #Withdraw amount
    amount = int(input(f"-> Please input your withdraw amount: "))

    atm.withdraw(amount)