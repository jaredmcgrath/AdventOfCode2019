start = 353096
end = 843212

def isValid(n):
    num = str(n)
    hasDouble = False
    for i in range(1,len(num)):
        if int(num[i-1]) > int(num[i]):
            return 0
        if num[i-1] == num[i]:
            hasDouble = True
    if hasDouble:
        return 1
    else:
        return 0

count = 0
for n in range(start,end+1):
    count += isValid(n)

print(count)
