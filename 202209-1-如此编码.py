n, m = map(int, input().split())
a = list(map(int, input().split()))

c = [1] * (n+1)
for i in range(1, n+1):
    c[i] = c[i-1] * a[i-1]

b = []
pre_bi = 0
for i in range(1, n+1):
    bi = m % c[i]
    bi, pre_bi = round((bi-pre_bi)/c[i-1],0), bi
    b.append(bi)
    
print(" ".join([str(int(i)) for i in b]))