key = "cat"
guess = ""
count = 0
limit = 3
out_of_guess = False
while guess != key and not out_of_guess:
    if count < limit:
        guess = input("What is the secret animal?")
        count += 1
    else:
        out_of_guess = True

if out_of_guess:
    print("Out of guess, you lose")
else:
    print("You win")