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

#Write your code below this line 👇
import random
print('Welcome to Rock, Paper, Scissors!')
selected_hand = int(input('What will you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: '))
cpu_hand = [rock, paper, scissors]
cpu_random = random.randint(0,2)

if selected_hand == 0:
    print(rock)
    print('Computer chose:')
    print(cpu_hand[cpu_random])
    if cpu_hand[cpu_random] == paper:
        print('You lose!')
    elif cpu_hand[cpu_random] == scissors:
        print('You win!')
    else:
        print('Draw!')
elif selected_hand == 1:
    print(paper)
    print('Computer chose:')
    print(cpu_hand[cpu_random])
    if cpu_hand[cpu_random] == scissors:
        print('You lose!')
    elif cpu_hand[cpu_random] == rock:
        print('You win!')
    else:
        print('Draw!')
else:
    print(scissors)
    print('Computer chose:')
    print(cpu_hand[cpu_random])
    if cpu_hand[cpu_random] == rock:
        print('You lose!')
    elif cpu_hand[cpu_random] == paper:
        print('You win!')
    else:
        print('Draw!')

input()