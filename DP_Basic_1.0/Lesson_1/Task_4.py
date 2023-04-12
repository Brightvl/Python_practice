four_digit_number = input("Введите четырехзначное число")

# 1. срезы в лоб
# print(f"{four_digit_number[-1]}"
#       f"{four_digit_number[1:-1]}"
#       f"{four_digit_number[0]}")

#  2. перестановка в списке
# my_list = list(four_digit_number)
# start_el = my_list[-1]
# my_list[-1] = my_list[0]
# my_list[0] = start_el
# print(my_list)

# 3. немного деления без остатка
# num_end = int(four_digit_number) % 10
# num_start = int(four_digit_number) // 1000
# print(f"{num_end}{four_digit_number[1:-1]}{num_start}")

# в падлу думать еще
