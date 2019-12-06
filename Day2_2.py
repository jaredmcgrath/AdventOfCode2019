import copy
startData = [int(x) for x in open('2.txt','r').read().split(',')]


for n in range(0,100):
    for v in range(0,100):
        data = copy.deepcopy(startData)

        data[1] = n
        data[2] = v

        ins = 0
        while data[ins] != 99:
            if data[ins] == 1:
                data[data[ins+3]] = data[data[ins+1]] + data[data[ins+2]]
            elif data[ins] == 2:
                data[data[ins+3]] = data[data[ins+1]] * data[data[ins+2]]
            ins += 4
        if data[0] == 19690720:
            print(100*n + v)

