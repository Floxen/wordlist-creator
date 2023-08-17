# Wordlist Generator

This Python script generates a variety of word combinations from user-provided words. It combines the input words, applies different modifications such as adding numbers, capitalizing letters, and shuffling the words. The resulting combinations are saved to a text file, making it useful for generating wordlists for various purposes like password testing, language analysis, or data generation.

## How to Use

1. Clone the repository or download the script.

2. Open a terminal or command prompt.

3. Navigate to the directory containing the script.

4. Run the script using the following command:

   ```sh
   python3 main.py
   ```

    Enter the words you want to include in the wordlist, separated by spaces.

    The script will generate various combinations of the input words and apply modifications according to your specifications.

    The generated combinations will be saved to a file named wordlist.txt in the same directory.

Customization

    You can customize the maximum number of modifications applied to each combination by adjusting the MAX_MODIFICATIONS variable in the script.

    You can also control the maximum number of total combinations by modifying the MAX_COMBINATIONS variable.

    The output file name can be changed by modifying the OUTPUT_FILE variable.

Example

Input words: "apple" "banana" "cherry"

Generated combinations might include:

    applebanana
    BananaCherry
    cHerryAPple3
    ...
