a = int(input("Nhập số kiểm tra đối xứng: "))
original = a
reversed = 0
while a > 0:
    digit = a % 10
    reversed = reversed * 10 + digit
    a = a // 10
if original == reversed:
    print("là số đối xứng")
else:
    print("không phải là số đối xứng")