import random


def opening_sequence():
    while True:
        try:
            cash = int(input("Insert money: "))
            if cash < 0 or cash == 0:
                print("We aren't giving you a loan you poor bastard.")
                continue
            break
        except ValueError:
            print("That money is no good here. \nInsert some REAL money.")
    print(f"Money accepted! \nCurrent Balance: ${cash}")
    return cash


def spinner():
    return random.randint(1, 4)


def spin_outcome(cash):
    cash -= 1
    rows, cols = (3, 3)
    reels = [[spinner() for i in range(cols)] for j in range(rows)]
    reel_giant = []
    for i in range(len(reels)):
        for j in range(len(reels[i])):
            reel_giant.append(reels[i][j])
            print(reels[i][j], end="      ")
        print("\n  ")
    return reels, cash, reel_giant, cols


def is_spin_win(reel_giant, cols):
    reel_one = []
    reel_two = []
    reel_three = []
    win = 0
    bonus = 0
    for i in range(len(reel_giant)):
        if i % cols == 0:
            reel_one.append(reel_giant[i])
        elif i % cols == 1:
            reel_two.append(reel_giant[i])
        else:
            reel_three.append(reel_giant[i])
    for i in reel_one:
        for j in reel_two:
            for k in reel_three:
                if i == j == k:
                    win += i
                    if i == 4:
                        bonus += 1
    return win, bonus

def winner(win, cash, bonus):
    if win > 0:
        cash += win
        print(f"Congratulations! You've won: ${win}")
    else:
        print("Sorry no win on that spin.")
    if bonus >= 1:
        cash = bonus_game(cash)
    return cash


def bonus_game(cash):
    print("You've entered the bonus! \nYou will win between 100 and 10,000 times the bet!")
    input("Press enter with any input to reveal your winnings: ")
    bonus_win = random.randint(100, 10000)
    print(f"Congratulations! \n!!!JERKPOT!!! \nYou've won: ${bonus_win}")
    cash += bonus_win
    return cash


def balance_check(cash):
    while cash < 1 or cash == 0:
        print("You are out of money.")
        cash = opening_sequence()
        return cash
    else:
        return cash


def spin_again(cash):
    print("----------------")
    print(f"Current Balance: ${cash}")
    spin = input("Spin the reels? \nIt costs $1 to spin. \n(Press enter to spin): ")
    return spin


cash = opening_sequence()
spin = input("Spin the reels? \nIt costs $1 to spin. \n(Press enter to spin): ")
while spin == "":
    [reels, cash, reel_giant, cols] = spin_outcome(cash)
    [win, bonus] = is_spin_win(reel_giant, cols)
    cash = winner(win, cash, bonus)
    cash = balance_check(cash)
    spin = spin_again(cash)
else:
    print("Game Quit.")