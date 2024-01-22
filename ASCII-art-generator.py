import pyfiglet

def ascii_converter(text):
    ascii_art = pyfiglet.figlet_format(text)
    print(ascii_art)

text =input("saisir le texte à convertir :")
ascii_converter(text)
    