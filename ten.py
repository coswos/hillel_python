import random
a = [random.randint(0, 10) for x in range(10)]
res = []
print(a)

for i in range(1, len(a) - 1):
    if a[i] > a[i+1] and a[i] > a[i-1]:
        res.append(a[i])
print(res)
