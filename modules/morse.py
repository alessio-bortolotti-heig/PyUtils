MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.', '0': '-----', ' ': '/'
}

# Invert the MORSE_CODE_DICT to create a reverse lookup for converting Morse to text
REVERSE_MORSE_CODE_DICT = {v: k for k, v in MORSE_CODE_DICT.items()}

def text_to_morse(text):
    """Convert a string of text to Morse code."""
    morse_code = ''
    for char in text.upper():
        if char in MORSE_CODE_DICT:
            morse_code += MORSE_CODE_DICT[char] + ' '
    return morse_code.strip()

def morse_to_text(morse):
    """Convert a string of Morse code to text."""
    text = ''
    morse_list = morse.split(' ')
    for symbol in morse_list:
        if symbol in REVERSE_MORSE_CODE_DICT:
            text += REVERSE_MORSE_CODE_DICT[symbol]
        elif symbol == '/':
            text += ' '
    return text

def main():
    while True:
        print("\nMorse Code Converter")
        print("1. Text to Morse Code")
        print("2. Morse Code to Text")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            text = input("Enter text to convert to Morse code: ")
            print("Morse Code:", text_to_morse(text))
        elif choice == '2':
            morse = input("Enter Morse code to convert to text (use '/' for space): ")
            print("Text:", morse_to_text(morse))
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid input, please choose a valid option.")

if __name__ == '__main__':
    main()
