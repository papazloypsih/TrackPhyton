# TODO Найдите количество книг, которое можно разместить на дискете
a = 1.44 * 1024 * 1024
b = 100
c = 50
d = 25
e = 4
weight_one_book = e * d * c * b
quantity = a // weight_one_book
print("Количество книг, помещающихся на дискету:", int(quantity))
