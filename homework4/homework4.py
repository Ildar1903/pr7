a=input("Введите целое число a: ")
b=input("Введите целое число b: ")
c=input("Введите целое число c: ")
if str.isnumeric(a) and str.isnumeric(b)and str.isnumeric(c):
    a=int(a)
    b=int(b)
    c=int(c)
    x=7*b+2*c-a
    print('x = ',x)
else:
    print("Вы ввели не целое число, перезапустите и введите целое число")
