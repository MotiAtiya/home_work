from .character import Character

class Mage(Character):
    ATTACK_POWER = 10

    def attack_power(self):
        return self.ATTACK_POWER + self.ATTACK_POWER * (self.health >= 50)
    

    