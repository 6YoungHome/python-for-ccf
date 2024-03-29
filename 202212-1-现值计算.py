ni = input().split()
n = int(ni[0])
i = float(ni[1])
vs = list(map(float, input().split()))

pv = 0
for x in range(len(vs)):
    pv += (vs[x])/((1+i)**x)
print(pv)
