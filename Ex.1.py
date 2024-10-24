class Car:
    def __init__(self, registration_number, maximun_number):
       self.registration_number= registration_number
       self.maximun_number=maximun_number
       self.current_number=0
       self.travelled_distance= 0


    def print_properties(self):
       print(f"registration_number: {self.registration_number}")
       print(F"maximun_number; {self.maximun_number}")
       print(f"current_number: {self.current_number}")
       print(f"travelled_distance: {self.travelled_distance}")

# Main Program
car = Car("ABC-123", 142)
car.print_properties()









