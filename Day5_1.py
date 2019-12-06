data = [int(x) for x in open('5.txt','r').read().split(',')]

inVal = 1
ins = 0
while data[ins]%100 != 99:
    if data[ins]%100 == 1:
        #add
        # only p1, p2 can be imm values
        p1 = data[ins+1] if (data[ins]%1000)//100 else data[data[ins+1]]
        p2 = data[ins+2] if data[ins]//1000 else data[data[ins+2]]
        data[data[ins+3]] = p1 + p2
        ins+=4
    elif data[ins]%100 == 2:
        #mul
        # only p1, p2 can be imm values
        p1 = data[ins + 1] if (data[ins]%1000) // 100 else data[data[ins + 1]]
        p2 = data[ins + 2] if data[ins] // 1000 else data[data[ins + 2]]
        data[data[ins + 3]] = p1 * p2
        ins+=4
    elif data[ins]%100 == 3:
        #input
        # can't have any imm vals
        data[data[ins+1]] = inVal
        ins +=2
    elif data[ins] %100 == 4:
        #output
        # p1 can be imm or ind
        p1 = data[ins + 1] if data[ins] // 100 else data[data[ins + 1]]
        print(p1)
        ins+=2



