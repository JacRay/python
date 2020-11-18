#vowels to g
def trans(phrase):
    translation =""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.islower():
                translation = translation + "g"
            else:
                translation = translation + "G"
        else:
            translation = translation +letter
    return translation


print((trans(input("Enter a Phrase: "))))
