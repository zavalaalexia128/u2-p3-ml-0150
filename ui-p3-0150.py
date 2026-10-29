# Zavala Medina 0150
import numpy as np

A0150=np.array([10,20,30,40,50,])
print(A0150)
print(A0150[0])
print(A0150[3])
print(A0150[-1])
print(A0150[-2])
print("--------------------------")
A0150=np.array([
    [10],[20],[30],
    [40],[50],[60]
])
print(A0150)
print(A0150.shape)
print(A0150)
print(A0150[0, 0])
print(A0150[1, 0])
print(A0150[-1, -1])
print(A0150[-2, -1])
print("--------------------------")
A0150=np.array([
    #0 -2
    [
    [10],[20],[30],
    [40],[50],[60]
],
    #1 -1
    [
     [70],[80],[90],
     [100],[110],[120]
     ]
])
print(A0150)
print(A0150[0, 0, 0])
print(A0150[1, 1, 0])
print(A0150[-1, -1, -1])

print("Zavala Medina 0150")