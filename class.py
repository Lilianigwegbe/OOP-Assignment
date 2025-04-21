class Superhero:
    def __init__(self, name, secret_identity, power_level, primary_ability):
        self._name = name  # Encapsulated attribute
        self._secret_identity = secret_identity  # Encapsulated attribute
        self.power_level = power_level
        self.primary_ability = primary_ability
        self._is_active = True  # Encapsulated status

    def use_ability(self):
        if self._is_active:
            return f"{self._name} uses {self.primary_ability} with power level {self.power_level}!"
        return f"{self._name} is currently inactive."

    def reveal_identity(self):
        return f"{self._name}'s secret identity is {self._secret_identity}."

    def toggle_active_status(self):
        self._is_active = not self._is_active
        status = "active" if self._is_active else "inactive"
        return f"{self._name} is now {status}."

    def get_name(self):  # Getter for encapsulated attribute
        return self._name

class FlyingSuperhero(Superhero):
    def __init__(self, name, secret_identity, power_level, primary_ability, max_altitude):
        super().__init__(name, secret_identity, power_level, primary_ability)
        self.max_altitude = max_altitude

    def use_ability(self):  # Polymorphism: override base class method
        if self._is_active:
            return (f"{self._name} soars to {self.max_altitude} feet and uses "
                    f"{self.primary_ability} with power level {self.power_level}!")
        return f"{self._name} is currently inactive."

    def fly(self):
        if self._is_active:
            return f"{self._name} flies at {self.max_altitude} feet!"
        return f"{self._name} cannot fly while inactive."

# Example usage
if __name__ == "__main__":
    # Create a regular superhero
    spiderman = Superhero("Spider-Man", "Peter Parker", 85, "Web-slinging")
    print(spiderman.use_ability())
    print(spiderman.reveal_identity())
    print(spiderman.toggle_active_status())
    print(spiderman.use_ability())

    # Create a flying superhero
    superman = FlyingSuperhero("Superman", "Clark Kent", 100, "Heat Vision", 50000)
    print(superman.use_ability())
    print(superman.fly())
    print(superman.reveal_identity())
    print(superman.toggle_active_status())
    print(superman.fly())