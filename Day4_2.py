start = 353096
end = 843212

def isValid(n):
    num = str(n)
    hasDouble = False
    hasValidDouble = False
    lastWasRepeat = False
    for i in range(1,len(num)):
        if int(num[i-1]) > int(num[i]):
            return 0
        if num[i-1] == num[i] and lastWasRepeat:
            hasDouble = False
        elif num[i-1] == num[i] and not lastWasRepeat:
            hasDouble = True
            lastWasRepeat = True
        if hasDouble and num[i-1] != num[i]:
            hasValidDouble = True
            lastWasRepeat = False
            hasDouble = False
        if num[i-1] != num[i]:
            lastWasRepeat = False
    if hasValidDouble or hasDouble:
        return 1
    else:
        return 0

count = 0
for n in range(start,end+1):
    count += isValid(n)

print(count)
