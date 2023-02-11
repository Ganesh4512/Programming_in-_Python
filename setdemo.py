print("Demonstration of list")

c

data = {11,21,51,101,21,11}     #duplicate
data1 = {11,90.80, True ,"Hello"}   #Heterogeneous

print("First set data : ",data)
print("Lenghth of data :",len(data))
print("Data is Heterogeneous :" , data1)
print("Data is unordered :",data1)
#print("Data at index 2 : ",data[2])
print("Data with unique duplicate elements :",data)



print("Set is mutable")
# Insert element is set
data.add(211)
print("Data after insertion :",data)

#Remove element
data.remove(211)
print("Data after removal : ",data)

data.discard(201)
print("Data after discard : ",data)