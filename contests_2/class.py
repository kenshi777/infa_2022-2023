class Goat:
    legs_number = 4 # Атрибут класса
    def __init__(self, height, weight):
        self.height = height
        self.weight = weight
    def __str__(self):
        s = "height = {}, weight = {}".format(self.height, self.weight)
        return s


marusya = Goat(60, 40)
# marusya.horns = 1 нельзя
notka = Goat(65, 42)
notka.weight += 1
# notka.bell = 'Big' нельзя
A = [notka, marusya]
for x in A:
    print(x)

notka.legs_number += 1
print(marusya.legs_number)
