print('WELCOME TO THE REALM OF NAKOSIA. What is your name, traveller?')
playername=str(input())
print('It is good to meet you', playername+".")
print("Your adventures in this world will involve combat. You must choose a class. This will determine your abilities.")
playerclass=str(input())
print('Interesting.')
if "Knight" == playerclass:
    print("You are a great warrior, etc.")
if "Mage" == playerclass:
    print("You are a magic dude, etc.")
if "Rogue" == playerclass:
    print("You are a sneaky boy, etc.")
