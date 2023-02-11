
#Fuction which accept nothing and returns nothing
def Demo1():
    print("Inside Demo1")
def Demo2(No):
    print("Inside Demo2 with argument :",No)

#fuction accept one parameter and return one parameter
def Demo3(No):
    print("Inside Demo3 with argument ",No)
    return No+2
#fuction accepts two parameter and return one parameters
def Demo4(No1,No2):
    print("Inside Demo4")
    Add = No1 + No1
    return Add
#fuction accepts two parameter and return two parameters
def Demo5(No1,No2):
    print("Inside Demo5")
    Add = No1 + No2
    Sub = No1 - No2
    return Add,Sub



#fuction accept p rameter one parameter and nothing
def main():
    Demo1()
    Demo2("Hello")
    Ans = Demo3(10)
    print("Return value of Demo3 is :",Ans)
    Ans = Demo4(10,11)
    Ans1,Ans2 = Demo5(11,10)
    print("First return value :",Ans1)
    print("Second return value :",Ans2)


if __name__ == "__main__":
    main()