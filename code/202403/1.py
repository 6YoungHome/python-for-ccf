from collections import defaultdict

n, m = map(int, input().split())
cx_count1 = defaultdict(int)
cx_count2 = defaultdict(int)

for _ in range(n):
    tmp = list(map(int, input().split()))
    l = tmp[0]
    for word in tmp[1::]:
        cx_count1[word] += 1
    for word in set(tmp[1::]):
        cx_count2[word] += 1

for i in range(1, m+1):
    print(cx_count2[i], cx_count1[i])

