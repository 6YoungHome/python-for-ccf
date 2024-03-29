def all_large(l1, l2, m):
    for k in range(m):
        if l1[k] <= l2[k]:
            return False
    return True

n, m = map(int, input().split())
loc_list = [tuple(map(int, input().split())) for _ in range(n)]

for i in range(n):
    output = 0
    for j in range(n):
        if (j != i) and all_large(loc_list[j], loc_list[i], m):
            output = j+1
            break
    print(output)