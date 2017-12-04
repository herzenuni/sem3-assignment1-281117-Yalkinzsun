#Author: Skorobogatov Kirill
#Программа способна возвращать числа произвольной длины (*)

def fun(x):
  list = []
  for i in x:
      i = str(i)
      s = 0
      for j in i:
          s += int(j)**2
      if 0 == s % 17:
          list.append(i)
  return list


def main():
    print(' Result: ', fun(range(1000,10000)))

if __name__ == '__main__':
    main()