number_collaps = 0
def sum_digits(num):
    # Складываем все цифры числа
    total = sum(int(digit) for digit in str(num))
    if num <= 0:
        raise Exception('digit less than zero')

    # Если получившееся число меньше 10, возвращаем его
    if total < 10:
        return total

    # Если получившееся число имеет более одной цифры, 
    # вызываем функцию sum_digits() рекурсивно
    return sum_digits(total)
    # print(sum_digits(total))


print(sum_digits(number_collaps))
