# Base Class
class Superhero:
    def __init__(self, name, power, origin):
        self.name = name
        self.power = power
        self.origin = origin

    def introduce(self):
        return f"I am {self.name} from {self.origin}, and my power is {self.power}!"

    def use_power(self):
        return f"{self.name} uses {self.power}!"

# Inherited Class (demonstrates polymorphism & encapsulation)
class FlyingSuperhero(Superhero):
    def __init__(self, name, power, origin, flight_speed):
        super().__init__(name, power, origin)
        self.__flight_speed = flight_speed  # Encapsulation (private attribute)

    def use_power(self):
        return f"{self.name} flies at {self.__flight_speed} km/h with {self.power}!"

    def reveal_speed(self):
        return f"{self.name}'s flying speed is {self.__flight_speed} km/h."

# Example Usage
hero1 = Superhero("ugali man", "eating", "kanairo")
hero2 = FlyingSuperhero("crypto", "assets Manipulation", "bank", 1200)

print(hero1.introduce())
print(hero1.use_power())

print(hero2.introduce())
print(hero2.use_power())
print(hero2.reveal_speed())
