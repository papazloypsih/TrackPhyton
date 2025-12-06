numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
sum_numbers = sum(numbers[0:4])+sum(numbers[5:])
count_numbers = len(numbers)
average_of_numbers = (sum_numbers / count_numbers)
numbers[4] = average_of_numbers
print("Измененный список:", numbers)
