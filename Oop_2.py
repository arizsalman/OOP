""" Polymorphism me aap ek function ya method define karte ho, aur phir alag-alag objects us function ko apne hisaab se implement karte hain. Matlab function ka naam same hai, lekin behavior alag ho sakta hai."""


class Fruit:
    total_fruit = 0  # OOP me ye kam Class varaible  hota he 
    # def __init__(self, fruit_a, fruit_d, fruit_b, fruit_m): YE ERROR DE GA
    # ye None is leye deya he take me apne hasab se dono child ko value alag de sako .

    def __init__(self, fruit_a=None, fruit_d=None, fruit_b=None, fruit_m=None):

        self.fruita = fruit_a
        self.fruitd = fruit_d
        self.fruitm = fruit_m
        self.fruitb = fruit_b
        Fruit.total_fruit += 1


class FruitF(Fruit):
    def __init__(self, fruit_a, fruit_b, fruit_g):
        super().__init__(fruit_a, fruit_b)
        self.fruitg = fruit_g

    def Sfall(self):
        return f'This is Cold season '

    def ful(self):
        return f' Some Fruit {self.fruita}: {self.fruitg}: {self.fruitb} \n {self.Sfall()}'


Cold = FruitF("Apple", "Banana", "Grips")
print(Cold.ful())


class FruitS(Fruit):
    def __init__(self, fruit_d, fruit_m, fruit_an):
        super().__init__(fruit_d, fruit_m)
        self.fruitan = fruit_an

    def Sfall(self):
        return "This is Hot season"

    def full(self):
        return f"Some Fruit {self.fruitd} : {self.fruitm} :{self.fruitan} :{self.Sfall()}"


hot = FruitS("DargonFruit", "Mango", "Anar")
print(hot.full())
print(Fruit.total_fruit)
