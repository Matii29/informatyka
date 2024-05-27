import random

class Pet:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.hunger = random.randint(0, 10)
        self.happiness = random.randint(0, 10)
        self.energy = random.randint(0, 10)
        self.cleanliness = random.randint(0, 10)
    
    def feed(self):
        if self.hunger > 0:
            self.hunger -= 2
            self.happiness += 1
            print(f"{self.name} has been fed.")
        else:
            print(f"{self.name} is not hungry.")
    
    def play(self):
        if self.energy > 0:
            self.hunger += 1
            self.happiness += 2
            self.energy -= 1
            print(f"{self.name} is playing.")
        else:
            print(f"{self.name} is too tired to play.")
    
    def bathe(self):
        if self.cleanliness < 10:
            self.cleanliness += 2
            print(f"{self.name} has been bathed.")
        else:
            print(f"{self.name} is already clean.")
    
    def sleep(self):
        if self.energy < 10:
            self.energy += 3
            print(f"{self.name} is sleeping.")
        else:
            print(f"{self.name} is not tired.")
    
    def status(self):
        print(f"{self.name}: Hunger = {self.hunger}, Happiness = {self.happiness}, Energy = {self.energy}, Cleanliness = {self.cleanliness}")
    
def main():
    print("Welcome to the Pet Simulator!")
    name = input("Enter your pet's name: ")
    species = input("Enter your pet's species: ")
    pet = Pet(name, species)
    
    while True:
        print("\nWhat would you like to do?")
        print("1. Feed your pet")
        print("2. Play with your pet")
        print("3. Bathe your pet")
        print("4. Let your pet sleep")
        print("5. Check your pet's status")
        print("6. Teach your pet a trick")
        print("7. Go for a walk")
        print("8. Quit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            pet.feed()
        elif choice == '2':
            pet.play()
        elif choice == '3':
            pet.bathe()
        elif choice == '4':
            pet.sleep()
        elif choice == '5':
            pet.status()
        elif choice == '6':
            print(f"{pet.name} is learning a new trick!")
            print("...")
            print(f"Congratulations! {pet.name} has learned a trick!")
        elif choice == '7':
            print(f"{pet.name} is going for a walk.")
            print("You both enjoy the fresh air.")
            pet.happiness += 2
            pet.energy -= 1
            pet.cleanliness -= 1
        elif choice == '8':
            print("Thank you for playing!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 8.")

main()