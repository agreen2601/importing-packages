from appliances.appliance import Appliance

class Refrigerator(Appliance):

    def __init__(self, color):
        super(Refrigerator, self).__init__(color)

    def make_ice(self):
        print("grind, grind, clunk. Time to call the fridge repair person")
