#4
#1 2 3 4 = 9

    #def Add(No):
       # Ans = 0
        #while(No >= 0):
       #     Ans = Ans +No
        #    No = No -1

      #  return Ans

    #Ret = Add(4)
  #  print("Addition is ",Ret)

# recursion
def Add(No):
    if(No <= 0):
        return 0
    else:
        return (No+Add(No-1))

Ret = Add(4)
print("Result is  :",Ret)
