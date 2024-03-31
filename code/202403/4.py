c, m, n = map(int, input().split())
l = [0]*c
for i in range(m):
    pos, w = map(int, input().split())
    l[pos-1] = w


def boom(pos):
    if l[pos] < 5:
        return
    l[pos] = 0
    pos_left = pos-1
    while pos_left >= 0 and l[pos_left] == 0:
        pos_left -= 1
    if pos_left >= 0:
        l[pos_left] += 1

    pos_right = pos + 1
    while pos_right < len(l) and l[pos_right] == 0:
        pos_right += 1
    if pos_right < len(l):
        l[pos_right] += 1

    if pos_left >= 0:
        boom(pos_left)
    if pos_right < len(l):
        boom(pos_right)

for i in range(n):
    op = int(input())
    l[op-1] += 1
    boom(op-1)
    print(len(l)-l.count(0))

# 5 5 2
# 1 2
# 2 4
# 3 4
# 4 4
# 5 2
# 3
# 1
