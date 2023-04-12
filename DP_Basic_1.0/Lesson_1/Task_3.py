decimal_number = int(input("Введите десятичное число -> "))

binary_number = ""
while decimal_number > 0:
    binary_number = str(0 if decimal_number % 2 == 0 else 1) + binary_number
    decimal_number //= 2
print(binary_number)

# Или так
# binary_number = bin(decimal_number)[2:]
