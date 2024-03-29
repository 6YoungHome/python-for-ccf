n, m = map(int, input().split())

depends = list(map(int, input().split()))

days = list(map(int, input().split()))

earlys = [1] * m
for i in range(m):
    if depends[i] != 0:
        depend = depends[i]
        while depend != 0:
            earlys[i] += days[depend-1]
            depend = depends[depend-1]
        

print(' '.join([str(i) for i in earlys]))

stop = False
for i in range(m):
    if earlys[i] + days[i] - 1 > n:
        stop = True
        break
    

if not stop:
    latest = [0] * m
    re_depends = [0] * m
    for i in range(m-1, -1, -1):
        tmp = 366
        for j in range(i+1, m):
            if depends[j] == i+1:
                tmp = min(tmp, latest[j])
        if tmp == 366:
            latest[i] = n - days[i] + 1
        else:
            latest[i] = tmp - days[i]
    print(' '.join([str(i) for i in latest]))
    
