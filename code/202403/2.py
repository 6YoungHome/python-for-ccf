n, m = map(int, input().split())
a = set([i.strip().lower() for i in input().split()])
b = set([i.strip().lower() for i in input().split()])

abb = a.union(b)
ajb = a.intersection(b)


print(len(ajb))
print(len(abb))