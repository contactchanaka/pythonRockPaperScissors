import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
options = [rock, paper, scissors]


def draw_image(option):
    if 0 <= option < len(options):
        print(options[option])
        valid = True
    else:
        valid = False
    return valid


def who_wins(user, computer):
    if user == computer:
        print("Draw")
    else:
        if options[user] == rock and options[computer] == scissors:
            print("You win !")
        elif options[user] == scissors and options[computer] == paper:
            print("You win !")
        elif options[user] == paper and options[computer] == rock:
            print("You win !")
        else:
            print("You lose !")


game_on = True

while game_on:
    try:
        choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors : "))
        game_on = draw_image(choice)
        if game_on:
            print("Computer Choice: ")
            computer_choice = random.randint(0, 2)
            draw_image(computer_choice)
            who_wins(choice, computer_choice)
        else:
            print("Game Over : Invalid Choice")
    except ValueError as e:
        game_on = False
        print("Game Over : ", e)
