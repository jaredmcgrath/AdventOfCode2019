import copy
data = open('3.txt','r').read().split('\n')

vWire1 = []
hWire1 = []
vWire2 = []
hWire2 = []
wire1 = data[0].split(',')

pos = [0, 0]
steps = 0
for piece in wire1:
    oldPos = copy.deepcopy(pos)
    dir = piece[0]
    mag = int(piece[1:])
    steps += mag
    if dir == 'U':
        pos[1] += mag
        vWire1.append([*oldPos, *pos, steps])
    elif dir == 'D':
        pos[1] -= mag
        vWire1.append([*oldPos, *pos, steps])
    elif dir == 'R':
        pos[0] += mag
        hWire1.append([*oldPos, *pos, steps])
    else:
        pos[0] -= mag
        hWire1.append([*oldPos, *pos, steps])

wire2 = data[1].split(',')
pos = [0, 0]
steps = 0
for piece in wire2:
    oldPos = copy.deepcopy(pos)
    dir = piece[0]
    mag = int(piece[1:])
    steps += mag
    if dir == 'U':
        pos[1] += mag
        vWire2.append([*oldPos, *pos, steps])
    elif dir == 'D':
        pos[1] -= mag
        vWire2.append([*oldPos, *pos, steps])
    elif dir == 'R':
        pos[0] += mag
        hWire2.append([*oldPos, *pos, steps])
    else:
        pos[0] -= mag
        hWire2.append([*oldPos, *pos, steps])

intersections = []
for hw in hWire1[1:]:
    for vw in vWire2:
        if ((hw[0] <= vw[0] and hw[2] >= vw[0]) or (hw[2] <= vw[0] and hw[0] >= vw[0])) and ((vw[1] <= hw[1] and vw[3] >= hw[1]) or (vw[3] <= hw[1] and vw[1] >= hw[1])):
            lastX = abs(vw[0]-hw[2])
            lastY = abs(hw[1] - vw[3])
            intersections.append((vw[0],hw[1],(vw[4]+hw[4]-lastX-lastY)))

for hw in hWire2[1:]:
    for vw in vWire1:
        if ((hw[0] <= vw[0] and hw[2] >= vw[0]) or (hw[2] <= vw[0] and hw[0] >= vw[0])) and ((vw[1] <= hw[1] and vw[3] >= hw[1]) or (vw[3] <= hw[1] and vw[1] >= hw[1])):
            lastX = abs(hw[2] - vw[0])
            lastY = abs(vw[3] - hw[1])
            intersections.append((vw[0],hw[1],(vw[4]+hw[4]-lastX-lastY)))

print(min([i[2] for i in intersections]))