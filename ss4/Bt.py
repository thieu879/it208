products = {}


def add_product():
    code = input("Nhập mã sản phẩm: ").strip()
    name = input("Nhập tên sản phẩm: ").strip()
    price = float(input("Nhập giá sản phẩm: ").strip())
    quantity = int(input("Nhập số lượng sản phẩm: ").strip())
    products[code] = {
        "name": name,
        "price": price,
        "quantity": quantity
    }
    print("Sản phẩm đã được thêm thành công.")


def display_product():
    if not products:
        print("Danh sách sản phẩm trống.")
        return
    for code, info in products.items():
        print(
            f"Mã sản phẩm: {code}, Tên: {info['name']}, "
            f"Giá: {info['price']}, Số lượng: {info['quantity']}"
        )


def search_product():
    code = input("Nhập mã sản phẩm cần tìm: ").strip()
    if code in products:
        info = products[code]
        print(
            f"Mã sản phẩm: {code}, Tên: {info['name']}, "
            f"Giá: {info['price']}, Số lượng: {info['quantity']}"
        )

    else:
        print("Không tìm thấy sản phẩm với mã đã nhập.")


def update_product():
    code = input("Nhập mã sản phẩm cần cập nhật: ").strip()
    if code in products:
        name = input("Nhập tên sản phẩm mới: ").strip()
        price = float(input("Nhập giá sản phẩm mới: ").strip())
        quantity = int(input("Nhập số lượng sản phẩm mới: ").strip())
        products[code] = {
            "name": name,
            "price": price,
            "quantity": quantity
        }
        print("Sản phẩm đã được cập nhật thành công.")
    else:
        print("Không tìm thấy sản phẩm với mã đã nhập.")


def delete_product():
    code = input("Nhập mã sản phẩm cần xoá: ").strip()
    if code in products:
        del products[code]
        print("Sản phẩm đã được xóa thành công.")
    else:
        print("Không tìm thấy sản phẩm với mã đã nhập.")


while True:
    print("---------------menu---------------")
    print("1. Thêm sản phẩm mới.")
    print("2. Hiển thị danh sách sản phẩm.")
    print("3. Tìm kiếm sản phẩm theo mã sản phẩm.")
    print("4. Cập nhật thông tin sản phẩm.")
    print("5. Xóa sản phẩm theo mã sản phẩm.")
    print("0. Thoát chương trình.")
    
    choice = input("Nhập lựa chọn của bạn: ").strip()
    if choice == '1':
        add_product()
    elif choice == '2':
        display_product()
    elif choice == '3':
        search_product()
    elif choice == '4':
        update_product()
    elif choice == '5':
        delete_product()
    elif choice == '0':
        print("Thoát chương trình.")
        break
    else:
        print("Lựa chọn không hợp lệ. Vui lòng thử lại.")