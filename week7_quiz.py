# 1.Your task is to create slightly different animals, which should 
# have the same properties and methods, but should implement the talk() 
# method in different ways. For example. should a cat (when talking) say 
#"Moew", a dog "Woff", a fish "Blub" and a Cow "Muuu". They should all
# share the following (private) properties: name (string), age (number),
# food (list of strings), and have the functions get_name, set_name, get_age,
# set_age, get_food, add_food, remove_food. Finally, all the animals must have
# the talk function, but that function must, as I said, be implemented in
# each animal, as the animals have different sounds.
#When you have made the classes, create instances of the classes and put in
# a list - loop through the list - and let all the animals talk! :)

class Animal:
    def __init__(self, name, age, food):
        self.__name=name
        self.__age=age
        self.__food=food
    def talk(self):
        print("i can talk")
    def sleep(self):
        print("I like sleeping")
    def run(self):
        print("i can run")

class Lion(Animal):
    def __init__(self, name, age, food):
        super().__init__(name, age, food)
        self.__name="Simba"
        self.__age=8
        self.__food=["antelopes", "deers", "hares"]
    def getName(self):
        return self.__name
    def setName(self, name):
        self.__name= name
    def getAge(self):
        return self.__age
    def setAge(self, age):
        self.__age= age
    def getFood(self):
        return self.__food
    def setFood(self):
        self.__food=["hares", "antelopes", "deers"]


    def talk(self):
        print("I {} can roar".format(self.__name))

class  Wolf(Animal):
    def __init__(self, name, age, food):
        super().__init__(name, age, food)
        self.__name="Jake"
        self.__age=6
        self.__food=["zebras", "antelopes", "rats"]
    def getName(self):
        return self.__name
    def setName(self, name):
        self.__name= name
    def getAge(self):
        return self.__age
    def setAge(self, age):
        self.__age= age
    def getFood(self):
        return self.__food
    def setFood(self):
        self.__food=["rats", "antelopes", "zebras"]


    def talk(self):
        print("I {} can growl".format(self.__name))

my_lion=Lion("Simba", 8, ["antelopes", "deers", "hares"])
print(my_lion.getName())
print(my_lion.setName("Alex"))
print(my_lion.getName())
print(my_lion.getAge())
print(my_lion.setAge(17))
print(my_lion.getAge())
print(my_lion.getFood())
print(my_lion.setFood())
print(my_lion.getFood())
my_lion.talk()

my_wolf=Wolf("Jake", 6, ["zebras", "antelopes", "rats"] )
print(my_wolf.getName())
print(my_wolf.setName("Edward"))
print(my_wolf.getName())
print(my_wolf.getAge())
print(my_wolf.setAge(3))
print(my_wolf.getAge())
print(my_wolf.getFood())
print(my_wolf.setFood())
print(my_wolf.getFood())
my_wolf.talk()







        