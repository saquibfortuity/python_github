class Train:
    def __init__(self, name, fare, seats):
        self.name = name
        self.fare = fare
        self.seats = seats

    def getstatus(self):
        print(f"The name of the train is {self.name} ")
        print(f"The seats available in this train are {self.seats}")


    def getfareinfo(self):
        print(f"price of the ticket is RS/- {self.fare}")

    def booktickets(self):
        if self.seats > 0:
            print(f"your ticket ha sbeen booked ! and seat number is {self.seats}")
            self.seats = self.seats - 1
        else:
            print("sorry this train is full kindly try in tatkal ")


rajdhani = Train("Rajdhani express 14015 ", 90, 300)

rajdhani.getstatus()
rajdhani.getfareinfo()
rajdhani.booktickets()



