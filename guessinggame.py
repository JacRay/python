secret = "giraffe"
guess = ""
count = 0
limit = 3
out_of = False
while guess != secret and not(out_of):
    if count < limit:
        guess = input("Enter Guess:")
        count += 1
    else:
        out_of = True
if out_of:
    print("Out of Guesses")
else:
    print("You Win!!")