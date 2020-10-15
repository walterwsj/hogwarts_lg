class game():
    def __init__(self):
        self.my_hp = 1000
        self.my_power = 200
        self.your_hp = 1000
        self.your_power = 199

class sub(game):
    def __init__(self,defense):
        self.defense=defense
        super(sub, self).__init__()

    def fight(self):
        while True:
            self.my_hp = self.my_hp+self.defense - self.your_power
            self.your_hp = self.your_hp - self.my_power
            if self.my_hp <= 0:
                print("You win")
                break
            elif self.your_hp <= 0:
                print("I win")
                break

xx=sub(5)
xx.fight()
