import random


def lottery():
    print("Welcome to a lottery! Select 3 numbers from 1 to 25.")

    print("If the numbers you chose correspond the numbers selected you win 1000000$")

    print("---"*20)

    inp1 = input("Select the first number: ")

    print("---"*20)

    inp2 = input("Select the second number: ")

    print("---"*20)

    inp3 = input("Select the third number: ")
    
    yournum = [inp1, inp2, inp3]

    winningnum = [random.randint(1, 25), random.randint(1, 25), random.randint(1, 25)]

    i = 0
    numbersin = 0

    while i <= 2:

        if yournum[i] in winningnum:
            numbersin += 1

        if numbersin == 3:
            print("You win 1000000$!")
            return 1000000
        
        else:
            print("You lose")
            return 0
        
def megalottery():
    print("Welcome to a megalottery! Select 6 numbers from 1 to 36.")

    print("If the numbers you chose correspond the numbers selected you win 1000000000$")

    print("---"*20)

    inp1 = input("Select the first number: ")

    print("---"*20)

    inp2 = input("Select the second number: ")

    print("---"*20)

    inp3 = input("Select the third number: ")

    print("---"*20)

    inp4 = input("Select the fourth number: ")

    print("---"*20)

    inp5 = input("Select the fifth number: ")

    print("---"*20)

    inp6 = input("Select the sixth number: ")

    yournum = [inp1, inp2, inp3, inp4, inp5, inp6]

    winningnum = [random.randint(1, 36), random.randint(1, 36), random.randint(1, 36), random.randint(1, 36), random.randint(1, 36), random.randint(1, 36)]

    i = 0
    numbersin = 0

    while i <= 5:

        if yournum[i] in winningnum:
            numbersin += 1

        if numbersin == 5:
            print("You win 1000000000$!")
            return 1000000000
        
        else:
            print("You lose")
            return 0

def flipacoin():

    print("Heads or tails?")

    print("1 - heads")

    print("2 - tails")

    inp = input("Select: ")

    selected = int(inp)
    
    coin = random.randint(0, 1)

    if coin == selected:
        print("You win!")

    else:
        print("You lose!")

def display_slots(slot1, slot2, slot3):

    print(f"Slots: {slot1} | {slot2} | {slot3}")

def check_winning(slot1, slot2, slot3):

    if slot1 == slot2 == slot3:

        return True
    
    return False

def slotmachine():
    money = 100

    while money > 0:

        print(f"You have ${money}.")

        bet = int(input("Enter your bet amount (or 0 to quit): "))
        
        if bet == 0:
            print("Thank you for playing! Goodbye!")
            break

        elif bet > money:
            print("You don't have enough money to place that bet.")
            continue

        slot1 = random.choice(["Cherry", "Lemon", "Orange", "Plum", "Bell", "Bar"])

        slot2 = random.choice(["Cherry", "Lemon", "Orange", "Plum", "Bell", "Bar"])

        slot3 = random.choice(["Cherry", "Lemon", "Orange", "Plum", "Bell", "Bar"])

        display_slots(slot1, slot2, slot3)

        if check_winning(slot1, slot2, slot3):

            winnings = bet * 10

            money += winnings

            print(f"Congratulations! You won ${winnings}.")

        else:
            money -= bet

            print(f"Sorry, you lost ${bet}. Better luck next time!")

        if money == 0:

            print("You have run out of money. Game over.")



def roll_dice():

    """Roll two dice and return their sum."""

    die1 = random.randint(1, 6)

    die2 = random.randint(1, 6)

    return die1, die2, die1 + die2

def dicerollchallenge():

    balance = 100

    print("Welcome to the Dice Roll Challenge!")

    
    while True:

        print(f"Your current balance is: ${balance}")

        if balance <= 0:

            print("You've run out of money! Game over.")

            break
        
        bet = int(input("Place your bet: "))

        if bet > balance or bet <= 0:

            print("Invalid bet amount. Please bet within your balance.")

            continue
        
        guess = int(input("Guess the sum of the two dice (2-12): "))

        if guess < 2 or guess > 12:

            print("Invalid guess. Please guess a number between 2 and 12.")

            continue
        
        die1, die2, result = roll_dice()

        print(f"The dice roll results are: {die1} and {die2}. Sum is: {result}")
        
        if guess == result:

            balance += bet

            print(f"Congratulations! You guessed correctly. You win ${bet}.")

        else:
            balance -= bet

            print(f"Sorry, you guessed wrong. You lose ${bet}.")
        
        if balance == 0:

            print("You've run out of money! Game over.")
            break
        
        continue_game = input("Do you want to continue playing? (y/n): ").lower()

        if continue_game != 'y':
            
            print(f"You leave the game with ${balance}.")
            break


running = True

while running:

    print("---Choose a game---")

    print("1 - lottery")

    print("2 - megalottery")

    print("3 - slot machine")

    print("4 - dice rolling")

    print("x - exit")

    inp = input("Select: ")

    if int(inp) == 1:
        lottery()

    elif int(inp) == 2:
        megalottery()

    elif int(inp) == 3:
        slotmachine()

    elif int(inp) == 4:
        dicerollchallenge()

    if inp == 'x':
        running = False
