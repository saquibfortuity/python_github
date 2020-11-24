class Railway_Form:
    formtype = 'railway form'
    def printdata(self):
        print(f'name is : {self.name}')
        print(f'train name is : {self.train}')
        print(f"timing for train is : {self.timing}")

my_from = Railway_Form()
my_from.name = "Saquib"
my_from.train = "Rajdhani express"
my_from.timing = "3:30 AM"
my_from.printdata()
