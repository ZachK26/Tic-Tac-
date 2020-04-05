
one = "1"
two = "2"
three = "3"
four = "4"
five = "5"
six = "6"
seven = "7"
eight = "8"
nine = "9"
win = "0"
while win == "0":
    print(one + "|  " + two + " |  " + three)
    print("------------")
    print(four + "|  " + five + " |  " + six)
    print("------------")
    print(seven + "|  " + eight + " |  " + nine)

    temp = input("Player X choose a space by typing the corresponding number: ")

    if temp == "1":
        one = "X"
    elif temp == "2":
        two = "X"
    elif temp == "3":
        three = "X"
    elif temp == "4":
        four = "X"
    elif temp == "5":
        five = "X"
    elif temp == "6":
        six = "X"
    elif temp == "7":
        seven = "X"
    elif temp == "8":
        eight = "X"
    elif temp == "9":
        nine = "X"

    print(one + "|  " + two + " |  " + three)
    print("------------")
    print(four + "|  " + five + " |  " + six)
    print("------------")
    print(seven + "|  " + eight + " |  " + nine)

    win = "0"
    if one == "X" and two == "X" and three == "X":
        print("x wins")
        win = "1"
        break
    elif four == "X" and five == "X" and six == "X":
        print("x wins")
        win = "1"
        break
    elif seven == "X" and eight == "X" and nine == "X":
        print("x wins")
        win = "1"
        break
    elif one == "X" and four == "X" and seven == "X":
        print("x wins")
        win = "1"
        break
    elif two == "X" and five == "X" and eight == "X":
        print("x wins")
        win = "1"
        break
    elif three == "X" and six == "X" and nine == "X":
        print("x wins")
        win = "1"
        break
    else :
        win = "0"

    temp = input("Player O choose a space by typing the corresponding number: ")

    if temp == "1":
        one = "O"
    elif temp == "2":
        two = "O"
    elif temp == "3":
        three = "O"
    elif temp == "4":
        four = "O"
    elif temp == "5":
        five = "O"
    elif temp == "6":
        six = "O"
    elif temp == "7":
        seven = "O"
    elif temp == "8":
        eight = "O"
    elif temp == "9":
        nine = "O"

    print(one + "|  " + two + " |  " + three)
    print("------------")
    print(four + "|  " + five + " |  " + six)
    print("------------")
    print(seven + "|  " + eight + " |  " + nine)

    if one == "O" and two == "O" and three == "O":
        print("o wins")
        win = "1"
        break
    elif four == "O" and five == "O" and six == "O":
        print("o wins")
        win = "1"
        break
    elif seven == "O" and eight == "O" and nine == "O":
        print("o wins")
        win = "1"
        break
    elif one == "O" and four == "O" and seven == "O":
        print("o wins")
        win = "1"
        break
    elif two == "O" and five == "O" and eight == "O":
        print("o wins")
        win = "1"
        break
    elif three == "O" and six == "O" and nine == "O":
        print("o wins")
        win = "1"
        break
    else:
        win = "0"



