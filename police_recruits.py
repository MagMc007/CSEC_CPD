n = int(input())
events = list(map(int, input().split()))
crimes = 0
cops = 0
for i in events:
    if i == -1:
        if cops > 0:
            cops -= 1
        else:
            crimes += 1

    else:
        cops += i
        
print(crimes)
