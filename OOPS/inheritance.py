class Car:
    def set_info(self, color: str, type: str, mileage: int, seat_capacity: int) -> None:
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
    def set_audo_info(self, electric: bool, city: str) -> None:
        self.electric = electric
        self.city = city
    
    def audi_info(self):
        print (f"Electric = {self.electric}")
        print (f"City = {self.city}")

#c1=Car("red", "alto", 20, 5)
#c1.base_info()

""" c1 = Audi()
c1.color = "red"
c1.type = "audi"
c1.mileage = 20
c1.seat_capacity = 5
c1.base_info() """

c1=Audi()
c1.set_info("red", "alto", 20, 5)
c1.set_audo_info("True", "Hyd")
c1.base_info()
c1.audi_info()            