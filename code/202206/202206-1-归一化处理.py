import math

n = int(input())
nums = list(map(int, input().split()))

mu = sum(nums)/n
d = math.sqrt(sum([(num - mu) ** 2 for num in nums])/n)

for i in range(n):
    print((nums[i]-mu)/d)