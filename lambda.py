#normal fuction /Named fuctions
#def Fuction_Name(Fuction_Parameters):
# Fuction_Body
def Add(No1,No2):
	return No1+No2

# Lambda fuctions /Unnamed fuction
#lambda parameterd : body

AddFuction= lambda A,B : A+B

Ans1 = Add(10,11)
Ans2 = AddFuction(10,11)

print("Addition using normal fuction :",Ans1)
print("Addition using normal fuction :",Ans2)

print("Type of lambda fuction is :",type(AddFuction))



