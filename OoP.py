"""  OOP me Class ko create karna  --> Class Anyname  ye first step he """
"""  Is ke bad jab hum define kare tu indentation ka kayal rakakna he """
""" phri function baneke --> def __init__(self ,your,required)<-- is me parameter denahota dena hota he"""
""" parameter ko banae bad us ko call karna hota he """
""" parameter [normal namejo bhe rakna ho= ye main parameter hota he ]  [name= Organnal parameter ]"""
"""function ke oarameter banate vakt hum parameter create karne se bale ""self"" lete he --> self ,any parameter """

#  ye jo kam keya he is me hum ne artribus add keye the


class Name:
    def __init__(self, name, fname):
        self.name = name
        self.fname = fname


# hum ne ye ak class bana le hum bohat sare class bhe bana sakte he
my_name = Name("Ariz", "Salman")
my_bro = Name("Ali", "Salman")

# print(Name)  # output me ye show ho ga <class '__main__.Name'> kyo ke pura function call kar rahe he hum
# ye yaha pe refrence ko dega jomemory me save hota he <__main__.Name object at 0x00000255E8527230>
# print(my_name)
# print(my_name.name)  # Ariz ye normal  name de ga
# print(my_name.fname)  # Salman  ye bhe  normal  name de ga
# print(my_bro.name)
# print(my_bro.fname)

# yaha hum functionality used kare ke phele app class banane hi phir atribute


class Name:
    def __init__(self, name, fname):
        self.name = name
        self.fname = fname

    def Full_name(self):
        return f" My name is:{self.name} \n My father name is:{self.fname}"


# full = Name("Ariz", "Salman")  # phele value de ge parameter ke
# print(full.Full_name())  # ab ye function ko jis ne store karaya he   exist kare ga
# Name("Ariz", "Salman") yaha error a ga jab tum object ko variable me nahe dalo ge tu error ai ga
# print(Name.Full_name())
"""Inheritance ek OOP concept hai jisme ek class (child/subclass) dusri class (parent/superclass) ki properties aur methods reuse aur extend kar sakti hai."""
""" Inheritance kya kam karta he {Kaam: code reuse aur functionality extend karna}"""


class Inheri:
    def __init__(self, home, address):
        self.home = home
        self.address = address  # YE Encapsulation laga deya

    def Full(self):
        return f" it's my {self.home} Address is {self.address}"

# abhe talk hum ne class bnae or us me functionality de ab aage Inheritance dena he


class Inheritance(Inheri):
    def __init__(self, home, address, From):
        super().__init__(home, address)
        self.From = From


Maraging = Inheritance("Velas", 'Gulhan', 'Karachi')

print(Maraging.Full())
print(Maraging.From)


"""Encapsulation [Encapsulation ka matlab hai data aur methods ko ek object ke andar band kar dena taki wo bahar se direct access na ho sake.]"""
"""Encapsulation method me do method hote he ak get () or ak setter ho ta he value ko hide{__}is se karte he . get value ko unhide kar de ta he or setter us unhide value ko change karnee ka control rakta he """
"""Encapsulation ka  Kaam  kya he  -->{Data ko hide karna (protection).
Sirf controlled methods (getters/setters) ke through access dena } """


class Encp:
    def __init__(self, pant, shos, shirt):
        self.pant = pant
        self.__shos = shos
        self.shirt = shirt

    def ful(self):
        return f"My pant is :{self.pant} My shrit is :{self.shirt} and shos is supries .."

    def get_shos(self):
        return self.__shos + "'s Shos"

    def set_shos(self, new_shos):
        self.__shos = new_shos


my_Encp = Encp("tom Brand", 'Bada', "News")
print(my_Encp.ful())
print(my_Encp.get_shos())
my_Encp.set_shos('Addadas!')
# print(my_Encp.set_shos()) ///ye error de ya vo yo ke hum is ko return nahe kar rahe he hum sirf is ko update kar rahe he (line no 91 )
print(my_Encp.get_shos())
