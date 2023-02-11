
def Display(No):
        if(0 < No):
            No = No -1
            Display(No)  #REcursive call
            print(No)




Display(6)