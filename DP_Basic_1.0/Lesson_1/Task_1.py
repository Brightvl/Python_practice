numeric_element = input("Введите любое число -> ")
for number in numeric_element:
    if number.isdigit():
        sum += int(number)
print(sum)
