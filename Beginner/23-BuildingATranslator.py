# https://www.youtube.com/watch?v=rfscVS0vtbw&t=10361s

# Vowels to "g" (Giraffe Language, made up) EX: "Hello" -> "Hgllg"

def translate(phrase):
    translation = "" # Used to build the translation letter for letter replacing vowels with "g"(G)
    for letter in phrase:
        if letter.lower() in "aeiou": # If letter is a vowel
            if letter.isupper(): # If letter is uppercase
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter # If letter is not a vowel then add it to the translation
    return translation

print(translate(input("Giraffe Translator. Enter a phrase: ")))