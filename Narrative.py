import Art
import sys
import time 
import playsound

def slowprint(s):
    for c in s + '\n' :
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1./10)

def level_start_narrative():
    print("You're in prison")
    playsound.playsound('Sounds/Narrator/inprison.wav', True)
    print()
    slowprint("'Hello Prisoner 23875'")
    playsound.playsound('Sounds/Guard/1.wav', True) 
    slowprint("'Welcome to Alcatraz maximum security prison'")
    playsound.playsound('Sounds/Guard/2.wav', True) 
    slowprint("'According to our files you're going to be in here for a while.... So get comfortable!'")
    playsound.playsound('Sounds/Guard/3.wav', True)
    print()
    print("You look around. On your left are two guards standing in front of a doorway.")
    playsound.playsound('Sounds/Narrator/youlookaround.wav', True)
    print("They are both armed.")
    playsound.playsound('Sounds/Narrator/botharmed.wav', True)
    print("They begin to handcuff you.....")
    playsound.playsound('Sounds/Narrator/theybegin.wav', True)
    print()
    playsound.playsound('Sounds/Narrator/doyoucooperatewithguards.mp3', False)
    print("do you cooperate with the guards?  (yes/no)>>")

def levelone_one():
    print()
    print("You sit down in the cell")
    playsound.playsound('Sounds/Narrator/level1_one/1.wav', True)
    print("half an hour later two guards come to collect you")
    playsound.playsound('Sounds/Narrator/level1_one/2.wav', True)
    print()
    slowprint("Prisoner 23875, please follow us to the cafeteria.")
    playsound.playsound('Sounds/Guard/level1_one/1.wav', True)
    print()
    print("The guards lead you to the cafeteria")
    playsound.playsound('Sounds/Narrator/level1_one/3.wav', True)
    print("You go and get your food and sit down to eat it")
    playsound.playsound('Sounds/Narrator/level1_one/4.wav', True)
    print()
    print(".....")
    print()
    print("You notice something strange in your food")
    playsound.playsound('Sounds/Narrator/level1_one/5.wav', True)
    print()
    print("....")
    print("There appears to be a small knife concealed in your food")
    playsound.playsound('Sounds/Narrator/level1_one/6.wav', True)
    print("....")
    print("Do you keep the knife? (yes/no)>>")
    playsound.playsound('Sounds/Narrator/level1_one/7.wav', True)

def levelone_two() :
    print()
    print("You move the bed underneath the window and use it to climb up")
    playsound.playsound('Sounds/Narrator/level1_two/1.wav', True)
    print("You notice a loose bar in the window and remove it, leaving a gap large enough to fit through")
    playsound.playsound('Sounds/Narrator/level1_two/2.wav', True)
    print("You can see the prison yard two stories below you")
    playsound.playsound('Sounds/Narrator/level1_two/3.wav', True)
    print()
    print("You jump")
    playsound.playsound('Sounds/Narrator/level1_two/4.wav', True)
    print()
    slowprint("Ouch!")
    print()
    print("You are now in the prison yard")
    playsound.playsound('Sounds/Narrator/level1_two/5.wav', True)
    print()
    print("A large inmate approaches you...")
    playsound.playsound('Sounds/Narrator/level1_two/6.wav', True)
    print("He asks you if you are new")
    playsound.playsound('Sounds/Narrator/level1_two/7.wav', True)
    print()
    slowprint("How do you answer? (yes/no)>>")
    playsound.playsound('Sounds/Narrator/level1_two/8.wav', True)

def levelone_one_one():
    print()
    print("You played the safe option!")
    playsound.playsound('Sounds/Narrator/level1_one_one/1.wav', True)
    print()
    print("You continue to mind your own business")
    playsound.playsound('Sounds/Narrator/level1_one_one/2.wav', True)
    print()
    print("You are in the process of returning to your cell when you hear an alarm and see red flashing lights")
    playsound.playsound('Sounds/Narrator/level1_one_one/3.wav', True)
    print()
    print("There is an announcement on the PA system...")
    playsound.playsound('Sounds/Narrator/level1_one_one/4.wav', True)
    print()
    slowprint("ATTENTION INMATES")
    playsound.playsound('Sounds/Speaker/1.wav', True)
    print()
    slowprint("WE WILL NOW BE INITIATING A PRISON-WIDE LOCKDOWN")
    playsound.playsound('Sounds/Speaker/2.wav', True)
    print()
    slowprint("ARMED GUARDS HAVE BEEN DEPLOYED, PLEASE LAY FACE DOWN WITH YOUR HANDS BEHIND YOUR BACK")
    playsound.playsound('Sounds/Speaker/3.wav', True)
    print()
    slowprint("FALIURE TO FOLLOW THESE INSTRUCTIONS WILL RESULT IN TERMINATION")
    playsound.playsound('Sounds/Speaker/4.wav', True)
    print()
    print("Do you follow these instructions? (yes/no)>>")
    playsound.playsound('Sounds/Narrator/level1_one_one/5.wav', True)

def levelone_two_two() :
    print()
    print("Your decision has attracted the attention of a group of inmates standing nearby.")
    playsound.playsound('Sounds/Narrator/level1_two_two/1.wav', True)
    print()
    print("The odds are clearly stacked against you")
    playsound.playsound('Sounds/Narrator/level1_two_two/2.wav', True)
    print()
    print("A large inmate swings at you, stunning you temporarily")
    playsound.playsound('Sounds/Narrator/level1_two_two/3.wav', True)
    print("...")
    print("@@@")
    print("&&&")
    print("...")
    print("The adrenaline begins to surge, you see red")
    playsound.playsound('Sounds/Narrator/level1_two_two/4.wav', True)
    print()
    print("You start fighting back")
    playsound.playsound('Sounds/Narrator/level1_two_two/5.wav', True)
    print("You can either fight to injure or fight to kill...")
    playsound.playsound('Sounds/Narrator/level1_two_two/6.wav', True)
    print("Do you fight to kill? (yes/no)>>>")
    playsound.playsound('Sounds/Narrator/level1_two_two/7.wav', True)

def leveltwo_one_one() :
    print()
    print("You reluctantly take the baggy off the doctor and hide it in your underwear")
    playsound.playsound('Sounds/Narrator/level2_one/1.wav', True)
    print()
    print("The guards walk you out of the medical wing of the prison and back to your cell")
    playsound.playsound('Sounds/Narrator/level2_one/2.wav', True)
    print()
    print("At lunch time you head to the yard and ask around for big steve")
    playsound.playsound('Sounds/Narrator/level2_one/3.wav', True)
    print()
    slowprint("'He's over there, by the basketball courts'")
    playsound.playsound('Sounds/Prisoners/1.wav', True)
    print()
    print("You head over to the courts and discretely pass the bag to Steve")
    playsound.playsound('Sounds/Narrator/level2_one/4.wav', True)
    print()
    print("You begin to walk away")
    playsound.playsound('Sounds/Narrator/level2_one/5.wav', True)
    print()
    slowprint("'HEY!... WHERES THE OTHER HALF?")
    playsound.playsound('Sounds/BigSteve/1.wav', True)
    print()
    print("Steve and his gang begin to follow you across the yard")
    playsound.playsound('Sounds/Narrator/level2_one/6.wav', True)
    print()
    print("Do you run? (yes/no)>>")
    playsound.playsound('Sounds/Narrator/level2_one/7.wav', True)

def leveltwo_two_one() :
    print()
    print("You refuse the doctors request")
    playsound.playsound('Sounds/Narrator/level2_twoone/1.wav', True)
    print()
    slowprint("'Very Well.... But i'd suggest you watch your back'")
    playsound.playsound('Sounds/Doctor/twoone/1.wav', True)
    print()
    slowprint("'You've just dug your own grave'")
    playsound.playsound('Sounds/Doctor/twoone/2.wav', True)
    print()
    print("You walk out of the doctors office and the guards lead you back to your cell")
    playsound.playsound('Sounds/Narrator/level2_twoone/2.wav', True)
    print()
    print("You start to think about what the doctor said and wonder if you made the right decision")
    playsound.playsound('Sounds/Narrator/level2_twoone/3.wav', True)
    print()
    print("You soon realise you are being followed by a small group of inmates")
    playsound.playsound('Sounds/Narrator/level2_twoone/4.wav', True)
    print()
    print("You pick up your pace and head round the corner. Up ahead you can see a group of guards")
    playsound.playsound('Sounds/Narrator/level2_twoone/5.wav', True)
    print()
    print("Do you go to the guards for help? (yes/no)>>")
    playsound.playsound('Sounds/Narrator/level2_twoone/6.wav', True)

def leveltwo_two_two() :
    print()
    print("You continue walking away, in an attempt not to look suspicious")
    playsound.playsound('Sounds/Narrator/level2_two_two/1.wav', True)
    print()
    print("The gang catch up with you and you feel a blade press against your back")
    playsound.playsound('Sounds/Narrator/level2_two_two/2.wav', True)
    print()
    slowprint("'You should come with us'")
    playsound.playsound('Sounds/Prisoners/2.wav', True)
    print()
    print("The gang leads you to a small store cupboard and lock the door")
    playsound.playsound('Sounds/Narrator/level2_two_two/3.wav', True)
    print()
    print("They sit you down on a chair in the middle of the room and tie your hands")
    playsound.playsound('Sounds/Narrator/level2_two_two/4.wav', True)
    print()
    print("Outside the door you can hear a group of guards")
    playsound.playsound('Sounds/Narrator/level2_two_two/5.wav', True)
    print()
    print("Do you shout for help? (yes/no)>>")
    playsound.playsound('Sounds/Narrator/level2_two_two/6.wav', True)

def leveltwo_one_one_one() :
    print()
    print("You run as fast as you can away from the gang")
    playsound.playsound('Sounds/Narrator/level2_one_one_one/1.wav', True)
    print()
    print("You approach a small group of guards standing nearby and quickyl explain your situation")
    playsound.playsound('Sounds/Narrator/level2_one_one_one/2.wav', True)
    print()
    print("They laugh at you and ask what you expect them to do about it")
    playsound.playsound('Sounds/Narrator/level2_one_one_one/3.wav', True)
    print()
    print("You run round the corner and hide in a cell you find unlocked")
    playsound.playsound('Sounds/Narrator/level2_one_one_one/4.wav', True)
    print()
    print("You hear the enemy gang pass you by, and breathe a sigh of relief")
    playsound.playsound('Sounds/Narrator/level2_one_one_one/5.wav', True)
    print()
    print("You decide to look around the cell")
    playsound.playsound('Sounds/Narrator/level2_one_one_one/6.wav', True)
    print()
    print("At first glance it seems pretty average")
    playsound.playsound('Sounds/Narrator/level2_one_one_one/7.wav', True)
    print()
    print("There is a poster for the Matrix on the furthest wall of the cell")
    playsound.playsound('Sounds/Narrator/level2_one_one_one/8.wav', True)
    print()
    print("You go and take a closer look. You remove the poster to reveal a tunnel going through the walls of the prison")
    playsound.playsound('Sounds/Narrator/level2_one_one_one/9.wav', True)
    print()
    print("Do you go through the tunnel? (yes/no)>>")
    playsound.playsound('Sounds/Narrator/level2_one_one_one/10.wav', True)

def level_two():
    slowprint("'Prisoner 23875, please follow us down this hallway'")
    playsound.playsound('Sounds/Guard/4.wav', True)
    slowprint("'We are going to take you to the infirmary for a routine physical. It would be wise if you cooperated'")
    playsound.playsound('Sounds/Guard/5.wav', True)
    print()
    print("The guards lead you through the cafeteria towards the medical wing of the hospital.")
    playsound.playsound('Sounds/Narrator/theguardleads.wav', True)
    print()
    slowprint("'Take a seat in the waiting room, the doctor will call you when hes ready'")
    playsound.playsound('Sounds/Guard/6.wav', True)
    print()
    print("You look around at the other inmates in the waiting room. They look scared. You wonder if you should feel the same.")
    playsound.playsound('Sounds/Narrator/youlookaround2.wav', True)
    print("20 gruelling minutes go by, the doctor finally calls you in.")
    playsound.playsound('Sounds/Narrator/20min.wav', True)
    print("After completing the physical and signing some documents, you turn to leave....")
    playsound.playsound('Sounds/Narrator/after.wav', True)
    print()
    slowprint("'Youre new here aren't you?'")
    playsound.playsound('Sounds/Doctor/1.wav', True)
    print("Says the doctor.")
    playsound.playsound('Sounds/Narrator/says.wav', True)
    print()
    print("The doctor then explains to you that there is a strict hierarchy within the prison. Respect has to be earned through completing favours.")
    playsound.playsound('Sounds/Narrator/explain.wav', True)
    print()
    slowprint("'I have a task for you. I need you to take this bag and deliver it to an inmate named Big Steve'")
    playsound.playsound('Sounds/Doctor/2.wav', True) 
    slowprint("'Meet him in the yard at 15:00'")
    playsound.playsound('Sounds/Doctor/3.wav', True)
    print()
    print("The doctor hands you a small bag filled with white powder.")
    playsound.playsound('Sounds/Narrator/whitepowder.wav', True)
    print()
    playsound.playsound('Sounds/Narrator/doyouaccepttask.mp3', False)
    print("Do you accept the task? (yes/no)>>")

def level_one():
    print()
    print("The guards beat you and handcuff you")
    playsound.playsound('Sounds/Narrator/beat.wav', True) 
    print()
    slowprint("'You're going to regret that you little sh*t!'")
    playsound.playsound('Sounds/Guard/7.wav', True)
    print()
    print("The guards beat you more")
    playsound.playsound('Sounds/Narrator/beatmore.wav', True)
    print()
    print("Eventually you wake up in a cold dark cell. Your head hurts and there is dried blood on your prison uniform.")
    playsound.playsound('Sounds/Narrator/eventually.wav', True)
    print("You can see a small window in the top left corner of the room.")
    playsound.playsound('Sounds/Narrator/yousee.wav', True)
    print()
    playsound.playsound('Sounds/Narrator/tryclimboutwindow.mp3', False)
    print("Try and climb out the window? (yes/no)>>")

def ae2_win():
    print()
    print("You decide to fight offense")
    playsound.playsound('Sounds/Narrator/AE1Win/1.wav', True)
    print()
    print("An inmate swings at you... you brace for impact")
    playsound.playsound('Sounds/Narrator/AE1Win/2.wav', True)
    print()
    print("The blow disorientates you but you manage to maintain composure")
    playsound.playsound('Sounds/Narrator/AE1Win/3.wav', True)
    print()
    print("You counter attack with a swift punch to the neck")
    playsound.playsound('Sounds/Narrator/AE1Win/4.wav', True)
    print()
    print("The inmate goes down")
    playsound.playsound('Sounds/Narrator/AE1Win/5.wav', True)
    print()
    print("A prison riot breaks out...")
    playsound.playsound('Sounds/Narrator/AE1Win/6.wav', True)
    print()
    print("The guards are heavily outnumbered")
    playsound.playsound('Sounds/Narrator/AE1Win/7.wav', True)
    print()
    print("In the midst of the riot, you manage to steal a set of keys off an injured guard")
    playsound.playsound('Sounds/Narrator/AE1Win/8.wav', True)
    print()
    print("You swiftly head to the nearest exit")
    playsound.playsound('Sounds/Narrator/AE1Win/9.wav', True)
    print()
    print("You find the van that corresponds to the set of keys and make your escape")
    playsound.playsound('Sounds/Narrator/AE1Win/10.wav', True)
    slowprint("Congratulations")
    playsound.playsound('Sounds/Narrator/AE1Win/11.wav', True)
    

def ae2_lose():
    print()
    print("You decide to fight defense")
    playsound.playsound('Sounds/Narrator/AE1/1.wav', True)
    print("You successfully counter a punch with a swift headbutt that incapacitates your opponent")
    playsound.playsound('Sounds/Narrator/AE1/2.wav', True)
    print()
    print("You regain your balance and attempt to flee the brawl")
    playsound.playsound('Sounds/Narrator/AE1/3.wav', True)
    print()
    print("You head to the nearest exit")
    playsound.playsound('Sounds/Narrator/AE1/4.wav', True)
    print("...")
    print("Just as you think youve gotten away, you feel an arm wrap around your neck")
    playsound.playsound('Sounds/Narrator/AE1/5.wav', True)
    print()
    print("An inmate pulls you to the ground and pummels you")
    playsound.playsound('Sounds/Narrator/AE1/6.wav', True)
    print("EVERYTHING GOES BLACK")
    playsound.playsound('Sounds/Narrator/AE1/7.wav', True)

def ae1_lose():
    print() 
    print("Despite being the lone dissenter, you decide to deviate from the given instructions")
    playsound.playsound('Sounds/Narrator/AE2/1.wav', True)
    print()
    print("Surrounding inmates encourage you to get down on the floor")
    playsound.playsound('Sounds/Narrator/AE2/2.wav', True)
    print()
    print("You hear a team of guards up ahead and decide to cut through the East wing of the prison")
    playsound.playsound('Sounds/Narrator/AE2/3.wav', True)
    print()
    print("You spot unguarded exit up ahead and can see daylight")
    playsound.playsound('Sounds/Narrator/AE2/4.wav', True)
    print()
    print("You are moments away from the exit, you can practically taste freedom")
    playsound.playsound('Sounds/Narrator/AE2/5.wav', True)
    print()
    print("Suddenly, you are ambushed by a troop of guards on your left")
    playsound.playsound('Sounds/Narrator/AE2/6.wav', True)
    print("...")
    print("They mercilessly open fire")
    playsound.playsound('Sounds/Narrator/AE2/7.wav', True)
    print()
    print("The bullets rip through you, killing you instantly.")
    playsound.playsound('Sounds/Narrator/AE2/8.wav', True)
    print()

def ae1_win():
    print()
    print("You drop to the ground and put your hands behind your back")
    playsound.playsound('Sounds/Narrator/AE2Win/1.wav', True)
    print()
    print("In the distance you can hear gunfire")
    playsound.playsound('Sounds/Narrator/AE2Win/2.wav', True)
    print()
    print("A troop of guards begin to run down the corridor towards you")
    playsound.playsound('Sounds/Narrator/AE2Win/3.wav', True)
    print()
    print("You make eye contact with an inmate on the floor to the left of you")
    playsound.playsound('Sounds/Narrator/AE2Win/4.wav', True)
    print()
    print("He starts blinking at you frantically, you wonder if he has something wrong upstairs")
    playsound.playsound('Sounds/Narrator/AE2Win/5.wav', True)
    print()
    print("...")
    print()
    print("Then you realise! Hee is trying to communicate with you through morse code")
    playsound.playsound('Sounds/Narrator/AE2Win/6.wav', True)
    print()
    print("- .-. .. .--.  - .... . --")
    print()
    print("You quickly decipher the code.... TRIP THEM")
    playsound.playsound('Sounds/Narrator/AE2Win/7.wav', True)
    print()
    print("You stick out your foot as the guards run past")
    playsound.playsound('Sounds/Narrator/AE2Win/8.wav', True)
    print()
    print("They go down like dominoes")
    playsound.playsound('Sounds/Narrator/AE2Win/9.wav', True)
    print()
    print("You and the other inmates quickly disarm and execute the guards.")
    playsound.playsound('Sounds/Narrator/AE2Win/10.wav', True)
    print()
    print("You make a break for the nearest exit")
    playsound.playsound('Sounds/Narrator/AE2Win/11.wav', True)
    print()
    print("PRISONER 23875, YOU HAVE SUCCESSFULLY ESCAPED ALCATRAZ. CONGRATULATIONS.")
    playsound.playsound('Sounds/Narrator/AE2Win/12.wav', True)
    print()

def level_two_win2():
    print()
    print("You climb through the tunnel")
    playsound.playsound('Sounds/Narrator/Level2win2/1.wav', True)
    print()
    print("You crawl through until the reach the end")
    playsound.playsound('Sounds/Narrator/Level2win2/2.wav', True)
    print()
    print("You find a hole in a sewage pipe")
    playsound.playsound('Sounds/Narrator/Level2win2/3.wav', True)
    print()
    print("you climb into the sewage pipe")
    playsound.playsound('Sounds/Narrator/Level2win2/4.wav', True)
    print()
    print("The smell is unbearable")
    playsound.playsound('Sounds/Narrator/Level2win2/5.wav', True)
    print()
    print("You proceed to crawl the sewage pipe")
    playsound.playsound('Sounds/Narrator/Level2win2/6.wav', True)
    print()
    print("You find the exit")
    playsound.playsound('Sounds/Narrator/Level2win2/7.wav', True)
    print()
    print("Atlast you are free")
    playsound.playsound('Sounds/Narrator/Level2win2/8.wav', True)

def level_two_gameover2():
    print()
    print("You decide not to go into the tunnel")
    playsound.playsound('Sounds/Narrator/Level2loose2/1.wav', True)
    print()
    print("You deem it too risky")
    playsound.playsound('Sounds/Narrator/Level2loose2/2.wav', True)
    print()
    print("Instead you look at around")
    playsound.playsound('Sounds/Narrator/Level2loose2/3.wav', True)
    print()
    print("You spot a air vent with a screw loose")
    playsound.playsound('Sounds/Narrator/Level2loose2/4.wav', True)
    print()
    print("You pry open the air vent cover")
    playsound.playsound('Sounds/Narrator/Level2loose2/5.wav', True)
    print()
    print("You proceed to crawl into the dark narrow air vent")
    playsound.playsound('Sounds/Narrator/Level2loose2/6.wav', True)
    print()
    print("You travel about 50 Feet")
    playsound.playsound('Sounds/Narrator/Level2loose2/7.wav', True)
    print()
    print("The vent creaks and collapses")
    playsound.playsound('Sounds/Narrator/Level2loose2/8.wav', True)
    print()
    print("You fell into the wardens office")
    playsound.playsound('Sounds/Narrator/Level2loose2/9.wav', True)
    print()
    print("The warden is startled as his coffee and doughnuts fall on him")
    playsound.playsound('Sounds/Narrator/Level2loose2/10.wav', True)
    print("The warden quickly hides his porno magazine")
    playsound.playsound('Sounds/Narrator/Level2loose2/11.wav', True)
    print("With an angry face and stern posture")
    playsound.playsound('Sounds/Narrator/Level2loose2/12.wav', True)
    print()
    print("The warden punishes you for a life sentence for bad behaviour")
    playsound.playsound('Sounds/Narrator/Level2loose2/13.wav', True)
    print()

def level2win() :
    print()
    print("You shout as loud as you can")
    playsound.playsound('Sounds/Narrator/Level2win/1.wav', True)
    print("...")
    print("The guards outside the door burst in")
    playsound.playsound('Sounds/Narrator/Level2win/2.wav', True)
    print()
    print("A fight breaks out between the gang and the prison guards")
    playsound.playsound('Sounds/Narrator/Level2win/3.wav', True)
    print()
    print("You manage to steal a set of keys off a guard who was injured during the fight")
    playsound.playsound('Sounds/Narrator/Level2win/4.wav', True)
    print()
    print("You swiftly head to the nearest exit")
    playsound.playsound('Sounds/Narrator/Level2win/5.wav', True)
    print()
    print("You find the van that corresponds to the set of keys and make your escape")
    playsound.playsound('Sounds/Narrator/Level2win/6.wav', True)
    slowprint("Congratulations")
    playsound.playsound('Sounds/Narrator/Level2win/7.wav', True)

def level2lose() :
    print()
    print("You decide to stay quiet and pray that the gang show you mercy")
    playsound.playsound('Sounds/Narrator/Level2loose/1.wav', True)
    print()
    print("They have other ideas in mind")
    playsound.playsound('Sounds/Narrator/Level2loose/2.wav', True)
    print()
    print("one of the inmates hits you over the head with a plank of wood and everything goes black...")
    playsound.playsound('Sounds/Narrator/Level2loose/3.wav', True)
    print()
    slowprint("GAMEOVER")