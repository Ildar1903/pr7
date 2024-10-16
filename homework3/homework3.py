def dec_to_13(n):
    symbols = "0123456789AB"
    if n < 13:
        return symbols[n]
    else:
        return dec_to_13(n // 13) + symbols[n % 13]

dec_n = input("Введите целое неотрицательное десятичное число: ")
if str.isnumeric(dec_n):
    dec_n = int(dec_n)
    conv_n = dec_to_13(dec_n)
    print(f"{dec_n} в тринадцатиричной системе: {conv_n}")
else:
    print("Вы ввели не целое и/или отрицательное число, перезапустите и введите целое неотрицательное число")
