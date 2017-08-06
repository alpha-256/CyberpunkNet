"""
x = [1,2,3]
w = [1,2,3]
dataLen = len(x)
z = []
y = []

def neuron0():
    i = 0
    while i < dataLen:
        z.append(x[i] * w[i])
        i = i + 1
    y.append(sum(z))
    print(z)
    print(y)

neuron0()
"""
from random import randint as ri
x = []
a = []
a1 = []
def genData():
    genQty = int(input("Amount of data >>> "))
    counter = 0
    while counter < genQty :
        x.append(ri(1,27))
        counter= counter + 1
def neuron1():
    dataLen = len(x)
    xSum = sum(x)
    print(xSum)
    average = xSum / dataLen
    for i in x:
        z = int(i - average)
        xAvg = z^2
        a.append(xAvg)
    a0 = sum(a)
    a1.append(a0/dataLen)

genData()
neuron1()
print(a)
print(a1)
