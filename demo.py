# class Pig:
#     def __init__(self, name):
#         self.name=name
#         self.food=["cassava", "pumpkin"]
#         self.new=[self.food.split(" ,")]
# cassy=Pig("cassy")
# print(cassy.name)
# print(cassy.food)
# import random

# class Player:
#     def __init__(self, name):
#         self.name=name

# class Game:
#     def __init__(self):
#         self.player1=Player("Kelly")
#         self.player2=Player("Arno")
#         print("this is a dice game")
#     def play(player1, player2):
#         player1_score=0
#         player2_score=0
#         while player1_score < 5 and player2_score < 5:
#             player1_value=random.randint(1, 6)
#             player2_value=random.randint(1, 6)
#             print("player1 value is:{}".format(player1_value))
#             print("player2 value is:{}".format(player2_value))
#             if player1_value > player2_value:
#                 player1_score +=1
#             elif player2_value > player1_value:
#                 player2_score +=1
        
#             print("player1 score is:{}".format(player1_score))
#             print("player2 score is:{}".format(player2_score))

#             if player1_value or player2_value == 6:
#                 chance = 1
#                 while chance <= 3:
#                     if player1_value ==6:
#                         player1_value=random.randint(1, 6)
#                         print("p1secondvalue is:{}".format(player1_value))
#                         if player1_value > player2_value:
#                             player1_score +=1
#                             if player1_score == 5:
#                                 break
                        
#                     elif player2_value ==6:
#                         player2_value=random.randint(1, 6)
#                         print("p2secondvalue is:{}".format(player2_value))
#                         if player2_value > player1_value:
#                             player2_score +=1
#                             if player2_score == 5:
#                                 break
                    
#                     print("player1 finalscore is:{}".format(player1_score))
#                     print("player2 finalscore is:{}".format(player2_score))
#                     chance += 1
#             else:
#                 print("none of the values is a 6")
    
#         if player1_score > player2_score:
#             winner=player1
#             score=player1_score
#         elif player2_score > player1_score:
#             winner=player2
#             score=player2_score
#         print("The winner is:{} with a score of:{} points".format(winner, score))
# player1=Player("kelly")
# player2=Player("Beezu")
# #my_game=Game()      
# Game.play("kelly", "beezu")
        # if roll_1 > roll_2:
        #     player1_score += 1
        # elif roll_2 > roll_1:
        #     player2_score += 1
    # print(player1_score)
    # print(player2_score)          

# numbers=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# new_numbers=[]
# for i in numbers:
#     sq_number= i * i
#     new_numbers.append(sq_number)
# print(new_numbers)

