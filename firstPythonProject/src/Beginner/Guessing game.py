secret_word = "Sownd"
guess=""
i=0;
out_of_Guess = False

while guess!=secret_word and not(out_of_Guess):
    if i<3:
        guess = input("Enter Guess: ")
        i=i+1
    else:
        out_of_Guess=True

if out_of_Guess:
    print("YOU LOST!")
else:
    print("YOU WON!")
