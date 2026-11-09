class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health


    def attack_power(self):
        raise NotImplementedError("you must implement attack_power method")

    