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
x = [1,2,3,4,5,6,7,8,9,0]
dataLen = len(x)
a = []

def neuron1():
    xSum = sum(x)
    average = xSum / dataLen
    for i in x:
        z = int(i - average)
        xAvg = z^2
        a.append(xAvg/dataLen)

neuron1()
print(a)
