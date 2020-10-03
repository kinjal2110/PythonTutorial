# Snack Water Gun
'''
this game i explained in gujrati as i understand.
koi pan ek manas snack, water , or gun bnavi ske.
if ek e snack bnavyo and bija e water bnavyu so snack e water ne pi jy and water out./snack winner
if ek e water bnavyu bija e gun bnavi so gun e water ma padi jse, gun out/water winner.
if el e gun bnavi, bija e snack bnavyu so gun e snack pr attack krse snack out/gun winner.
'''
import random
lst = ['s', 'w', 'g']
chance = 10
no_of_chance = 0
computer_point = 0
human_point = 0
print("\t\t\t\tSnack Water Gun G A M E")
while no_of_chance < chance:
    i = input("Press anyone of them\n snack for s\n water for w\n gun for g\n")
    random1 = random.choice(lst)

    # if random computer input and human input are same then tie
    if i == random1:
        print("Tie both 0 point to each")

    #if user choose snack and computer choose gun then gun win because gun shoot snack.
    elif i == 's' and random1 == 'g':
        computer_point = computer_point +1
        print(f"your guess {i} and computer guess is {random1}\n")
        print("computer wins 1 point\n")
        print(f"computer point is {computer_point} and your point is {human_point}")

    # if user choose gun and computer choose water then computer win because gun goes on water.
    elif i == 'g' and random1 == 'w':
        computer_point = computer_point + 1
        print(f"your guess {i} and computer guess {random1}\n")
        print("computer wins 1 point\n")
        print(f"computer point is {computer_point} and your point is {human_point}")

    #if user choose water and computer choose snack then computer win because snack drink all the water.
    elif i == 'w' and random1 == 's':
        computer_point = computer_point +1
        print(f"your guess {i} and computer guess is {random1}\n")
        print("computer wins 1 point\n")
        print(f"computer point is {computer_point} and your point is {human_point}")

    # if user choose snack and computer choose water then user win because snack drink all water.
    elif i == 's' and random1 == 'w':
        human_point = human_point + 1
        print(f" your guess {i} and computer guess {random1}\n")
        print("human wins 1 point\n")
        print(f"computer point is {computer_point} and your point is {human_point}")

    # if user choose water and computer choose gun then user win because gun goes on water.
    elif i == 'w' and random1 =='g':
        human_point = human_point +1
        print(f"your guess {i} and computer guess is {random1}\n")
        print("computer wins 1 point\n")
        print(f"computer point is {computer_point} and your point is {human_point}")

    #if user enter invalid input.
    else:
        print("you have entered wrong input\n")

    no_of_chance = no_of_chance + 1
    print(f"{chance - no_of_chance} is left out of {chance}\n")

print("Game over")

if computer_point > human_point:
    print("Computer wins and you loose")

elif computer_point < human_point:
    print("You wins and computer loose")

print(f"your point is {human_point} and computer point is {computer_point}")