#—------------------------------- Задача —--------------------------------#
'''
Вы обнаружили таинственную коробку с сокровищами.
На коробке написан сумма драгоценности (число), которую вы ищете.
Найдите драгоценность среди всех сокровищ(список чисел).
Если его нет, вам нужно написать “нет такого сокровища”,
если есть то вернуть номер драгоценности (на каком оно месте? ТОЛЬКО ПЕРВОЕ попашиеся).
'''

'''
пример
 [100, 500, 333, 300, 400, 333]
 число, которое ищем: 333
 
 вывод: индекс = 2 или нумерация по порядку = 3
 
 пример
  [100, 500, 333, 300, 400, 333]
 число, которое ищем: 555
 
 вывод: нет такого сокровища
'''


''' 1  способ '''
# treasures = [100, 500, 333, 300, 400, 333]
# target_treasure = 333 # можно и через input сделать
# index = 0
# # перебрать все элементы в списке treasures
# for num in treasures:
#     if num == target_treasure:
#         print(num, 'index = ', index)
#         break
#     index += 1
# else: # сработает тогда, когда цикл закончиться И опертор break не был вызван
#     print('Нет такого сокровища')



''' 2  способ '''
# treasures = [100, 500, 333, 300, 400, 333]
# target_treasure = 333
#
# # Есть ли target_treasure В (среди) treasures?
# # print(f' if {target_treasure} in {treasures} ? \n{target_treasure in treasures} ')
#
# if target_treasure in treasures:
#     # treasures.index(target_treasure) ->  вернет индекс элемента, который ищем
#     print(f' индекс = {treasures.index(target_treasure)}')
# else:
#     print('Нет такого сокровища')


#—------------------------------- Задача —--------------------------------#
'''
На складе накопилось много ненужных предметов (список чисел). 
Вам нужно избавиться от всех предметов, 
которые вам больше не нужны и заменить их на 0, 
это все нечетные по порядку предметы.


пример
исходные: [1, 43, 44, 56, 91]
вывод: [0, 43, 0, 56, 0]
'''
#-------пример с заменой элемента в списке---------#
# items = [1, 43, 44, 56, 91]
# print(items)
# items[0] = 0
# print(items)


# items = [1, 43, 44, 56, 91]
# for i in range(len(items)): # перебираем индексы 0, 1, 2, 3, 4 для примера [1, 43, 44, 56, 91]
#     if (i + 1) % 2 != 0:
#         items[i] = 0
# print(items)





#—------------------------------- Задача —--------------------------------#
'''
Ваше приключение на этом острове имеет две части: 
первая часть – это исследования на четных островах, 
а вторая – на нечетных. Разделите свои заметки так, 
чтобы все четные приключения были в одном списке,
 а нечетные – в другом. Теперь вам будет легче организовать 
 свои воспоминания.
 
пример:
[34, 32, 33, 8, 5, 38]

четные приключения: [34, 32, 8, 38]
нечетные приключения: [33, 5]
'''
# islands = [34, 32, 33, 8, 5, 38]
# even_adventure = [] # четные приключения
# odd_adventure = [] # нечетные приключения
#
# for island in islands:
#     if island % 2 == 0:
#         even_adventure.append(island)
#     else:
#         odd_adventure.append(island)
#
# print(even_adventure)
# print(odd_adventure)


#—------------------------------- кортежи, множества, словари —--------------------------------#
'''
в коллекции - лежит сразу много значений
list список
tuple кортеж
set множество
dictionary словарь
'''
# -------------кортежи tuple--------------#
'''
кортеж - это тоже что и список, но его нельзя редактировать (неизменяемый список)

можно:  
    * создать
    * перебирать элементы через for
нельзя:
    * добавить элементы
    * редактировать/изменять элементы
    * удалять элементы


назначение: хранить элементы без изменений
'''
# t = (1, 2, 'hello', True, 0.5)
# print(t, type(t))
# t[0] = 0 #TypeError: 'tuple' object does not support item assignment


'''
ГОЛОВОЛОМКА

'''
#------------
# t = (1, 2, 'hello', True, 0.5)
# print(t)
# t = (8, 4) # Перезапись в переменную делать можно
# print(t)


# -----------
# t = (1, 2, [5, 44], 'hello', True, 0.5)
# print(t)
# #t[2] = 'новый элемент' #TypeError: 'tuple' object does not support item assignment
# t[2][0] = 'новый элемент' # но так можно, потому что работаете со списоком,а не с кортежем
# print(t)



# -------------set множество--------------#
'''
множество - это уникальный элементов
 можно:
    * добавить (кроме дубликатов)
    * удалить
    * можно перебирать через цикл for 
    
нельзя:
    * нельзя обратить по индексу(нет индексов)
    * редактировать элементы
    * хранить определнные типы данных (см документацию)
    
для чего используем:
    когда нужно избавить от дубликатов 
    задачи на сопостовления множетсв 
'''
# s = {1, 2, '432', 76, 89}
# print(s, type(s))




#—------------------------------- Задача —--------------------------------#

'''
Вы состоите в тайном клубе, где каждый член клуба имеет свой 
уникальный номер. Вы решили провести ревизию и удалить всех членов,
 которые посещали клуб более одного раза. 
 Составьте новый список, в котором будут только уникальные участники.

пример:
[1, 432, 56, 89, 1, 1, 89 ]

вывод: [432, 56]
'''
# # определить уникальные числа в списке
# members = [1, 432, 56, 89, 1, 1, 89]
# unique_members = set(members)
# print(members, unique_members)
#
#
# # какое из чисел встречается два и более раза
# for num in unique_members:
#     print(num, 'кол-во: ', members.count(num))
#     if members.count(num) >= 2:
#         while num in members:
#             members.remove(num)
# print(members)




#—------------------------------- Задача —--------------------------------#
# Петя случайно добавил в список продуктов повторяющиеся продукты.
# Помогите Пете оставить список только из неповторяющихся продкутов (порядок не важен)
'''
пример:
["яблоки", "молоко", "хлеб", "яйца", "яблоки", "яблоки", "масло", "мука", "молоко"]

уникальные товары без повторений:
["яблоки", "молоко", "хлеб", "яйца", "масло", "мука"]

'''
# products = ["яблоки", "молоко", "хлеб", "яйца", "яблоки", "яблоки", "масло", "мука", "молоко"]
#
# unique_products = set(products)
# unique_products = list(unique_products)
#
# unique_products.sort()
# print(unique_products)


#—------------------------------- Задача —--------------------------------#
'''
Есть два списка чисел. 
Необходимо опредлить элементы, которые встречаются в обоих списках

пример:
[5, 1, 2, 3, 1]
[2, 1, 8, 9, 2]

вывод: [2, 1]
'''
s1 = [5, 1, 2, 3, 1]
s2 = [2, 1, 8, 9, 2]

s1 = set(s1)
s2 = set(s2)

print(f'{s1} & {s2} = {s1 & s2}') # элементы, которые встречаются в обоих списках
print(f'{s1} - {s2} = {s1 - s2}') # элементы, которые встречаются в s1  /# элементы, которые не встречаются в s2
print(f'{s2} - {s1} = {s2 - s1}') # элементы, которые встречаются в s2 / # элементы, которые не встречаются в s1
print(f'{s2} ^ {s1} = {s2 ^ s1}') # элементы, которые не встречаются в  s2  и в s1
print(f'{s2} | {s1} = {s2 | s1}') # все элементы
