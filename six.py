list_square = []
a = 50
a_list = [1, 4, 9, 16, 25, 36, 49]

b = 10
b_list = [1, 4, 9]

c = 9
c_list = [1, 4, 9]

d = 4
d_list = [1, 4]

e = 1
e_list = [1]

f = 100
f_list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

g = 99
g_list = [1, 4, 9, 16, 25, 36, 49, 64, 81]


def square(list, var):
    for i in list:
        i1 = i * i
        list_square.append(i1)
    for i2 in list_square:
        if i2 <= var:
            print(f'this number is less than or equal to the number {var}: ', i2)
    list_square.clear()


square(a_list, a)
square(b_list, b)
square(c_list, c)
square(d_list, d)
square(e_list, e)
square(f_list, f)
square(g_list, g)
