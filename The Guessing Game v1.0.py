#!/usr/bin/env python
# coding: utf-8

# # WELCOME TO GUESSING GAME!
# 
# *I'm thinking of a number between 1 and 100*
# 
#   * If your guess is more than 10 away from my number, I'll tell you you're <span style="color:blue">COLD!  </span><br />
#   * If your guess is within 10 of my number, I'll tell you you're <span style="color:red">WARM!  </span> <br />
#   * If your guess is farther than your most recent guess, I'll say you're getting <span style="color:blue">COLDER  </span> <br />
#   * If your guess is closer than your most recent guess, I'll say you're getting <span style="color:red">WARMER  </span> <br />
# <br />
# <font size=5%><strong>LET'S PLAY!</strong></font>

# In[ ]:


import random
a= random.randint(1,100)

print("\nI am thinking of a number between 1 to 100, guess the number ;)")

b=[]
while True: 
    try:
        n=(int(input('\nEnter your first guess:')))
        b.append(n)
    except:
        print("\nInvalid input, please enter a number between 1 to 100")
        continue
    else:
        break

if b[-1] > 100 or b[-1] < 0:
        print("\nOUT OF BOUNDS!")
elif b[-1] == a:
        print("\nBINGO!")
        print("\nYou guessed the number on your first attempt")
elif b[-1] in list(range (a-10,a+11)):
        print('\nWARM!')
elif b[-1] > a+10 or b[-1] < a-10:
        print("\nCOLD!")
                
while b[-1] != a:
    while True: 
        try:
            n=(int(input('\nEnter your next guess:')))
            b.append(n)
        except:
            print("\nInvalid input, please enter a number between 1 to 100")
            continue
        else:
            break
                
    if b[-1] == a:
        print("\nBINGO!, You guessed the number in {} attempts.".format(len(b))) 
    elif b[-1] > 100 or b[-1] < 0:
        print("\nOUT OF BOUNDS!")
    elif abs(b[-1]-a) < abs(b[-2]-a):
        print('\nWARMER')
    elif abs(b[-1]-a) >= abs(b[-2]-a):
        print("\nCOLDER")
    elif (b[-1]) == (b[-2]):
        print("\nYou've guess the same no. again!")
        continue      
## Press Shift + Enter to begin

