n, x = map(int, input().split())
a = [int(input()) for _ in range(n)]

a.sort()

ans = []

pre_sum = [sum(a[0:i]) for i in range(n+1)]

def dfs(book, sum_price):
    if sum_price >= x:
        ans.append(sum_price)
        return
    if book >= n:
        return
    if pre_sum[n] - pre_sum[book+1] + sum_price < n:
        return 
    dfs(book+1, sum_price)
    dfs(book+1, sum_price+a[book])
    
dfs(0, 0)
print(min(ans))

