from math import cos, pi, sqrt
q = [list(map(int, input().split())) for _ in range(8)]
n = int(input())
t = int(input())
d = list(map(int,(input().split())))

m = [[0]*8 for _ in range(8)]
m2 = [[0]*8 for _ in range(8)]
def get_next_pos(x, y):
    if x == 7 and y % 2 != 1:
        return x, y+1
    elif y == 7 and x % 2 == 1:
        return x+1, y
    elif x == 0 and y % 2 != 1:
        return x, y+1
    elif y == 0 and x % 2 == 1:
        return x+1, y
    elif (x+y) % 2 == 1:
        return x+1, y-1
    else:
        return x-1, y+1

if t == 0:
    x, y = 0, 0
    for i in range(min(n,64)):
        m[x][y] = d[i]
        x, y = get_next_pos(x, y)
    for i in m:
        print(" ".join([str(j) for j in i]))
        
elif t == 1:
    x, y = 0, 0
    for i in range(min(n,64)):
        m[x][y] = d[i]*q[x][y]
        x, y = get_next_pos(x, y)
    for i in m:
        print(" ".join([str(j) for j in i]))

elif t == 2:
    x, y = 0, 0
    try:
        for i in range(min(n,64)):
            m[x][y] = d[i]*q[x][y]
            x, y = get_next_pos(x, y)
        for i in m:
            print(" ".join([str(j) for j in i]))
    except:
        print(x,y)

    for i in range(8):
        for j in range(8):
            ms = 0
            # This block of code is performing a 2D Discrete Cosine Transform (DCT) on the matrix `m`
            # to obtain a new matrix `m2`.
            for u in range(8):
                au = 0.5**0.5 if u==0 else 1
                for v in range(8):
                    av = 0.5**0.5 if v==0 else 1
                    ms += au*av*m[u][v]*cos(pi*(i+0.5)*u/8)*cos(pi*(j+0.5)*v/8)
            tmp = 0.25*ms+128
            tmp1, tmp2 = int(tmp), tmp-int(tmp)
            if tmp2 >= 0.5:
                tmp = tmp1+1
            else:
                tmp = tmp1
            tmp = 255 if tmp > 255 else tmp
            tmp = 0 if tmp < 0 else tmp
            m2[i][j] = tmp
            
    for i in m2:
        print(" ".join([str(j) for j in i]))

