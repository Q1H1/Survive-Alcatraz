import Narrative
import Art
import playsound
def level_start():
    Art.prison()
    Narrative.level_start_narrative()
    answer = input()
    answer = answer.lower()
    print(f"You answered "+answer)
    if answer == "yes":
        level_two()
    elif answer == "no":
        level_one()
    else:
        print("It needs to be a yes or no")
        level_start()
    
def level_one():
    Art.guard()
    Narrative.level_one()
    answer = input()
    answer = answer.lower()
    print(f"You answered "+answer)
    if answer == "yes":
       level_one_two()
    elif answer == "no":
        level_one_one()
    else:
        print("It needs to be a yes or no")
        level_one()
def level_one_two():
    Art.climb()
    Narrative.levelone_two()
    answer = input()
    answer = answer.lower()
    print("Yes or no?")
    print(f"You answered "+answer)
    if answer == "yes":
        level_one_two_two()
    elif answer == "no":
        level_one_one_one()
    else:
        print("It needs to be a yes or no")
        level_one_two()
def level_one_two_two():
    Narrative.levelone_two_two()
    answer = input()
    answer = answer.lower()
    print("Yes or no?")
    print(f"You answered "+answer)
    if answer == "yes":
        level_one_win2()
    elif answer == "no":
        level_one_gameover2()
    else:
        print("It needs to be a yes or no")
        level_one_two_two()
def level_one_one():
    Art.prisoncell()
    Narrative.levelone_one()
    answer = input()
    answer = answer.lower()
    print("Yes or no?")
    print(f"You answered "+answer)
    if answer == "yes":
        level_one_two_two()
    elif answer == "no":
        level_one_one_one()
    else:
        print("It needs to be a yes or no")
        level_one_one()

def level_one_one_one():
    Narrative.levelone_one_one()
    answer = input()
    answer = answer.lower()
    print("Yes or no?")
    print(f"You answered "+answer)
    if answer == "yes":
        level_one_win()
    elif answer == "no":
        level_one_gameover()
    else:
        print("It needs to be a yes or no")
        level_one_one_one()

def level_two():
    Art.arrest()
    Narrative.level_two()
    answer = input()
    answer = answer.lower()
    print(f"You answered "+answer)
    if answer == "yes":
        level_two_one_one()
    elif answer == "no":
        level_two_two_one()
    else:
        print("It needs to be a yes or no")
        level_two()
def level_two_one_one():
    Narrative.leveltwo_one_one()
    answer = input()
    answer = answer.lower()
    print("Yes or no?")
    print(f"You answered "+answer)
    if answer == "yes":
        level_two_one_one_one()
    elif answer == "no":
        level_two_two()
    else:
        print("It needs to be a yes or no")
        level_two_one_one()

def level_two_one_one_one():
    Narrative.leveltwo_one_one_one()
    answer = input()
    answer = answer.lower()
    print("Yes or no?")
    print(f"You answered "+answer)
    if answer == "yes":
        level_two_win2()
    elif answer == "no":
        level_two_gameover2()
    else:
        print("It needs to be a yes or no")
        level_two_one_one_one()
        
def level_two_two_one():
    Narrative.leveltwo_two_one()
    answer = input()
    answer = answer.lower()
    print("Yes or no?")
    print(f"You answered "+answer)
    if answer == "yes":
        level_two_one_one_one()
    elif answer == "no":
        level_two_two()
    else:
        print("It needs to be a yes or no")
        level_two_two_one()
def level_two_two():
    Narrative.leveltwo_two_two()
    answer = input()
    answer = answer.lower()
    print("Yes or no?")
    print(f"You answered "+answer)
    if answer == "yes":
        level_two_win()
    elif answer == "no":
        level_two_gameover()
    else:
        print("It needs to be a yes or no")
        level_two_two()
        
def level_two_gameover():
    Narrative.level2lose()
    Art.gameover()
    playsound.playsound('Sounds/Narrator/GO.wav', False)
    print("GAME OVER")
    print("Do you wish to try restart? ")
    answer = input()
    answer = answer.lower()
    if answer == "yes":
        level_start()
    elif answer == "no":
        endcredits()
    else:
        print("It needs to be a yes or no")
        level_two_gameover()

def level_two_win():
    Narrative.level2win()
    Art.youwon()
    print("Won the game")
    input("Press enter to exit the game")

def level_two_gameover2():
    Narrative.level_two_gameover2()
    Art.gameover()
    playsound.playsound('Sounds/Narrator/GO.wav', False)
    print("GAME OVER")
    print("Do you wish to try restart? ")
    answer = input()
    answer = answer.lower()
    if answer == "yes":
        level_start()
    elif answer == "no":
        endcredits()
    else:
        print("It needs to be a yes or no")
        level_two_gameover()

def level_two_win2():
    Narrative.level_two_win2()
    Art.youwon()
    print("Won the game")
    input("Press enter to exit the game")

def level_one_win():
    Narrative.ae1_win()
    Art.youwon()
    print("Won the game")
    input("Press enter to exit the game")

def level_one_gameover():
    Narrative.ae1_lose()
    Art.gameover()
    playsound.playsound('Sounds/Narrator/GO.wav', False)
    print("Do you wish to try restart? ")
    answer = input()
    answer = answer.lower()
    if answer == "yes":
        level_start()
    elif answer == "no":
        endcredits()
    else:
        print("It needs to be a yes or no")
        level_one_gameover()
        
def level_one_win2():
    Narrative.ae2_win()
    Art.youwon()
    print("Won the game")
    input("Press enter to exit the game")

def level_one_gameover2():
    Narrative.ae2_lose()
    Art.gameover()
    playsound.playsound('Sounds/Narrator/GO.wav', False)
    print("Do you wish to try restart? ")
    answer = input()
    answer = answer.lower()
    if answer == "yes":
        level_start()
    elif answer == "no":
        endcredits()
    else:
        print("It needs to be a yes or no")

def endcredits():
    print("Made by Tim, Morgan")
