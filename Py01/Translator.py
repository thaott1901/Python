# All vowels become z
def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation += "Z"
            else:
                translation += "z"
        else:
            translation += letter
    return translation


# print(translate(input("Enter a phrase: ")))