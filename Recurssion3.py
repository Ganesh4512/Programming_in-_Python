
def Display(No):
    if(No > 0):
        print("Hello")
        No = No -1
        Display(No)         #Recursive fuction call

Display(4)      #fuction call