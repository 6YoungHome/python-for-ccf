n, m, l, k = map(int, input().split())

c = list(map(int, input().split()))
u = list(map(int, input().split()))
v = list(map(int, input().split()))
d = list(map(int, input().split()))

aim_dict = {}
length_dict = {}
for i in range(m):
    if u[i] not in aim_dict:
        aim_dict[u[i]] = []
    aim_dict[u[i]].append(v[i])
    
    if u[i] not in length_dict:
        length_dict[u[i]] = {}
    length_dict[u[i]][v[i]] = d[i]

path_list = []
remain_pos = set([i for i in range(1, n)])
for i in range(1, n):
    if c[i] == c[0]:
        remain_pos.remove(i)

def find(pos, pos_list, remain_pos):
    if len(pos_list) > l:
        return
    remain_pos_new = remain_pos.copy()
    for i in remain_pos:
        if c[i] == c[pos]:
            remain_pos_new.remove(i)
    
    pos_list = pos_list + [pos]
    if pos == n-1:
        path_list.append(pos_list)
    if pos in aim_dict:
        aim_pos = [i for i in aim_dict[pos] if i in remain_pos_new]
        if aim_pos:
            for aim in aim_pos:
                find(aim, pos_list, remain_pos_new)
        
find(0, [], remain_pos)

max_length = 0
for path in path_list:
    length = 0
    for i in range(len(path)-1):
        length += length_dict[path[i]][path[i+1]]
    max_length = max(max_length, length)

print(max_length)