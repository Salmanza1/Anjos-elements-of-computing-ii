from .character import Character

# Adding Methods for Specialized Behavior
class Healer(Character):

    # Initialize character attributes

    def __init__(self, name, level, health, healing_power):
        # Inherit name, level, health attributes
        super().__init__(name, level, health)
        # Initialize the healer's specific attribute: healing_power
        self.healing_power = healing_power
    # Create healing method that interacts with other character
    def heal(self, target):
        """
        Heaks the target character.

        Args:
             self(Healer): Use the healing power attribute as an healing points.
             target (Character): The character to heal 

        Returns:
                str: A message indicating the healing action
        """
        # Increase the target's health by the healer's healing power
        target.health += self.healing_power
        # Return a message describing the healing action
        return f"{self.name} heals {target.name} for {self.healing_power} HP! {target.name} now has {target.health} HP."