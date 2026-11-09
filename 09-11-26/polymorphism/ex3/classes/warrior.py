from .character import Character

class Warrior(Character):
    ATTACK_POWER = 15

    def attack_power(self):
        return self.ATTACK_POWER

    