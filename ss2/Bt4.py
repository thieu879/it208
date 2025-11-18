n = int(input("nhập số: "))
sum = 0
if n > 0:
    for i in range(1, n + 1):
        sum += i
    print("sum =", sum)
else:
    print("vui lòng nhập số dương")