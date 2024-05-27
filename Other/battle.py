import random


class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        damage = random.randint(0, self.attack_power)
        other.health -= damage
        return damage

    def is_alive(self):
        return self.health > 0

    def __str__(self):
        return f"{self.name}: Health={self.health}, Attack Power={self.attack_power}"



class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=15)

    def heavy_attack(self, other):
        damage = random.randint(self.attack_power // 2, self.attack_power * 2)
        other.health -= damage
        return damage


class Mage(Character):

    def __init__(self, name):
        super().__init__(name, health=80, attack_power=20)

    def cast_spell(self, other):
        damage = random.randint(self.attack_power // 2, self.attack_power * 3)
        other.health -= damage
        return damage

# Function to simulate a battle
def battle(player, enemy):

    print(f"{player.name} (Player) vs. {enemy.name} (Enemy)")
    while player.is_alive() and enemy.is_alive():

        if isinstance(player, Warrior):
            damage = player.heavy_attack(enemy)
            print(f"{player.name} performs a heavy attack for {damage} damage!")

        elif isinstance(player, Mage):
            damage = player.cast_spell(enemy)
            print(f"{player.name} casts a spell for {damage} damage!")

        else:
            damage = player.attack(enemy)
            print(f"{player.name} attacks for {damage} damage!")

        if not enemy.is_alive():

            print(f"{enemy.name} has been defeated!")
            break



        damage = enemy.attack(player)
        print(f"{enemy.name} attacks for {damage} damage!")

        if not player.is_alive():
            print(f"{player.name} has been defeated!")
            break

        print(player)

        print(enemy)

        print()

def main():
    print("Welcome to the Battle Game!")
    name = input("Enter your character's name: ")

    while True:
        choice = input("Choose your character (1 - Warrior, 2 - Mage): ")

        if choice == '1':
            player = Warrior(name)
            break

        elif choice == '2':
            player = Mage(name)
            break

        else:
            print("Invalid choice. Please try again.")


    enemy = Character("Enemy", health=90, attack_power=10)


    battle(player, enemy)

if __name__ == "__main__":

    main()