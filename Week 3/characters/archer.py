from .warrior import Warrior

# Coding Challenge: Add Your Own Class
class Archer(Warrior):
    """
    Represents an Archer character, inheriting from Warrior.

    Attributes:
        name (str): The archer's name.
        level (int): The archer's level.
        health (int): The archer's current health.
        strength (int): The archer's strength.
        stealth (int): The archer's stealth level.
    """
    def __init__(self, name, level, health, strength, arrows):
        """Initializes a new archer object."""
        # Call the parent class's __init__ method to initialize inherited attributes
        super().__init__(name, level, health, strength)

        # Initialize the archer's specific attribute: arrows
        self.arrows = arrows

    # Create sneak attack that targets and reduces health of another player
    def fire_arrow(self, target):
        """
        Fires an arrow at the target, reducing their health if arrows are available.

        """
        # Reduce the target's health by a factor of arrows
        if self.arrows > 0:
            self.arrows -= 1
            target.health -= self.strength
            return f"{self.name} fires an arrow at {target.name} doing {self.strength} damage!"
        else:
            return f"{self.name} has no arrows left to fire!"