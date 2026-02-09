class Car:
    def __init__(self, color, type, mileage, seat_capacity) -> None:
        self.color = color
        self.type = type
        self.mileage = mileage
        self.seat_capacity = seat_capacity
    
    def base_info(self):
        print(f"Color is = {self.color}")
        print(f"type is = {self.type}")
        print(f"mileage is = {self.mileage}")
        print(f"seat_capacity is = {self.seat_capacity}")

class Audi(Car):
    def __init__(self) -> None:
        print ("Audi")

#c1=Car("red", "alto", 20, 5)
#c1.base_info()

c1 = Audi()
c1.color = "red"
c1.type = "audi"
c1.mileage = 20
c1.seat_capacity = 5
c1.base_info()

