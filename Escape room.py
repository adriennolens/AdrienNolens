import time
def main_room():
    print("Welcome to the main room")
    print("You might already know what your aim is, but for those who don't...")
    time.sleep(3)
    print("Your aim is to escape your kidnappers house")
    print("😧")
    time.sleep(3)
    print("Every room requires specific answers to move onto the next")
    time.sleep(2)
    print("Right now you're in a small cramped room\nYou have a couple of realistic options")
    while True:
        first_answer = input("1. Scream your lungs out and hope someone hears\n2. Patiently wait\n3. Look around for a more secretive way to leave\n(Type 1, 2 or 3)")
        time.sleep(1)
        if first_answer == "1":
            print("Well, that was a terrible idea, your kidnapper has come and taped your mouth")
            game_over()
            break
        elif first_answer == "2":
            print("Nothing happens and you slowly weaken and die")
            game_over()
            break
        elif first_answer == "3":
            print("There's a box in the way of a small hole in the wall that you can just about see, you move it and move on, smart move")
            basement()
            break
        else:
            print("Invalid input, type 1,2 or 3")

def input_check(room1, room2):
    while True:
        basement_choice = input("1. Would you like to slowly and quietly go up the stairs\n2. Go back via the hole to the other room and hope for the best\n(Type 1 or 2)")
        if basement_choice == "1":
            print("You're brave and it pays off, you open the door and no ones around")
            room1()
            break
        elif basement_choice == "2":
            print("Scaredy cat...")
            room2()
            break
        else:
            print("Invalid input, type 1,2 or 3")

def backtomainroom():
    print("Well you're back I guess")
    print("Right now you're in a small cramped room\nYou have a couple of realistic options")
    while True:
        first_answer = input("1. Scream your lungs out and hope someone hears\n2. Patiently wait\n3. Look around for a more secretive way to leave\n(Type 1, 2 or 3)")
        time.sleep(1)
        if first_answer == "1":
            print("Well, that was a terrible idea, your kidnapper has come and taped your mouth")
            game_over()
            break
        elif first_answer == "2":
            print("Nothing happens and you slowly weaken and die")
            game_over()
            break
        elif first_answer == "3":
            print("There's a box in the way of a small hole in the wall that you can just about see, you move it and move on, smart move")
            basement()
            break
        else:
            print("Invalid input, type 1,2 or 3")

def basement():
    time.sleep(2)
    print("You've crept inside the hole and ended up in what you think is the basement")
    print("There are no windows, but there are steps upstairs")
    time.sleep(2)
    while True:
        basement_choice = input(
            "1. Would you like to slowly and quietly go up the stairs\n2. Go back via the hole to the other room and hope for the best\n(Type 1 or 2)")
        if basement_choice == "1":
            print("You're brave and it pays off, you open the door and no ones around")
            winecellar()
            break
        elif basement_choice == "2":
            print("Scaredy cat...")
            backtomainroom()
            break
        else:
            print("Invalid input, type 1,2 or 3")

def winecellar():
    time.sleep(2)
    print("You look around and notice that you're now in a fancy looking wine cellar, this house might be bigger than you thought")
    print("Similarly to the other rooms you're in a desperate situation, and you don't have much choice")
    print("You can...")
    while True:
        wine_choice = input("1. Run up as fast as you can\n2. Bring one of his wine bottles as a weapon, the downside is you'll be slower\n(Type 1 or 2)")
        if wine_choice == "1":
            print("Sadly you thought it would work, but because of the size of the house you didn't notice your kidnapper is there")
            print("You've been caught :(")
            game_over()
            break
        elif wine_choice == "2":
            print("You were careful and snuck up on your kidnapper hitting him with the bottle")
            balcony()
            break
        else:
            print("Invalid input, type 1 or 2")

def balcony():
    time.sleep(2)
    print("You've made it to a balcony and can see the way out, right under you is a swimming pool")
    jump = input("If you want to jump and escape type 'jump'\nIf you're too scared type anything else:")
    if jump.upper == "jump" or jump.upper == " jump":
        win()
    else:
        print("game over")
        game_over()

def game_over():
    print("...\nTry again maybe?")
    print("/"*100)
    play_again()

def win():
    print("Well done, you've managed to escape the estate and reach safety")
    trophy = open("trophy.txt","r")
    print(trophy.read())
    trophy.close()
    play_again()


def play_again():
     while True:
        again = input("Would you like to play again? (Y/N)")
        if again == "Y" or again == "y":
            backtomainroom()
            break
        elif again == "N" or again == "n":
            print("Thanks for playing")
            break
        else:
            print("You haven't typed Y or N")


main_room()

