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

#2.The snail climbs up 7 feet each day and slips back 2 feet each night. 
#How many days will it take the snail to get out of a well with the given 
#depth?. Using python, write a function to solve this problem. Sample Input: 
#31 Sample Output: 6

def days(depth):
    feet_climbed_in_1day=7
    feet_slipped_in_1day=2
    actual_feet_climbed=feet_climbed_in_1day - feet_slipped_in_1day
    number_of_days=depth // actual_feet_climbed
    return number_of_days
depth=31
print(days(depth))

#3.Write a function that takes a list of numbers and returns the 
#largest number in the list.

import numpy as np
def max(list):
    return np.max(list)
list=[36, 14, 93, 183]
print(max(list))

#4.Write a program that accepts a sentence and calculate the number 
#of upper case letters and lower case letters. Suppose the following 
#input is supplied to the program: Hello world! Then, the output 
#should be: UPPER CASE 1 LOWER CASE 9
def calculate(sentence):
    count_lower=0
    count_upper=0
    for i in sentence:
        if (i.islower()):
            count_lower += 1
        elif(i.isupper()):
            count_upper += 1
    return ("UPPER CASE: {} LOWER CASE: {}".format(count_upper, count_lower) )

sentence="Hello world"
print(calculate(sentence))

#5.Using Object Oriented Programming, write a program that implements 
#a dice game. The game should have two players, and each player 
#should have a name and a score. The game should have a method 
#called play that takes two players as arguments and 
#simulates the game. The game should be played as follows:

# Each player rolls a die.
# The player with the highest roll wins the round.
# The winner gets one point added to their score.
# The game ends when one player has 5 points.
# The player with the most points at the end of the game wins.
# The program should print out the winner's name and score.
# If a player rolls a 6, they get an extra roll. If they roll a 6 
# again, they get another extra roll. If they roll a 6 a third time, 
# they get an extra roll, but their turn ends.
import random

class Player:
    def __init__(self, name):
        self.name=name

class Game:
    def __init__(self):
        print("This is a dice game")
    def play(player1, player2):
        player1_score=0
        player2_score=0
        while player1_score < 5 and player2_score < 5:
            player1_value=random.randint(1, 6)
            player2_value=random.randint(1, 6)
            print("player1 value is:{}".format(player1_value))
            print("player2 value is:{}".format(player2_value))
            if player1_value > player2_value:
                player1_score +=1
            elif player2_value > player1_value:
                player2_score +=1
        
            print("player1 score is:{}".format(player1_score))
            print("player2 score is:{}".format(player2_score))

            if player1_value or player2_value == 6:
                chance = 1
                while chance <= 3:
                    if player1_value ==6:
                        player1_value=random.randint(1, 6)
                        print("p1secondvalue is:{}".format(player1_value))
                        if player1_value > player2_value:
                            player1_score +=1
                            if player1_score == 5:
                                break
                        
                    elif player2_value ==6:
                        player2_value=random.randint(1, 6)
                        print("p2secondvalue is:{}".format(player2_value))
                        if player2_value > player1_value:
                            player2_score +=1
                            if player2_score == 5:
                                break
                    
                    print("player1 finalscore is:{}".format(player1_score))
                    print("player2 finalscore is:{}".format(player2_score))
                    chance += 1
            else:
                print("none of the values is a 6")
    
        if player1_score > player2_score:
            winner=player1
            score=player1_score
        elif player2_score > player1_score:
            winner=player2
            score=player2_score
        print("The winner is:{} with a score of:{} points".format(winner, score))      
Game.play("Elsa", "Arno")

#6.Write a Python program that lists out all the default as well as 
#custom properties of the class.

#7.Write a Program in Python to implement a Stack Data Structure 
#using Class and Objects, with push, pop, and traversal methods
class Animal:
    def __init__(self):
        self.animal_names= []
    def push(self, name):
        return self.animal_names.append(name)
    def isEmpty(self):
        return len(self.animal_names) == 0
    def pop(self):
        if self.isEmpty():
            return ("list is empty")
        return self.animal_names.pop()
    def peek(self):
        return self.animal_names[-1]
    def size(self):
        return len(self.animal_names)
    def show(self):
        return self.animal_names
my_animal_list=Animal()
my_animal_list.push("cat")
my_animal_list.push("dog")
my_animal_list.push("horse")
my_animal_list.push("cow")
my_animal_list.push("goat")
print(my_animal_list.show())
print(my_animal_list.size())
print(my_animal_list.pop())
print(my_animal_list.peek())
print(my_animal_list.isEmpty())
print(my_animal_list.pop())
print(my_animal_list.pop())
print(my_animal_list.pop())
print(my_animal_list.pop())
print(my_animal_list.pop())

#8.Using list comprehension, write a program that takes a list of numbers
#and returns a list of the squares of the numbers.
numbers=[1,2,3,4,5,6,7,8,9,10]
sq_numbers=[i*i for i in numbers]
print(sq_numbers)

#9.Using only functions and lists, implement a queue data structure.
#The queue should have the following methods: enqueue, dequeue, and size.
#The queue should be "first-in-first-out"(FIFO).
class Queue:
    def __init__(self) -> None:
        self.bank_queue=[]
    def enqueue(self, number):
        return self.bank_queue.insert(0,  number)
    def isEmpty(self):
        return len(self.bank_queue) == 0
    def dequeue(self):
        if self.isEmpty():
            return("queue is empty")
        return self.bank_queue.pop()
    def show(self):
        return self.bank_queue
    def size(self):
        return len(self.bank_queue)
bank=Queue()
bank.enqueue(1)
bank.enqueue(2)
bank.enqueue(3)
bank.enqueue(4)
print(bank.show())
print(bank.dequeue())
print(bank.show())
print(bank.dequeue())
print(bank.dequeue())
print(bank.dequeue())
print(bank.dequeue())
bank.enqueue(10)
bank.enqueue(50)
print(bank.show())
