a = int(input("nhập số: "))
if a % 3 == 0 & a % 5 == 0:
    print("số chia hết cho 3 và 5")
elif a % 3 == 0:
    print("số chia hết cho 3")
elif a % 5 == 0:
    print("số chia hết cho 5")
else:
    print("số không chia hết cho 3 và 5")