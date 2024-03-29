def jz_cheng(a, b):
    x = len(a)
    y = len(b)
    z = len(b[0])
    ans = [[0]*z for _ in range(x)]
    for i in range(x):
        for j in range(z):
            for k in range(y):
                ans[i][j] += a[i][k] * b[k][j]
    return ans

def xl_cheng(w, a):
    x = len(w)
    for i in range(x):
        for j in range(len(a[0])):
            a[i][j] *= w[i]
    return a

def jz_t(a):
    at = [[0] * len(a) for _ in range(len(a[0]))]
    for i in range(len(a)):
        for j in range(len(a[0])):
            at[j][i] = k[i][j]
    return at

n, d = map(int, input().split())

q = [list(map(int, input().split())) for _ in range(n)]
k = [list(map(int, input().split())) for _ in range(n)]
k = jz_t(k)
v = [list(map(int, input().split())) for _ in range(n)]

w = list(map(int, input().split()))

tmp = jz_cheng(q, k)
tmp = xl_cheng(w, tmp)
tmp = jz_cheng(tmp, v)

for i in tmp:
    print(' '.join(list(map(str, i))))
        