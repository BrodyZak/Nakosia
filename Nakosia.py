print("-Version alpha 0.01-")
print("+Created by Brody Zak+")

print(" _        _______  _        _______  _______ _________ _______ ")
print("( (    /|(  ___  )| \    /\(  ___  )(  ____ \\__   __/ (  ___  )")
print("|  \  ( || (   ) ||  \  / /| (   ) || (    \/   ) (   | (   ) |")
print("|   \ | || (___) ||  (_/ / | |   | || (_____    | |   | (___) |")
print("| (\ \) ||  ___  ||   _ (  | |   | |(_____  )   | |   |  ___  |")
print("| | \   || (   ) ||  ( \ \ | |   | |      ) |   | |   | (   ) |")
print("| )  \  || )   ( ||  /  \ \| (___) |/\____) |___) (___| )   ( |")
print("|/    )_)|/     \||_/    \/(_______)\_______)\_______/|/     \|")
print("")
print("What is your name, traveller?")

# set player's name
playername = input()

print('Welcome,', playername + ".")
print("Your adventures in this world will involve combat. You must choose a class. This will determine your abilities.")

# choose player's class
playerclass = input()
print('Interesting.')

#initialize player class
if playerclass in ["Knight", "knight"]:
    print("You are strong.")
    hp = 200
    str = 8
    magic = 1
    spd = 4
if playerclass in ["Mage", "mage"]:
    print("You are magic.")
    hp = 120
    str = 3
    magic = 8
    spd = 5
if playerclass in ["Rogue", "rogue"]:
    print("You are sneaky.")
    hp = 150
    str = 5
    magic = 2
    spd = 8

#choose path
print("Four paths stretch out before you.")
print("A mountain to the North.")
print("A forest to the West")
print("A cave to the East.")
print("A desert to the South.")
print("You must make a decision. What is your choice?")
start_path = input()

if start_path in ["North", "north", "Mountain", "mountain"]:
    start_path = "north"
if start_path in ["West", "west", "Forest", "forest"]:
    start_path = "west"
if start_path in ["East", "east", "Cave", "cave"]:
    start_path = "east"
if start_path in ["South", "south", "Desert", "desert"]:
    start_path = "south"

#the adventure begins
print(playername, "the", playerclass, "sets out", start_path, "in search of adventure.")

# death
if hp < 1:
    print("      @@@@@@@@@@@@@@@@@@")
    print("    @@@@@@@@@@@@@@@@@@@@@@@")
    print("  @@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print(" @@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("@@@@@@@@@@@@@@@/      \@@@/   @")
    print("@@@@@@@@@@@@@@@@\      @@  @___@")
    print("@@@@@@@@@@@@@ @@@@@@@@@@  | \@@@@@")
    print("@@@@@@@@@@@@@ @@@@@@@@@\__@_/@@@@@")
    print(" @@@@@@@@@@@@@@@ \_|_|_|_|_|_|_|_|")
    print("  @@@@@@@@@@@@@|  | | | | | | | |");
    print("                \_|_|_|_|_|_|_|_|");
    print("This looks like the end for you, traveller.")
    death_response = input()
    exit()

# begin journey north
if start_path in ["north"]:
    print("                  ,sdPBbs.")
    print("                ,d$$$$$$$$b.")
    print("               d$P'`Y'`Y'`?$b")
    print("              d'    `  '  \ `b")
    print("             /    |        \  `")
    print("            /    / \       |   `")
    print("       _,--'        |      \    |")
    print("      /' _/          \   |        '")
    print("    _/' /'             |   \        `-.__")
    print("  __/'       ,-'    /    |    |     \      `--...__")
    print("/'          /      |    / \     \     `-.           ``")
    print("Covering your face, you begin to make your way towards the mountain's summit.")
    print("The winds and cold are brutal, but you persevere.")
    print("...")
    print("time passes")
    print("...")
    print("You have been travelling for quite some time, and the sun is beginning to set.")
    print("Now is the time for a decision.")
    print("You can either press onward, or you can make camp for the night and set out again tomorrow.")
    print("the choice is yours.")
    north_choice1 = input("")

# make camp
if north_choice1 in ["stop", "Stop", "camp", "Camp", "make camp", "Make camp", "rest", "Rest", "Take a break", "take a break", "Take break", "take break"]:
    print("You quickly throw together a ramshackle camp with what little you have on hand and sleep for the night.")
    print("Lying your head on your supplies, you manage to drift off to sleep.")
    print("...")
    print("You are rudely awakened by a low-pitched growl coming from outside. Do you investigate?(y/n)")
    wolf_choice1 = input()

    # face wolf
    if wolf_choice1 in ["y", "Y", "yes", "Yes,"]:
        print("You emerge from your shelter to see a large wolf staring back at you, saliva dripping from it's jaw.")
        print("--ICE WOLF--")
        print("=HP: 30")
        print("=STR: 5")
        print("=SPD: 6")
        print("=MGK: 0")
        print("It's eyes shine a brilliantly as it pierces you with it's gaze. What do you do?")
        wolf_choice2 = input();

    # hide from wolf
    if wolf_choice1 in ["n", "N", "No", "no"]:
        print("You hide in your shelter, hoping that whatever is outside will leave you alone.")
        print("...")
        print("This will obviously not be the case.")
        print("The ice wolf that was outside grows tired of waiting and tears through the side of your shelter, attacking you.")
        hp -= 20
        print("HP:", hp)
        print("You struggle with the wolf until you manage to throw it away from you.")
        print("Blood drips from your wound as you stare at your enemy.")
        print("--ICE WOLF--")
        print("=HP: 30")
        print("=STR: 5")
        print("=SPD: 6")
        print("=MGK: 0")
        print("It's eyes shine a brilliantly as it pierces you with it's gaze. What do you do?")
        wolf_choice2 = input()


if north_choice1 in ["Continue", "continue", "keep going", "Keep going", "Don't stop", "don't stop", "press on", "Press on", "Press onwards", "press onwards"]:
    print("Forsaking rest, you continue forwards. The winds take their toll, and you are weakened by the extended exposure.")
    hp -= 15
    print("HP:", hp)
    print("You eventually collapse into the snow.")
    print("...")
    print("Time passes")
    print("...")



print("You wake up as the sun rises.")