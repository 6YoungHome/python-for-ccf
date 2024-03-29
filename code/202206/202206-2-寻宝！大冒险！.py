# n, l, s = map(int, input().split())

# a = [[0]*(l+1) for _ in range(l+1)]
# for _ in range(n):
#     x, y = map(int, input().split())
#     a[x][y] = 1

# b = [[0]*(s+1) for _ in range(s+1)]
# for i in range(s, -1, -1):
#     tmp = list(map(int, input().split()))
#     for j in range(s+1):
#         b[i][j] = tmp[j]
# b = tuple(tuple(i) for i in b)
        
# def get_slice(ts, i, j, s):
#     return tuple([tuple(t[j:j+s]) for t in ts[i:i+s]])

# ans = 0
# for i in range(0, l-s+1):
#     for j in range(0, l-s+1):
#         part = get_slice(a, i, j, s+1)
#         if part == b:
#             ans += 1

# print(ans)

n, l, s = map(int, input().split())
trees = set([tuple(map(int, input().split())) for i in range(n)])

trees2 = []
b = [[0]*(s+1) for _ in range(s+1)]
for i in range(s, -1, -1):
    tmp = list(map(int, input().split()))
    for j in range(s+1):
        if tmp[j] == 1:
            trees2.append((i, j))
map_tree_count = len(trees2)

def count_trees_in(trees, x, y, s):
    count = 0
    for i, j in trees:
        if i >= x and j >= y:
            if i <= x+s and j <= y+s:
                count += 1
    return count

ans = 0
for x, y in trees:
    if x+s > l:
        continue
    stop = False
    for x_, y_ in trees2:
        if (x_+x, y+y_) not in trees:
            stop = True
            break
    if not stop and map_tree_count == count_trees_in(trees, x, y, s):
        ans += 1
    
print(ans)
            

