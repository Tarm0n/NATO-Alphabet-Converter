import pandas

alphabet_df = pandas.read_csv("nato_phonetic_alphabet.csv")
alphabet_dict = {row.letter: row.code for (index, row) in alphabet_df.iterrows()}
print(alphabet_dict)


def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        phonetic_code = [alphabet_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(phonetic_code)

generate_phonetic()
