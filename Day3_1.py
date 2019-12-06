import copy
data = open('3.txt','r').read().split('\n')

vWire1 = []
hWire1 = []
vWire2 = []
hWire2 = []

wire1 = data[0].split(',')
pos = [0, 0]
for piece in wire1:
    oldPos = copy.deepcopy(pos)
    dir = piece[0]
    mag = int(piece[1:])
    if dir == 'U':
        pos[1] += mag
        vWire1.append([*oldPos, *pos])
    elif dir == 'D':
        pos[1] -= mag
        vWire1.append([*oldPos, *pos])
    elif dir == 'R':
        pos[0] += mag
        hWire1.append([*oldPos, *pos])
    else:
        pos[0] -= mag
        hWire1.append([*oldPos, *pos])

wire2 = data[1].split(',')
pos = [0, 0]
for piece in wire2:
    oldPos = copy.deepcopy(pos)
    dir = piece[0]
    mag = int(piece[1:])
    if dir == 'U':
        pos[1] += mag
        vWire2.append([*oldPos, *pos])
    elif dir == 'D':
        pos[1] -= mag
        vWire2.append([*oldPos, *pos])
    elif dir == 'R':
        pos[0] += mag
        hWire2.append([*oldPos, *pos])
    else:
        pos[0] -= mag
        hWire2.append([*oldPos, *pos])

intersections = []
# we know y coordinate of all horizontal wires are the same
# and all x coordinates of vertical wires are the same
for hw in hWire1:
    for vw in vWire2:
        if ((hw[0] <= vw[0] and hw[2] >= vw[0]) or (hw[2] <= vw[0] and hw[0] >= vw[0])) and ((vw[1] <= hw[1] and vw[3] >= hw[1]) or (vw[3] <= hw[1] and vw[1] >= hw[1])):
            intersections.append((vw[0],hw[1]))

for hw in hWire2:
    for vw in vWire1:
        if ((hw[0] <= vw[0] and hw[2] >= vw[0]) or (hw[2] <= vw[0] and hw[0] >= vw[0])) and ((vw[1] <= hw[1] and vw[3] >= hw[1]) or (vw[3] <= hw[1] and vw[1] >= hw[1])):
            intersections.append((vw[0],hw[1]))

mags = [abs(x[0]) + abs(x[1]) for x in intersections]
print(min(mags))