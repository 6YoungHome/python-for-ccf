n, m = map(int, input().split())

ops = [tuple(map(int, input().split())) for _ in range(n)]

for i in range(m):
    x, y = map(int, input().split())
    for op in ops:
        x += op[0]
        y += op[1]
    print(x, y)