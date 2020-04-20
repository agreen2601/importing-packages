from appliances.appliance import Appliance

class CanOpener(Appliance):

    def __init__(self, color):
        super(CanOpener, self).__init__(color)

    def open_can(self):
        print(f'Tuna smells bad')
