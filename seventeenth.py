num = int(input('please enter a number greater than zero: '))

if num <= 0:
    raise Exception('number less than zero or zero')

last_num = num % 10  # последнее число (единицы)
ten = f'{(num % 100) // 10}0'  # целый десяток
hundred = f'{(num % 1000) // 100}00'  # сотни
k = f'{num // 1000}000'  # много тысяч


def print_all(num=num, k=k, hundred=hundred, ten=ten, last=last_num):
    print(
        k + ' + ' if int(k) != 0 else '',
        hundred + ' + ' if int(hundred) != 0 else '',
        ten + ' + ' if int(ten) != 0 else '',
        last if int(last) != 0 else '',
        sep=''
    )


print_all()
