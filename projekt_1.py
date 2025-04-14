"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Daniel Skřivánek
email: ddaniel.skrivanek@seznam.cz
discord: vetrex89cz #3080
"""

from task_template import TEXTS

# Seznam registrovaných uživatelů

registrovani_uzivatele = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

# Funkce pro ověření přihlašovacích údajů

def prihlaseni():
    
    uzivatelske_jmeno = input("username: ")
    heslo = input("password: ")
    
    if uzivatelske_jmeno in registrovani_uzivatele and  \
            registrovani_uzivatele[uzivatelske_jmeno] == heslo:
        print("-" * 40)
        print(f"Welcome to the app, {uzivatelske_jmeno}")
        return True
    else:
        print("Unregistered user, terminating the program..")
        return False

# Funkce pro analýzu textu

def analyza_textu(text):
    
    words = text.split()

    titlecase_words = []
    uppercase_words = []
    lowercase_words = []
    word_lenghts = []
    numeric_strings = []

    for word in words:
        stripped_word = word.strip(".,")

        word_lenghts.append(len(stripped_word))
        
        if stripped_word.istitle():
            titlecase_words.append(word)
        elif stripped_word.isupper():
            uppercase_words.append(word)
        elif stripped_word.islower():
            lowercase_words.append(word)

        if stripped_word.isdigit():
            numeric_strings.append(stripped_word)

    numeric_sum = sum(int(word) for word in numeric_strings)

    word_length_occurrences = {}
    for length in set(word_lenghts):
            word_length_occurrences[length] = word_lenghts.count(length)
            
    print(f"There are {len(words)} words in the selected text.")
    print(f"There are {len(titlecase_words)} titlecase words.")
    print(f"There are {len(uppercase_words)} uppercase words.")
    print(f"There are {len(lowercase_words)} lowercase words.")
    print(f"There are {len(numeric_strings)} numeric words.")
    print(f"The sum of all the numbers {numeric_sum}")

    print("-" * 40)
    print("LEN | OCCURENCES | NR.")
    print("-" * 40)
    for length, occurrences in sorted(word_length_occurrences.items()):
        print(f"{length:2d} | {'*' * occurrences} {occurrences}")


# Hlavní funkce programu
def hlavni():
    
    if prihlaseni():
        print("We have 3 texts to be analyzed.")
        print("-" * 40)
        try:
            vyber = int(input("Enter a number btw. 1 and 3 to select: "))
            print("-" * 40)
            if 1 <= vyber len(TEXTS):
                analyza_textu(TEXTS[vyber - 1])
            else:
                print("Invalid selection, terminating the program..")
        except ValueError:
            print("Invalid input, terminating the program..")

if __name__ == "__main__":
    hlavni()
