def findAdd(raw, d, root):
    # find the number of children of node root, and add them as values to the dictionary, then recursively call
    childIdx = [i for i, x in enumerate(raw) if x[0] == root]
    # break condition for recursion: has no children
    if not len(childIdx):
        return d
    # if there is more than one child, add them
    else:
        newLen = d[root] + 1
        for i in childIdx:
            newVal = raw[i][1]
            d[newVal] = newLen
            findAdd(raw, d, newVal)
        return d


data = [x.split(')') for x in open('6.txt','r').read().split('\n')]
D = {'COM':0}
D = findAdd(data, D, 'COM')

print(sum(D.values()))