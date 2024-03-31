from collections import defaultdict

n, m = map(int, input().split())
f = [0] + list(map(int, input().split()))
d = list(map(int, input().split()))

tree = defaultdict(list)
for i in range(2, n+1):
    tree[f[i-1]].append(i)

deep = defaultdict(int)
deep[1] = 1
for i in range(2, n+1):
    deep[i] = deep[f[i-1]] + 1

ans = []

for _ in range(m):
    op, x = map(int, input().split())
    if op == 2:
        ans.append(str(deep[x]))
        continue

    x_sons = tree[x].copy()
    for x_son in x_sons:
        x_gsons = tree[x_son].copy()
        d[x - 1] += d[x_son - 1]
        for x_gson in x_gsons:
            tree[x].append(x_gson)
            deep[x_gson] -= 1
        tree[x].remove(x_son)
        # del deep[x_son]
    ans.append(f"{len(tree[x])} {d[x-1]}")

for i in ans:
    print(i)

# 4 6
# 1 1 3
# 100 0 200 300
# 2 1
# 2 4
# 1 1
# 2 4
# 1 1
# 1 1
#
# 11 3
# 1 1 2 2 3 3 4 4 5 5
# 100 100 100 100 100 100 100 100 100 100 100
# 1 4
# 2 4
# 1 2

# 11 2
# 1 1 2 2 3 3 4 4 5 5
# 100 100 100 100 100 100 100 100 100 100 100
# 1 4
# 2 4