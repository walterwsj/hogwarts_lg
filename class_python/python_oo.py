class House:
    def __init__(self):
        self.utitlity="Sleeping"

    ##Static property
    door = 'red'
    floor = 'white'

    ##Dymatic
    def sleep(self):
        print(self.utitlity)
        print("Use for sleep")

    def cook(self):
        print("Use for cook")


northern_europe = House()
chinese_style = House()
northern_europe.door="white"
print(House.door)
print(northern_europe.sleep())
