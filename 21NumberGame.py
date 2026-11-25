"""Game Rules:
The game is played between two players who take turns one after another.
On each turn, a player can call 1 to 3 numbers.
The numbers must be consecutive (for example, 5 6 7) skipping numbers leads to disqualification.
The counting always starts from 1 and continues upward.
The one who calls 21, loses the game."""



# Hint :A winning strategy is to make the total count a multiple of 4 (4, 8, 12, 16, 20) before the opponent’s turn.
def nearestMultiple(num):
    if num >= 4:
        near = num + (4 - (num % 4))
    else : 
        near = 4
    return near

def lose1():
    print("You lose\n")
    print("Better luck next time")
    exit(0)

def check(xyz):
     i = 1
     while i < len(xyz):
        i = 1
        if(xyz[i] - xyz[i-1] != 1):
            return False
        i += 1
     return True


def start1():
    xyz = []
    last = 0

    print("Enter F to play First chance : ")
    print("Enter S to play Second chance : ")

    chance = input("-> ")
    
    if chance.upper() == "F":
        while True:
            if last == 20:
                lose1()


            print("Your Turn\n")
            inp = int(input("How many numbers you wish to enter ? (1-3)\n -> "))

            if 1 <= inp <= 3:
                comp = 4 - inp
            else :
                 print("Wrong input. You are disqualified from the game.")
                 lose1()

            print("Enter Your Numbers : ")
            for _ in range(inp):
                xyz.append(int(input('-> ')))

            last = xyz[-1]

            if not check(xyz):
                print("You haven't entered the consecutive integers")
                lose1()
            if last == 21:
                lose1()

            print("Computer's turn: ")
            for j in range(1 , comp +1):
                xyz.append(last+j)

            print("Numbers after computer turn :", xyz)
            last = xyz[-1]



    elif chance.upper() == "S":
        comp = 1
        last = 0
        while last < 20:
            print("\n Computer's Turn : ")
            for j in range (1, comp+1):
                xyz.append(last + j)
            print("Numbers after computer's turn :", xyz)

            if xyz[-1] == 20:
                lose1()

            print("\nYour Turn : ")
            inp = int(input("How many numbers you wish to enter? (1-3)\n->"))

            print("Enter Your Numbers: ")
            for _ in range(inp):
                xyz.append(int(input("-> ")))
            last = xyz[-1]

            if not check(xyz):
                print("You didn't entered the consecutive numbers : ")
                lose1()

            near = nearestMultiple(last)
            comp = near - last

            if comp == 4:
                comp = 3

        print("CONGRATULATIONS!")
        print("\n You Won")

    else:
        print("Wrong choice .Please Enter S or F ")

game = True

while game :
     ans = input("Do you want to play 21 number game? (Yes \ no)\n-> ")

     if ans.lower() == 'yes':
         start1()
     else:
         nex = input("Do you want to quit the game? (Yes / No)\n -> ")

         if nex.lower() == "yes":
             print("You are quitting the game....")
             exit(0)
         elif nex.lower() == "no":
             print("Continuing...")
         else:
             print("Wrong Choice.")

        





