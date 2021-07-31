n=10
no_of_guess=1
print("no of guesses 5 times")
while(no_of_guess<=5):
    guess_no=int(input("guess:\n"))
    if guess_no<10:
        print("less")
    elif guess_no>10:
        print("greater")
    else:
        print("correct")
        print(no_of_guess,"no of guess taken")
        break
    print(5-no_of_guess,"no of guess left")
    no_of_guess = no_of_guess +1
if (no_of_guess>5):
    print("over")