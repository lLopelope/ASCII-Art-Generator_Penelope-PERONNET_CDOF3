import pyfiglet

def generate_ascii_art(text):
    ascii_art = pyfiglet.figlet_format(text)
    print(ascii_art)

if __name__ == "__main__":
    user_input = input("Enter text for ASCII art: ")
    generate_ascii_art(user_input)