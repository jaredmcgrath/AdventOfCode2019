import copy, itertools
sData = [int(x) for x in open('7.txt','r').read().split(',')]

# Add default params so we can start new or continue mid-execution
# The inputPtr = 0 only on first iteration, to indicate we send phase. Otherwise, it is 1
# This will mutate data too
def runAmp(data, phase, sig, ins = 0, inputPtr = 0):
    returnVal = 0
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
            if inputPtr == 1:
                data[data[ins + 1]] = sig
                inputPtr += 1
            elif inputPtr == 0:
                data[data[ins+1]] = phase
                inputPtr += 1
            # This is where we want to return, just before we look for the next input signal
            else:
                # prep for return. Don't change ins
                # Need to return data, ins, inputPtr, and returnVal as tuple
                return data, ins, inputPtr-1, returnVal
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
    # If we just return a single value
    return returnVal


phases = [5, 6, 7, 8, 9]
perms = itertools.permutations(phases)
maxOutput = -1
for perm in perms:
    #Reset state for every permutation trial
    datas = [copy.deepcopy(sData) for x in range(5)]
    insPtrs = [0, 0, 0, 0, 0]
    inputPtrs = [0, 0, 0, 0, 0]
    sig = 0
    done = False
    while not done:
        for i,phase in enumerate(perm):
            out = runAmp(datas[i], phase, sig, insPtrs[i], inputPtrs[i])
            if isinstance(out, tuple):
                #unpack tuple
                datas[i], insPtrs[i], inputPtrs[i], sig = out
            else:
                sig = out
                done = True
    if sig > maxOutput:
        maxOutput = sig

print(maxOutput)