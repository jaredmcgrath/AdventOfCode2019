data = [int(x) for x in open('8.txt','r').read()]

w = 25
h = 6
layers = []
idx = 0
count = len(data)

for i in range(int(len(data)/(w*h))):
    layers.append(data[i*h*w:(i+1)*h*w])
    if layers[i].count(0) < count:
        count = layers[i].count(0)
        idx = i

print(layers[idx].count(1)*layers[idx].count(2))