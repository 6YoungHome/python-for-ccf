from collections import defaultdict
n, m = map(int, input().split())

w_dict = defaultdict(defaultdict(int))
b_dict = defaultdict(defaultdict(int))
p_dict = defaultdict(defaultdict(int))
path_id = []

for i in range(n-1):
    u, v, w, b = map(int, input().split())
    w_dict[u][v] = w
    b_dict[u][v] = b
    p_dict[u][v] = w-b
    path_id.append((u,v))

dp = [[1] * n for _ in range(n)]
for i in range(n):
    1



