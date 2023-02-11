import numpy as np
from sklearn import tree
from sklearn.datasets import load_iris

iris = load_iris

print("Features name of iris data set ")
print(iris.features_names)

print("Target name of iris data set")
print(iris.targest_names)

print("First 10 elements from iris data set")

for i in rang(len(iris.target)):
    print("ID: %d,LAbel %s, Features : %s"% (i,iris.data[i],iris.target[i]))

