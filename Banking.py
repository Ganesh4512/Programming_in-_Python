#instance variable: ANme,address,amount,account no.
#instance method : Create account(),DisplayAccountinfo
# Class variable : Bank_Name,ROI_On_FD
#Class method
#static method : DisplayKYCInfo



class Bank_Account:
    Bank_Name = "HDFC bank PVT LTD"

class Bank_Account:
    def __init__(self):
        self.Name =""
        self.Amount = 0
        self.Address =""
        self.AccountNo=0

    def CreateAccount(self):
        print("Enter your name : ")
        self.Name = input()

        print("Enter ur initial amount :")
        self.Amount=int(input())

        print=("Enter ur Address :")
        self.Address = input()

        print=("Enter account amount :")
        self.AccountNo = int(input())

    def DisplayAccountInfo(self):
        print("Ur account inforamation is as below_____  ")
        print("Name of Account holder :", self.Name)
        print("Account Number :", self.AccountNo)
        print("Address of account holder :", self.Address)
        print("Cureent amount in Current :", self.Amount)

    @classmethod
    def DisplayBankInformation(cls):
        print("Welcome to banking console")
        print("Name of bank",cls.Bank_Name)
        print("Rate of intrest we offer on fixed deposite is : ", cls.ROI_On_FD)

    @staticmethod
    def DisplayKYCInfo():
        print("Plz conside below KYC info")
        print("According to the rules of Government of india u have to submit below Document")
        print("1:Clear and recent passport size photo")
        print("2 :Photo of aadhar card")
        print("3 :photo PAN card")

    def Deposit(self,value):
        self.Amount=self.Amount+value

    def Withdraw(self,value):
        self.Amount=self.Amount-value
def main():
    Bank_Account.DisplayKYCInfo()

    print("Name of bank : ", Bank_Account.Bank_Name)
    print("Rate of Interest on Fixed deposit :", Bank_Account.ROI_On_FD)


    User1=Bank_Account()
    User2=Bank_Account()

    print("Creating th first account")
    User1.CreateAccount()

    print("Creating th first account")
    User2.CreateAccount()

    User1.DisplayAccountInfo()
    User2.DisplayAccountInfo()

    User1.Deposit(500)
    User2.Deposit(1200)

    print("Amount of {} User1 after deposit is {}:".format(User1.Name, User1.Amount))
    print("Amount of {} User2 after deposit is {}:".format(User2.Name, User2.Amount))

    User1.Withdraw(200)
    User2.Withdraw(3000)
    print("Amount of {} User1 after withdraw is {}:".format(User1.Name, User1.Amount))
    print("Amount of {} User2 after withdraw is {}:".format(User2.Name, User1.Amount))




if __name__ =="__main__":
    main()