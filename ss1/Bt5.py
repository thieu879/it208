while True:
    n = input("Nhập một số thập phân (1 hoặc 0): ")
    if n == "1":
        value = True
        print("Giá trị boolean sau khi chuyển đổi là:", value)
        break
    elif n == "0":
        value = False
        print("Giá trị boolean sau khi chuyển đổi là:", value)
        break
    else:
        print("Lỗi: chỉ được nhập '1' hoặc '0'")
        break
