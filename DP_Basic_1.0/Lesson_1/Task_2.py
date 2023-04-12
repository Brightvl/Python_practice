real_number = input("Введите вещественное число -> ")
for idx in range(len(real_number)):
    if real_number[idx] == "." or real_number[idx] == ",":
        print(real_number[idx + 1])
