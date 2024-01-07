library = [{"ID": 1, "title": "Lord of the rings", "Price": "33.49 PLN", "shelf": "A46"},
           {"ID": 2, "title": "Hobbit", "Price": "39.99 PLN", "shelf": "F03"},
           {"ID": 3, "title": "Rodzina Monet", "Price": "44.90 PLN", "shelf": "M21"}]

def newid():
    newId = 1
    isnew = False
    while not isnew:
        notnew = False
        for i in range(0, len(library)):
            if library[i]['ID'] == newId:
                notnew = True
        if notnew:
            newId += 1
        if not notnew:
            isnew = True
    return newId

def printbooks():
    print("<List of books>")
    print("---"*10)
    for i in library:
        for v,k in i.items():
            print(f"{v} | {k}")
        print("---"*10)
    print("^ The list of books is above ^")

def removebook():
    mistake = False
    print("<Remove a book>")
    inp = input("Select ID: ")
    if inp == "-":
        mistake = True
    else:
        inp = int(inp)
    if not mistake:
        for i in range(0, len(library)):
            if library[i]["ID"] == inp:
                library.pop(i)

def addbook():
    print("<Add a book>")
    mistake = False
    info1 = input('Title: ')
    if info1 == "-":
        mistake = True
    if not mistake:
        info2 = input('Price: ')
        if info2 == "-":
            mistake = True
    if not mistake:
        info3 = input('Shelf: ')
        if info3 == "-":
            mistake = True
    if not mistake:
        book = {'ID': newid(), 
                'title': str(info1), 
                'price': str(info2), 
                'shelf': str(info3)}
        library.append(book)

def editbook():
    print("<Edit a book>")
    chose = False
    mistake = False
    inp = input("Select ID: ")
    if inp == "-":
        mistake = True
    else:
        inp = int(inp)
    if not mistake:
        for i in range(0, len(library)):
            if library[i]["ID"] == inp:
                selected = i
                chose = True
            if chose:
                info1 = input('Title: ')
                info2 = input('Price: ')
                info3 = input('Shelf: ')
                if info1 != "-":
                    library[selected]["title"] = info1
                if info2 != "-":
                    library[selected]["price"] = info2
                if info3 != "-":
                    library[selected]["shelf"] = info3
running = True

def stoprunning():
    inp = input("Are you sure? All the data will be lost. (Y/N): ")
    if inp == "Y":
        global running
        running = False


def actions():
    print('p - print books list')
    print('a - add a book')
    print('r - remove a book')
    print('e - edit a book')
    print('x - stop the program')
    inp = input('Select action - ')
    if inp == 'a':
        addbook()
    elif inp == 'p':
        printbooks()
    elif inp == 'r':
        removebook()
    elif inp == 'e':
        editbook()
    elif inp == 'x':
        stoprunning()
    else:
        print("Unknown command")

def printstartmessage():
    print("Welcome to library book managment program!")
    print("TIP: If you make a mistake in action choise, type - in the following input field")

# ------- THE RUNNING CODE --------- #
printstartmessage()
while running:
    actions()
