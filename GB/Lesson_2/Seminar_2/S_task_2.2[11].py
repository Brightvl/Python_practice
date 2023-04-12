# №2.2[11]. Дано натуральное число A > 1. 
# Определите, каким по счету числом Фибоначчи 
# оно является, то есть выведите такое число n, 
# что φ(n)=A. Если А не является числом Фибоначчи, 
# выведите число -1. 
# Примеры/Тесты:
# 5 -> в ряду Фибоначчи 5 имеет порядковый номер 6

number = 0
#int(input('Введите исло: ')) 
if number == 0:
    print(f'{number} - 1')
else:
    prev = 0
    cur = 1
    #flag = False
    for i in range(number):
        tmp = cur
        cur=cur+prev
        prev = tmp
        #c, b = b, c+b
        #print(, end=' ')
        if number == cur:
            print(f'{number} является {i+3} числом')
            # flag = True 
            break
    # if not flag:
    #     print('-1')
    #     # if cur > number:
    #     #     print('-1')
    #     #     break;


    else:
        print('-1')