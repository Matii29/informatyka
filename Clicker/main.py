from helpmess import helpmessage

import random

from shopmess import shopmessage

from Other.petsimulator import Pet

from startmess import startmessage

cash = 0

diamonds = 0

clicks = 0

curbutton = 0

curmachine = -1

cavesize = 0

status = [["Broke", 0],
          ["Poor", 100],
          ["Low-Budget", 1000]
          ["Decent", 2000]
          ["Impressive", 4000],
          ["Above-Average", 10000],
          ["Rich", 50000],
          ["Succesful", 100000]
          ["Ultra-Succesful", 500000]
          ["Milionare", 1000000]
          ["Multi-Milionare", 10000000]
          ["Bilionare", 1000000000]
          ["Multi-Bilionare", 10000000]
          ["Killer", 500000000000]
          ]


buttons = [["Dirt", 0.1, 0], 
           ["Cardboard", 0.3, 3], 
           ["Plastic", 0.5, 15], 
           ["Wood", 1, 50], 
           ["Stone", 2, 125], 
           ["Metal", 3, 300], 
           ["Bronze", 5, 600], 
           ["Silver", 7, 800], 
           ["Gold", 10, 1000], 
           ["Diamond", 13, 1400], 
           ["Emerald", 18, 1700], 
           ["Obsidian", 25, 2500],
           ["Platine", 100, 10000]]


machines = [0.1,
            0.2, 
            0.5,
            1,
            2,
            4,
            8,
            15,
            30,
            50]


startmessage()


helpmessage()


running = True



while running:

    inp = input("Action: ")


    if inp == 'c':
        cash += buttons[curbutton][1]
        print(f"+{buttons[curbutton][1]}$ - {cash}$")


    if inp == 'm':
        ticket = random.randint(0, 99)
        if ticket < cavesize:
            diamondgain = random(machines[curmachine], machines[curmachine]*1.5)
            diamonds += diamondgain
            print(f"+{diamondgain}D - {diamonds}D")
        else:
            print("Nothing found")


    if inp == 'a':
        print("---------------------")

        print(f"Cash - {cash}$")
        print(f"Diamonds - {diamonds}D")

        if curbutton == len(buttons):
            print(f"{buttons[curbutton][0]} Button")

        if curmachine == -1:
            print("No mining machine")

        elif curmachine == len(machines)+1:
            print(f"Mining machine tier {curmachine+1} (MAX)")
        else:
            print(f"Mining machine tier {curmachine+1}")

        if cavesize == 0:
            print("Cave size: None")
        else:
            print(f"Cave size: {cavesize}/100")
        print("---------------------")


    if inp == 'x':
        running = False
    if inp == 's':
        if curbutton == 12:
            print("Button MAX")
        else:
            print(f"b - Upgrade Button - {buttons[curbutton+1][2]}$)")

        if curmachine == -1:
            print("m - Buy machine - 100$")
        else:
            print(f"m - Upgrade machine - {machines[curmachine][1]}$")

        if cavesize == 0:
            print("c - Buy cave 100$")
        else:
            print(f"c - Enlarge cave - {cavesize*5}$")
        
        print("x - Exit the shop")

        inp = input("Choose action: ")

        if inp == 'b' and curbutton < 12:
            if cash >= buttons[curbutton+1][2]:
                cash -= buttons[curbutton+1][2]
                curbutton += 1