print("Application to demonstrate Industrial programming")

import marvellousmodule
def main():
    print("Value of  __name__  from main is :", __name__)

    print("Enter first numer : ")
    no1= int(input())
    print("Enter second numer : ")
    no2= int(input())

    Sum = marvellousmodule.Addition(no1,no2)

    print("Addition is : ",Sum)

if __name__ == "__main__":
    main()