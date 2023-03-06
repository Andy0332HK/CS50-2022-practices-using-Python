
ans = "apple"
class text_colors:
    red = '\033[1;31;40m'
    green = '\033[1;32;40m'
    yellow = '\033[1;33;40m'
    ENDC = '\033[0m'

for i in range(6,0,-1):
    print("\nYou have " + str(i) + " tries to guess the 5-letter word I'm thinking of")
    guess = input("Your Guess: ")
    while len(guess) != len(ans):
        guess = input("Your Guess: ")

    if guess == ans:
        print(text_colors.green + guess + text_colors.ENDC)
        print("You are right!")
        break
    else:
        for t in range(len(guess)):
            if guess[t] == ans[t]:
                print(text_colors.green + guess[t] + text_colors.ENDC, end="")
            else:
                for y in range(len(ans)):
                    if guess[t] == ans[y]:
                        print(text_colors.yellow + guess[t] + text_colors.ENDC, end="")
                        break

                    else:
                        print(text_colors.red + guess[t] + text_colors.ENDC, end="")
                        break