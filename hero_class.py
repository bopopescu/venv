class Hero():
    def __init__(self, name, level, model):
        self.name = name
        self.level = level
        self.model = model
        self.health = 100

    def show_hero(self):
        if(self.health == 0):
            print( "Hero destroyed!!!")
        else:
            description = (self.name + " Level is: " + str(self.level) + " model is: " + self.model + " Health is "+ str(self.health)).title()
            print(description)

    def level_up(self):
        self.level += 1
    def move(self):
        print("Hero " + self.name + " running...")

    def attack(self):
        if (self.health>0):
            self.health = self.health - 20
        else:
            print(self.name + " killed")