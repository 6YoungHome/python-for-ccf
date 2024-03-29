n, m, k = map(int, input().split())
bdz = []
for _ in range(n):
    bdz.append(list(map(int, input().split())))

t = [[0]*k for _ in range(k)]
t_dict = {}
for _ in range(m):
    tmp = list(map(int, input().split()))
    