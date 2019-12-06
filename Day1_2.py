import math

data = open('1.txt','r').read().split('\n')

totalFuel = 0
for mass in map(int, data):
    newFuel = math.floor(mass/3)-2
    while newFuel > 0:
        totalFuel += newFuel
        newFuel = math.floor(newFuel/3)-2

print(totalFuel)
