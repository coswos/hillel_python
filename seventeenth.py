num = int(input('please enter a number greater than zero: '))

def number_collaps(num):
    if num <= 0:
        raise Exception('number less than zero or zero')
        # return "zero division"

    number = str(num)
    list1 = []
    for i in range(len(number)):
        if number[i] != "0":
            list1.append(number[i] + "0" * (len(number) - (i+1)))
    return "+".join(list1)


print(number_collaps(num))

