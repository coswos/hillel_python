a = 'abcdefghij'

print(a[2])
print(a[-2])
print(a[:5])
print(a[:-2])
for i in range(len(a)):
    if i % 2 == 1:
        print(a[i])

print('----- ----- -----')
for i in range(len(a)):
    if i % 2 == 0:
        print(a[i])

print(a[::-1])
print(a[::-2])
print(len(a[::-2]))
