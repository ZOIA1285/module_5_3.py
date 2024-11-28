from modul_5_2 import House1

class House2(House1):
    def __eq__(self, other):
        if isinstance(other, House2):
            return self.number_of_floors == other.number_of_floors


    def __lt__(self, other):
            return self.number_of_floors < other.number_of_floors


    def __le__(self, other):
            return self.number_of_floors <= other.number_of_floors


    def  __gt__(self, other):
            return self.number_of_floors > other.number_of_floors


    def __ge__(self, other):
            return self.number_of_floors >= other.number_of_floors


    def __ne__(self, other):
            return self.number_of_floors != other.number_of_floors


    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
            return self


    def __radd__(self, value):
        if isinstance(value, int):
            return self.__add__(value)


    def  __iadd__(self, value):
        if isinstance(value, int):
            return self.__add__(value)


h1 = House2('ЖК Эльбрус', 10)
h2 = House2('ЖК Акация', 20)
print(h1)
print(h2)
print(h1 == h2) # __eq__
h1 = h1 + 10 # __add__
print(h1)
print(h1 == h2)
h1 += 10 # __add__
print(h1)
h2 = 10 + h2 # __add__
print(h2)
print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne_

