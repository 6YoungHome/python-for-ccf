q = int(input())

for _ in range(q):
    n, k = map(int, input().split())
    n_ = n
    pre_n = n
    factor = []
    while n != 1:
        for i in range(2, int(n_**(1/k))+2):
            if n % i == 0:
                factor.append(i)
                n = n // i
                break
        if n == pre_n:
            break
        pre_n = n
    ans = 1
    for i in set(factor):
        if factor.count(i) >= k:
            ans *= (i ** factor.count(i))
    print(ans)