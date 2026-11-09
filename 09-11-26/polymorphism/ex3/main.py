from classes.mage import Mage
from classes.warrior import Warrior

def attack(attacker, attacked):
    attacked.health -= attacker.attack_power()
    print(f"{attacker.name} hits {attacked.name} for {attacker.attack_power()}")

conan = Warrior("Conan", 100)
merlin = Mage("Merlin", 60)
attack(conan, merlin)
attack(merlin, conan)
print(merlin.name, merlin.health)
print(conan.name, conan.health)
