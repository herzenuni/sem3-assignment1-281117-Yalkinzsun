def summator(x):
    s = None
    try:
        if type(int(x)) is not int:
            raise TypeError
    except (ValueError, TypeError) as e:
        print(' {} �� �������� ����������� ������!'.format(x))
    else:
        s = 0
        for i in x:
            i = int(i)
            s += i
    return s


def main():
    y = input(' ������� ����������� ����: ')
    z = summator(y)
    print(' ����� ���� ����� {} ����� {}'.format(y, z))


main()
