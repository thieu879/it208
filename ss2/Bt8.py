a = int(input("nhập a: "))
b = int(input("nhập b: "))
c = int(input("nhập c: "))
if a + b > c and a + c > b and b + c > a:
    print("3 cạnh trên có thể tạo thành tam giác")
else:
    print("3 cạnh trên không thể tạo thành tam giác")