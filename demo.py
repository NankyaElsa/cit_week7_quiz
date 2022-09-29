class Pig:
    def __init__(self, name):
        self.name=name
        self.food=["cassava", "pumpkin"]
        self.new=[self.food.split(" ,")]
cassy=Pig("cassy")
print(cassy.name)
print(cassy.food)

              