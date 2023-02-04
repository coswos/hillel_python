a = int(input())
b = int(input())
c = int(input())
pupils = a + b + c
tables = []
if pupils % 2 == 1:
    tables = (pupils // 2) + 1
else:
    tables = pupils // 2

print(tables)