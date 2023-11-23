from dictionaries import CHARS_MORSE, MORSE_CHARS

class MorseCipher:
    def __init__(self):
        self.chars_morse = CHARS_MORSE
        self.morse_chars = MORSE_CHARS

    def text_to_morse(self, user_text):
        result = ""
        for char in user_text:
            if char in self.chars_morse:
                result += f"{self.chars_morse[char]} "
            elif char == " ":
                result += "/"
            else:
                return None  # Invalid characters.
        return result

    def morse_to_text(self, user_text):
        user_text += " "  # Needed for adding the last character.
        result = ""
        morse_letter = ""
        for char in user_text:
            if char in ".-":
                morse_letter += char
            elif char == " ":
                if morse_letter in self.morse_chars:
                    result += f"{self.morse_chars[morse_letter]}"
                else:
                    result += "#"
                morse_letter = ""
            elif char == "/":
                result += " "
            else:
                return None  # Invalid characters.
        return result

    # def enter(self):
    #     direction = input("Enter 'E' for encode or 'D' to decode: ").upper()
    #     text = input("Enter text: ").upper()
    #     if direction == "E":
    #         print(self.text_to_morse(text))
    #     elif direction == "D":
    #         print(self.morse_to_text(text))
    #     else:
    #         print("Invalid input")
