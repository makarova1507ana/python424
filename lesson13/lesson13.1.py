# # -------------практика------------------#
# '''
# Задача: У вас есть два набора клиентов: один, который купил продукт A, и другой, который купил продукт B. Найдите клиентов, которые купили оба продукта.
# Пример:
# Множество клиентов, купивших продукт A: {1001, 1002, 1003, 1004}
# Множество клиентов, купивших продукт B: {1003, 1004, 1005, 1006}
# Результат: {1003, 1004}
# '''
# set_A = {1001, 1002, 1003, 1004}
# set_B = {1003, 1004, 1005, 1006}
#
# print(f'Клиенты которые купили оба продукта {set_A & set_B}')
#
#
#
#



#
# # ------------------------------------- Задача ------------------------------------------------#
# '''
# - **Условие**:
# У каждого пирата есть карта, которая представлена
# в виде словаря, где ключ — это остров,
#  а значение — это количество зарытых сокровищ на этом острове.
# Необходимо написать программу,
# которая найдёт остров с максимальным количеством сокровищ.
#
# Данные для примера:
# {"Остров Сокровищ": 5,
# "Необитаемый остров": 3,
# "Остров Снов": 7}`
#
# -> "Остров Снов"
# '''
# # islands = {"Остров Сокровищ": 5, "Необитаемый остров": 3, "Остров Снов": 7}
# # max_val = max(islands.values())
# # for key, value in islands.items():
# #     if value == max_val:
# #         print(key, value)
# #         break
#
# # ---- 2 -----#
# islands = {"Остров Сокровищ": 5, "Необитаемый остров": 3, "Остров Снов": 7}
# keys = list(islands.keys())
# values = list(islands.values())
# max_value = max(values)
# index_max_value = values.index(max_value)
# print(keys[index_max_value])


# # ---- 3 -----#
# islands = {"Остров Сокровищ": 5, "Необитаемый остров": 3, "Остров Снов": 7}
# pirat = max(islands, key=islands.get) # islands.get - ссылка на метод по получению ключа
# print(islands.get("Остров Сокровищ")) # islands.get("Остров Сокровищ") == islands["Остров Сокровищ"]



# # пример
# '''
# key - принимает ссылку на функцию или метод
# '''
# print(max(("pytha", "lua", "zuby")))
# print(max(("pytha", "lua", "ruby"), key=len)) # len - ссылка





#—------------------------------- Задача —--------------------------------#
'''
Дан список строк такого формата :
"Имя: Яблоки, рублей за кг: 25, всего кг: 10”,
"Имя: Груши: рублей за кг: 50, всего кг: 100”,
"Имя: Молоко, рублей за шт: 5, всего шт: 200”

Найти общуюю сумму
6250
'''
strings = [ "Имя: Яблоки, рублей за кг: 25, всего кг: 10",
"Имя: Груши, рублей за кг: 50, всего кг: 100",
"Имя: Молоко, рублей за кг: 5, всего кг: 200" ]


#  "Имя: Яблоки, рублей за кг: 25, всего кг: 10" -> {'Имя': 'Яблоки'
#                                                    'рублей за кг': 25,
#                                                    'всего кг': 10}

# print(strings[0].find('Имя'))
# print(strings[0].find(':'))
products = []
for i in range(len(strings)):
    start = strings[i].find('Имя')
    end = strings[i].find(':')
    name = strings[i][start:end]
    start = strings[i].find(':')
    end = strings[i].find('рублей за кг')
    value_name = strings[i][start+1:end-2]
   # print(name, value_name)
    
    start = strings[i].find('рублей за кг')
    strings[i] = strings[i].replace(':', '*', 1)
    end = strings[i].find(':')
    cost = strings[i][start:end]
    
    start = strings[i].find(':')
    end = strings[i].find('всего кг')
   # print(strings[i][start+1:end-2])
    value_cost = int(strings[i][start+1:end-2])
    #print(cost, value_cost)
    
    
    
    start = strings[i].find('всего кг')
    strings[i] = strings[i].replace(':', '*', 1)
    end = strings[i].find(':')
    weight = strings[i][start:end]
    
    start = strings[i].find(':')
    value_weight = int(strings[i][start+2:])
   # print(weight, value_weight)
    
    product = {name: value_name, cost: value_cost, weight:value_weight}
    products.append(product)

print(products)

#!!! дорешать найти общую сумму уже из словаря products