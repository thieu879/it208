n = int(input("nhập số: "))
if n > 0:
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    print("giai thừa =", factorial)
else:
    print("vui lòng nhập số dương")