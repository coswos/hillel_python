a = 123

a1 = a // 100
a2 = (a // 10) % 10
a3 = a % 10

res = [a3, a2, a1]
res1 = ''.join(map(str,res))
print(res1)
