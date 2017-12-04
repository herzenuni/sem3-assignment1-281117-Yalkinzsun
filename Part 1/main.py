def summator(x):
    s = None
    try:
        if type(int(x)) is not int:
            raise TypeError
    except (ValueError, TypeError) as e:
        print(' {} не является натуральным числом!'.format(x))
    else:
        s = 0
        for i in x:
            i = int(i)
            s += i
    return s


def main():
    y = input(' Введите натуральное чило: ')
    z = summator(y)
    print(' Сумма цифр числа {} равна {}'.format(y, z))


main()
