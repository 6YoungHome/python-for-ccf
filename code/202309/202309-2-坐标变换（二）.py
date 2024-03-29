from math import sin, cos

n, m = map(int, input().split())

k = 1
t = 0
ops = [(1, 0)]
for _ in range(n):
    op = tuple(map(float, input().split()))
    if op[0] == 1:
        k *= op[1]
        ops.append((k, t))
    else:
        t += op[1]
        ops.append((k, t))

for _ in range(m):
    i, j, x, y = map(int, input().split())

    k = ops[j][0] / ops[i-1][0]
    t = ops[j][1] - ops[i-1][1]

    x1 = (x * cos(t) - y * sin(t)) * k
    y1 = (x * sin(t) + y * cos(t)) * k
    print(x1, y1)

