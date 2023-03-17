# Задача 18: Требуется найти в массиве A[1..N] 
# самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное 
# число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. 
# Последняя строка содержит число X
# *Пример:*
# 5
# 1 2 3 4 5
# 6
# -> 5

numbers = [1, 3, 6, 5, 3, 8, 10, 1, 9, 8, 3, 3]
numbers.sort()
set_numbers = set(numbers)
poisk_a = int(input("Введите число для поиска ближайшего: "))
count = 1

for num in set_numbers:
    if poisk_a == num:
        print("Ваше число есть в списке.")
        break
 
    else:
        if num - poisk_a == count:
            print("Ближайшее число: ", num)
            count += 1
            break
    
    
        
if num - poisk_a < 0:
    last_element = numbers[-1]
    print("Ближайшее число: ", last_element)