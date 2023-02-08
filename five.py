dict = []
while True:
    x = int(input('enter an integer: '))
    dict.append(x)
    if x == int(0):
        break
dict.remove(0)
print('quantity of entered numbers: ', len(dict))
print('sum of entered numbers: ', sum(dict))
print('arithmetic mean of entered numbers: ', sum(dict) / len(dict))
t_sort = sorted(dict)
print('min number is: ', t_sort[0])
print('max number is: ', t_sort[-1])
for i in dict:
    if i % 2 == 0:
        print('it is a pair element: ', i)
for i in dict:
    if i % 2 == 1:
        print('it is not a pair: ', i)
