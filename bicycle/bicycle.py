class Bicycle:
    def run(self,km):
        print(f"Total running {km} miles")

class E_Bicycle(Bicycle):
    def __init__(self,valume):
        self.valume=valume
    def fill_charge(self,vol):
        self.valume+=vol
        print(f"Charged {vol}. Current volume is {self.valume}")
    def run(self,km):
        power_km=self.valume*10
        if power_km>=km:
            print("Charging running {km} miles")
        else:
            print(f"Battery is out. charging running {power_km}")
            super(E_Bicycle, self).run(km-power_km)

ebike=E_Bicycle(10);
ebike.run(200)
