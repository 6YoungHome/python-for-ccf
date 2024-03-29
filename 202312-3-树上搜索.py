n, m = map(int, input().split())

w = list(map(int, input().split()))
p = list(map(int, input().split()))

t = [1] * n

def dfs_tree(node, sum_w):
    sum_w += w[node-1]
    for i in range(len(p)):
        if p[i] == node and t[i+1] == 1:
            sum_w = dfs_tree(i+2, sum_w)
            
    return sum_w
    


for i in range(m):
    aim_tag = int(input())
    quit_list = [1]
    ans = []
    class_now = 1
    aim_classes = [i+2 for i in range(n) if p[i]==class_now]
    min_delta = 100
    min_class = 1
    for aim_class in aim_classes:
        children = [aim_class]
        dfs_tree(aim_class)
        w1 = sum([w[i-1] for i in children])
        w2 = sum([w[i-1] for i in range(1, n+1) if i not in quit_list+children])
        if abs(w1-w2) < min_delta:
            min_class = aim_class
            min_delta = abs(w1-w2)
    ans.append(min_class)
    if aim_tag == min_class:
        
        
        