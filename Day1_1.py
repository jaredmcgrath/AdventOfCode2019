import math
data = map(int, open('1.txt','r').read().split('\n'))
print(sum([math.floor(int(x)/3)-2 for x in data]))
