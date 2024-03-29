from collections import defaultdict
n = int(input())
p = list(map(int, input().split()))
a = list(map(int, input().split()))

tx = defaultdict(set)
ax = defaultdict(list)

for i in range(n, 1, -1):
    tx[i].add(i)
    tx[p[i-2]] = tx[p[i-2]].union(tx[i])
tx[1] = set([i for i in range(1,n+1)])

sqrs = defaultdict(defaultdict(int))
for i in range(n):
    for j in range(i+1, n):
        sqrs = (a[i]-a[j])**2

for x in range(1, n+1):
    ansx = 0
    for y in tx[x]:
        sqrs = [(a[z-1]-a[y-1])**2 for z in tx[x] if z != y]
        if sqrs:
            ansx += min(sqrs)
    print(ansx)