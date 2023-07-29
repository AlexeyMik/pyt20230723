# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.
#
# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
#
laa = "2 4 6 8 10 12 10 8 6 4 2".split() # создает список из слов, считая пробел разделителем
lbb = "3 6 9 12 15 18".split()
sa = set(laa) # из списка создает 1-е множество
sb = set(lbb) # из списка создает 2-е множество
s = sa.intersection(sb) # находим пересечение множеств
print(s)
listRes= list(s) # из элементов мнжества делаем список 
print("сначала в лексикографическом порядке: обычно отличается от порядка по возрастанию")
print(*sorted(listRes)) # печать слов списка (пересечения) в лексикографическом порядке
for i in range(len(listRes)) :
    listRes[i] = int(listRes[i]) # каждый элемент списка преобразуем в целое число
print("числа из списка пересечения в порядке возрастания величин чисел")
print(*sorted(listRes)) # печать чисел из списка (пересечения) в порядке возрастания (величин) чисел