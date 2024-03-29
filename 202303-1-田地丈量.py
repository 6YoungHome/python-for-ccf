n, a, b = map(int, input().split())
points = [[i for i in map(int, input().split())] for j in range(n)]
sum = 0
for i in range(n):
    x = min(a, points[i][2])-max(0, points[i][0])
    y = min(b, points[i][3])-max(0, points[i][1])
    if x>=0 and y>=0:
        sum += x*y
print(sum)