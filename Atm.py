class Atm:
    def __init__(self,cardNumber,pin):
        self.cardNumber= cardNumber
        self.pin=pin
    def  checkBalance(self):
        print("Your balance is 6000")
    def withdrawl(self,amount):
        print("You have withdrawn 1000 rupees")    

def main():
    cardNumber=input("insert your card number")
    pinNumber=input("enter your pin number")

    newUser= Atm(cardNumber,pinNumber)
    print("choose 1 for balance and 2 for withdrawl")
    Activity=int(input("enter activity number :- "))
    if (Activity==1):
     newUser.checkBalance(),
     
    elif (Activity==2):
     amount=int(input("enter your amount"))
     newUser.withdrawl(amount) 
    else :
        print("Enter a valid number")

main()


     

