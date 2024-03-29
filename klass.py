# Задание 1
# class Avtomobil:
#     '''описание автомобиля'''
#     def __init__(self, model, year, gen, vol, color, price):
#         '''характеристики'''
#         self.model = model
#         self.year = year
#         self.gen = gen
#         self.vol = vol
#         self.color = color
#         self.price = price
#
#     '''вывод красивенько описание'''
#     def info(self):
#         print(f"Марка машины: {self.model} \n"
#               f"Год выпуска: {self.year} \n"
#               f"Производитель: {self.gen} \n"
#               f"Обьем двигателя: {self.vol} \n"
#               f"Цвет: {self.color} \n"
#               f"Цена: {self.price} \n")
#
#     def car_new():
#       Avtomobil.model = input("введите марку машины: ")
#       Avtomobil.year = input("Введите год выпуска: ")
#       Avtomobil.gen = input("введите производителя: ")
#       Avtomobil.vol = input("Введите объем двигателя: ")
#       Avtomobil.color = input("введите цвет машины: ")
#       Avtomobil.price = input("Введите цену продажи: ")
#       print("Новые данные:   \n"
#             f"Марка машины: ", Avtomobil.model, "\n"
#             f"Год выпуска: ", Avtomobil.year, "\n"
#             f"Производитель: ", Avtomobil.gen, "\n"
#             f"Обьем двигателя: ", Avtomobil.vol, "\n"
#             f"Цвет: ", Avtomobil.color, "\n"
#             f"Цена: ", Avtomobil.price, "\n")
#
#     def carinfo(self, znak):
#     self.znak = int(input("Что хотите узнать о машине?: \n"
#                               "1.Показать марку машины \n"
#                               "2.Показать год выпуска \n"
#                               "3.Посмотреть страну-производителя \n"
#                               "4.Посмотреть объем двигателя \n"
#                               "5.Посмотреть цвет машины \n"
#                               "6.Узнать цену \n"
#                               "Введите число: \n"))
#         if self.znak == 1:
#             print(self.model)
#         elif self.znak == 2:
#             print(self.year)
#         elif self.znak == 3:
#             print(self.gen)
#         elif self.znak == 4:
#             print(self.vol)
#         elif self.znak == 5:
#             print(self.color)
#         else:
#             print(self.price)
#
#
# class Avto_new(Avtomobil):
#     '''для нового автомобиля'''
#     def __init__(self, new_model, new_color, new_price):
#         self.new_model = new_model
#         self.new_color = new_color
#         self.new_price = new_price
#
#
#     '''вывод экземпляров класса'''
# auto1 = Avtomobil ("BMW X5", 2020,"США", 4.7, "red", 7000000)
# auto2 = Avtomobil ("Lamborgini", 2020,"Италия", 5.2, "yellow", 16000000)
#
# print(Avtomobil.carinfo())

# auto3 = Avtomobil.car_new()
# print(auto3)

# newavto = Avto_new("Лада-Гранта", "blue", 2000000)

# print(auto1.info())
# print(auto2.info())

# print(newavto.new_model)


# задание2
# class Book():
#     '''описание книги'''
#     def __init__(self, title, year, publisher, zhanr, avtor, price):
#         self.title = title
#         self.year = year
#         self.publisher = publisher
#         self.zhanr = zhanr
#         self.avtor = avtor
#         self.price = price
#
#     '''вывод красивенько описание'''
#     def info(self):
#         print(f"Название книги: {self.title} \n"
#               f"Год выпуска: {self.year} \n"
#               f"Издательство: {self.publisher} \n"
#               f"Жанр: {self.zhanr} \n"
#               f"Автор: {self.avtor} \n"
#               f"Цена: {self.price} \n")
#
#    # '''вывод экземпляров класса'''
#
# b1 = Book("Собрание сочинений А.С.Пушкина", 1996, "АСТ-пресс", "Классическая литература", "А.С.Пушкин", 1000)
# print(b1.title)
# print(b1.info())
#

# задание3

# class Stadium():
#     def __init__(self, name, opendate, country, city, place):
#         self.name = name
#         self.opendate = opendate
#         self.country = country
#         self.city = city
#         self.place = place
#
#     def info (self):
#         print("Стадион", self.name, "находится в стране ", self.country, "в городе ", self.city, ".\n"
#         "Его построили в ", self.opendate, "году. Вместимость стадиона составляет ", self.place, "мест.")
#
# st1 = Stadium("Лужники",1956, "Россия","Москва", 81000)
#
# print(st1.info())
# print(st1.name)


