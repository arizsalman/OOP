"""

Static method ek aisa method hota hai jo class ke andar likha jata hai, lekin usko chalane ke liye na to self (object reference) chahiye aur na hi cls (class reference)."""


class Math:
    @staticmethod
    def add(a, b):
        return a + b


# call without creating object
print(Math.add(5, 10))   # 15

# object se bhi call kar sakte ho
m = Math()
print(m.add(3, 7))
# y = Math(10, 3) ya ha error de agar isa karna he tu __init__ pe kam karo.
# print(y)


""" Property Decorator 
@property decorator Python me use hota hai jab aap chahte ho ke ek method ko attribute ki tarah access kar sako.

Matlab: method ko () laga ke call nahi karna padta, bas normal variable ki tarah use hota hai. or ye overwrite anhe karta """


class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    @property
    def full_name(self):
        return f"{self.brand} {self.model}"


my_car = Car("Toyota", "Corolla")

# ab object ke attribute ko overwrite kar diya
# yaha eror ie ya is leye ke overwrite kar de ya hum ne Property decorator allow nahe karta
my_car.model = "Yaris"
# ye value show nahe hue ge ok property decrator ke wajah se 
print(my_car.full_name)

# yahan method ko property ki tarah access kiya
print(my_car.full_name)   # Output: Toyota Corolla

# print(my_car.full_name())   # ye error de ga kyon ke hum ne call kya or porperty decorator lagane ke bad hum  call nahe karte
