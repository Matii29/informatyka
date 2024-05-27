def shopmessage(button, buttonp, machine, machinep, cavesize):
    if button == 12:
        print("Button MAX")
    else:
        print(f"b - Upgrade Button - {buttonp}$)")
    if machine == -1:
        print("m - Buy machine - 100$")
    else:
        print(f"m - Upgrade machine - {machinep}$")
    if cavesize == 0:
        print("c - Buy cave 100$")
    else:
        print(f"c - Enlarge cave - {cavesize*5}$")