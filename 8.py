#Exercise:- Take user input, and we need to say user to those number or less then or greater then number
#           which already has an over program.(it likes binary search).
#   if n=18
# number of guesses is 9
# we need to print number of guesses left
# number of guesses he took to finish.
# if all guesses left then print "game over"

n=18
n_of_guess=1
print("Number of guess is limited to 9")
while(n_of_guess<=9):
    in1 = int(input("Guess any number:"))
    if in1<18:
        print("you enter less number please input greater number")
    elif in1>18:
        print("you enter greater number please input smaller number")
    else:
        print("you won")
        print("number of guesses you took to finish")
        break

    print(9-n_of_guess, "number of guesses left")
    n_of_guess= n_of_guess + 1

    if(n_of_guess>9):
        print("game over")