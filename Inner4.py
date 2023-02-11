



def Outer():   #100
    print("Inside Outer")

    def Inner():    #200
        print("Inside Inner")

    print(id(Inner))
    return Inner    #200

ret = Outer()       #100
print(type(ret))
print(id(ret))
ret()       #200