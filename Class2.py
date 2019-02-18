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


class SuperHero(Hero):
    def __init__(self, name, level, model, magic):
        super().__init__(name, level, model)
        self.magic = magic
        self.__magiclevel = 150
    def makemagic(self):
        if (self.magic == 0):
            print("not a superhero")
        else:
             self.magic -= 1
    def show_hero(self):
        if(self.health == 0):
            print( "Hero destroyed!!!")
        else:
            description = (self.name + " Level is: " + str(self.level) + " model is: " + self.model + " Health is "+ str(self.health)
                           + " Magic = " +str(self.magic)).title()
            print(description)



myhero = Hero("Vurdalak", 4 , "kiborg")
mysuperhero = SuperHero("Moisei", 10, "human", 5)
myhero.show_hero()
mysuperhero.show_hero()
mysuperhero.makemagic()
mysuperhero.makemagic()
mysuperhero.makemagic()
mysuperhero.makemagic()
mysuperhero.makemagic()
mysuperhero.makemagic()
mysuperhero.show_hero()


