import random

def rockpaperscissor():
    total = [0, 0, 0]
    while True:
            userinput = input("rock paper scissor: ").lower().strip()
            com = random.choice(['rock' , 'paper' , 'scissor'])
            if userinput == com:
                        print("Draw")
                        total[2] = total[2] + 1
            elif ((userinput == 'paper' and com == 'rock') or
                        (userinput == 'scissor' and com == 'paper') or
                        (userinput == 'rock' and com == 'scissor')):
                        print("You win")
                        total[0] = total[0] + 1
            elif ((userinput == 'scissor' and com == 'rock') or
                        (userinput == 'paper' and com == 'scissor') or
                        (userinput == 'rock' and com == 'paper')) :
                        print('you lose')
                        total[1] = total[1] + 1
            elif userinput == 'stop':
                        print(f"you won {total[0]} times and the computer won {total[1]} times and draw {total[2]} times")
                        break
            else:
                    print('wrong input')


rockpaperscissor()

