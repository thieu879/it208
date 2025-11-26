numbers = [1, 2, 3, 2, 5, 1, 7, 9, 9, 4]
print(f"List ban đầu: {numbers}")

even_positions = numbers[::2]
print(f"Các vị trí chẵn: {even_positions}")

numbers_tuple = tuple(numbers)
print(f"Tuple: {numbers_tuple}")

numbers_dict = {index: value for index, value in enumerate(numbers)}
print(f"Dict: {numbers_dict}")

numbers_set = set(numbers)
print(f"Set: {numbers_set}")

duplicates_removed = len(numbers) - len(numbers_set)
print(f"Số phần tử bị loại trùng: {duplicates_removed}")
