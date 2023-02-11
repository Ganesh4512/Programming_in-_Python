

def Substraction(No1,No2):
    Ans = 0
    Ans = No1 - No2
    return  Ans

def Decorator_Fuction(Fuction_Name):
    def Inner(A,B):
        if(A < B):
            A,B = B,A
        return Fuction_Name(A,B)
    return Inner

def main():
    Value1 = int(input("Enter first number"))
    Value2 = int(input("Enter Second number"))

    New_Fuction= Decorator_Fuction(Substraction)
    print(New_Fuction(Value1 ,Value2))

if __name__ == "__main__":
    main()