

def Area(Radius,PI=3.14):
    Result = PI * Radius * Radius
    return Result



def main():
    RValue =10.5
    PIValue = 3.14

    #positional Argument
    Ans = Area (RValue,PIValue)   # ans = Area(10.5,3.14)
    print("Area of circle is : ",Ans)

    #keyword Argument
    Ans = Area(PI =PIValue, Radius= RValue)  # ans = Area(3.14,10.5)
    print("Area of circle is : ", Ans)

    #positional arguments and second is default
    Ans = Area(10.5)        #Ans = Area(10.5)
    print("Area of circle is : ", Ans)

    #keyword  arguments
    Ans = Area(PI =7.10,Radius=10.5)    #Area = Area(10.5)
    print("Area of circle is : ", Ans)



if __name__ == "__main__":
    main()