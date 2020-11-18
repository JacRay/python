ismale = True
istall = False
if ismale and istall:
    print("You are a male or tall or both")
elif ismale and not(istall):
    print("You are a short male")
elif not(ismale) and istall:
    print("You are not a male but tall")
else:
    print("You are not a male not tall")