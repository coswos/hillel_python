number_collaps = 8127192823
def sum_digits(num):
    # Складываем все цифры числа
    total = sum(int(digit) for digit in str(num))

    # Если получившееся число меньше 10, возвращаем его
    if total < 10:
        return total

    # Если получившееся число имеет более одной цифры, 
    # вызываем функцию sum_digits() рекурсивно
    return sum_digits(total)
    # print(sum_digits(total))


print(sum_digits(number_collaps))
