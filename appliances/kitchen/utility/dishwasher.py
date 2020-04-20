from appliances.appliance import Appliance

class DishWasher(Appliance):

    def __init__(self, color):
        super(DishWasher, self).__init__(color)

    def wash_dishes(self):
        print(f"The dishwasher is {self.color} and {self.heat_method}. Grind, grind, clunk. Time to call the dishwasher repair person")
