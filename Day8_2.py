data = [int(x) for x in open('8.txt','r').read()]
w = 25
h = 6

mask = [[2 for x in range(w)] for y in range(h)]

for l in range(int(len(data)/(w*h))):
    for row in range(h):
        for col in range(w):
            if mask[row][col] == 2 and data[l*w*h + row*w + col] < 2:
                mask[row][col] = data[l*w*h + row*w + col]

for row in mask:
    print(''.join(['#' if col else '.' for col in row]))
