import random
import itertools

MAX_MODIFICATIONS = 512 # Maximum modification per "single" word
MAX_COMBINATIONS = 326  # Maximum moficiation per "final" word
OUTPUT_FILE = "wordlist.txt"  # Wordlist dump output file

def generate_word_combinations(input_words):
    word_combinations = []

    for length in range(1, len(input_words) + 1):
        for combination in itertools.permutations(input_words, length):
            word_combinations.append(''.join(combination))

    return word_combinations

def modify_word(word):
    modifications = []

    # Add random numbers
    for _ in range(random.randint(0, 3)):
        position = random.randint(0, len(word))
        random_number = str(random.randint(0, 9))
        modified_word = word[:position] + random_number + word[position:]
        modifications.append(modified_word)

    # Randomly capitalize letters
    modified_word = ''.join(random.choice([c.upper(), c]) for c in word)
    modifications.append(modified_word)

    # Add random capitalization
    modifications.append(word.upper())
    modifications.append(word.lower())
    modifications.append(word.capitalize())

    return modifications

def main():
    user_input = input("Input words (separate by \"SPACE\"): ")
    input_words = user_input.split()

    word_combinations = generate_word_combinations(input_words)
    random.shuffle(word_combinations)

    # Use set() for unuquiing the "single" word combination
    modified_combinations = set()

    while len(modified_combinations) < MAX_COMBINATIONS:
        combination = random.choice(word_combinations)

        modifications = modify_word(combination)
        random.shuffle(modifications)

        modified_combinations.update(modifications[:MAX_MODIFICATIONS])

    with open(OUTPUT_FILE, "w") as file:
        for combination in modified_combinations:
            file.write(combination + "\n")

    print(f"Wordlist written into {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
