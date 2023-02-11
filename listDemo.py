print("Demonstration of list")

# Data : Heterogeneous
# Ordered : Yes
# Indexed : Yes
# Mutable : Yes
# Duplicates : Yes

data = [11,21,51,101,21,11]     #duplicate
data1 = [11,90.80, True ,"Hello"]   #Heterogeneous

print("Data ata index 2 :",data[2])
print("Data is ordered :",data1)
print("Data at index 2 : ",data[2])
print("Data with duplicate elements :",data)

print("List is mutable")
data.append(201)
print("Data after append :",data)
data.pop()

print("Data after pop :",data)