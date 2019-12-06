def findAdd(raw, d, root):
    # find the number of children of node root, and add them as values to the dictionary, then recursively call
    childIdx = [i for i, x in enumerate(raw) if x[0] == root]
    # break condition for recursion: has no children
    if not len(childIdx):
        return d
    # if there is more than one child, add them
    else:
        newLen = d[root][0] + 1
        for i in childIdx:
            newVal = raw[i][1]
            d[newVal] = (newLen, root)
            findAdd(raw, d, newVal)
        return d


def findCommonAncestor(D, k1, k2):
    # If k1, k2 have the same parent
    if D[k1][1] == D[k2][1]:
        return D[k1][1]
    # If k1, k2 are not near each other, traverse up the tree
    elif abs(D[k1][0] - D[k2][0]) > 0:
        diff = D[k1][0] - D[k2][0]
        if diff > 0:
            for i in range(diff):
                k1 = D[k1][1]
        else:
            for i in range(-diff):
                k2 = D[k2][1]
        return findCommonAncestor(D, k1, k2)
    else:
        return findCommonAncestor(D, D[k1][1], D[k2][1])


data = [x.split(')') for x in open('6.txt','r').read().split('\n')]
D = {'COM':(0,'')}
D = findAdd(data, D, 'COM')

# We find YOU and SAN, then find their common ancestor
com = findCommonAncestor(D,'YOU','SAN')
dist = (D['YOU'][0] - D[com][0] - 1) + (D['SAN'][0] - D[com][0] - 1)
print(dist)