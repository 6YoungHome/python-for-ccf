n, m = map(int, input().split())
order_list = []
mat_list = []
in_list = []

def run_order(order):
    operate = order[0]
    if operate != 3:
        mat = order[1]
    if operate == 1:
        mat_list.insert(0, mat)
        in_list.append(operate)
    elif operate == 2:
        mat_list.append(mat)
        in_list.append(operate)
    elif operate == 3:
        pre_in = in_list.pop()
        if pre_in == 1:
            mat_list.pop(0)
        elif pre_in == 2:
            mat_list.pop()
    else:
        print("Error!!!")

def parse_key(mat_list):
    if len(mat_list) == 0:
        mat = [1,1,1,1]
    elif len(mat_list) == 1:
        mat = mat_list[0]
    else:
        mat = mat_list[0]
        for i in range(1, len(mat_list)):
            mat = mat_multi(mat, mat_list[i])
    print(mat[0]%998244353, mat[1]%998244353, mat[2]%998244353, mat[3]%998244353)

def mat_multi(x, y):
    a = x[0] * y[0] + x[1] * y[2]
    b = x[0] * y[1] + x[1] * y[3]
    c = x[2] * y[0] + x[3] * y[2]
    d = x[2] * y[1] + x[3] * y[3]
    return [a,b,c,d]
    
for _ in range(n):
    order = list(map(int, input().split()))
    if order[0] == 3:
        order_list.append((3))
    else:
        order_list.append((order[0], [order[1], order[2], order[3], order[4]]))

for _ in range(m):
    order = list(map(int, input().split()))
    if order[0] == 2:
        for i in range(order[1]-1, order[2]):
            run_order(order_list[i])
        
        parse_key(mat_list)
        mat_list = []
        
    elif order[0] == 1:
        if order[2] == 3:
            order_list[order[1]-1] = (3,)
        else:
            order_list[order[1]-1] = (order[2],[order[3], order[4], order[5], order[6]])


