import copy, itertools
sData = [int(x) for x in open('7.txt','r').read().split(',')]

def runAmp(sData, phase, sig):
    data = copy.deepcopy(sData)
    returnVal = 0
    ins = 0
    inputPtr = 0
    inVal = [phase, sig]
    while data[ins]%100 != 99:
        if data[ins]%100 == 1:
            # add
            # only p1, p2 can be imm values
            p1 = data[ins+1] if (data[ins]%1000)//100 else data[data[ins+1]]
            p2 = data[ins+2] if data[ins]//1000 else data[data[ins+2]]
            data[data[ins+3]] = p1 + p2
            ins+=4
        elif data[ins]%100 == 2:
            # mul
            # only p1, p2 can be imm values
            p1 = data[ins + 1] if (data[ins]%1000) // 100 else data[data[ins + 1]]
            p2 = data[ins + 2] if data[ins] // 1000 else data[data[ins + 2]]
            data[data[ins + 3]] = p1 * p2
            ins+=4
        elif data[ins]%100 == 3:
            #input
            data[data[ins+1]] = inVal[inputPtr]
            inputPtr += 1
            ins +=2
        elif data[ins] %100 == 4:
            #output
            p1 = data[ins + 1] if data[ins] // 100 else data[data[ins + 1]]
            returnVal = p1
            ins+=2
        elif data[ins]%100 == 5:
            #jmp if true
            p1 = data[ins + 1] if (data[ins] % 1000) // 100 else data[data[ins + 1]]
            p2 = data[ins + 2] if data[ins] // 1000 else data[data[ins + 2]]
            if p1:
                ins = p2
            else:
                ins+=3
        elif data[ins]%100 == 6:
            #jmp if false
            p1 = data[ins + 1] if (data[ins] % 1000) // 100 else data[data[ins + 1]]
            p2 = data[ins + 2] if data[ins] // 1000 else data[data[ins + 2]]
            if not p1:
                ins = p2
            else:
                ins += 3
        elif data[ins]%100 == 7:
            # lt
            p1 = data[ins + 1] if (data[ins] % 1000) // 100 else data[data[ins + 1]]
            p2 = data[ins + 2] if data[ins] // 1000 else data[data[ins + 2]]
            if p1 < p2:
                data[data[ins+3]] = 1
            else:
                data[data[ins + 3]] = 0
            ins += 4
        elif data[ins]%100 == 8:
            #eq
            p1 = data[ins + 1] if (data[ins] % 1000) // 100 else data[data[ins + 1]]
            p2 = data[ins + 2] if data[ins] // 1000 else data[data[ins + 2]]
            if p1 == p2:
                data[data[ins + 3]] = 1
            else:
                data[data[ins + 3]] = 0
            ins += 4

    return returnVal


phases = [0, 1, 2, 3, 4]
perms = itertools.permutations(phases)
maxOutput = -1
for perm in perms:
    sigIn = 0
    for phase in perm:
        sigIn = runAmp(sData, phase, sigIn)
    if sigIn > maxOutput:
        maxOutput = sigIn

print(maxOutput)