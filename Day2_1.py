data = [int(x) for x in open('2.txt','r').read().split(',')]

ins = 0
while data[ins] != 99:
    if data[ins] == 1:
        data[data[ins+3]] = data[data[ins+1]] + data[data[ins+2]]
    elif data[ins] == 2:
        data[data[ins+3]] = data[data[ins+1]] * data[data[ins+2]]
    ins += 4


print(data[0])