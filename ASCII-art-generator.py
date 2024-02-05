try:
    import pyfiglet
except ImportError:
    print("Le module pyfiglet n'est pas installé. Installation en cours...")
    import subprocess
    subprocess.check_call(["python", "-m", "pip", "install", "pyfiglet"])
    import pyfiglet

def ascii_converter(text):
    ascii_art = pyfiglet.figlet_format(text)
    print(ascii_art)

#Add of the verification
def get_valid_text():
    text = input("Saisir le texte à convertir : ")
    # Boucle jusqu'à ce que l'utilisateur entre un texte non vide
    while not text.strip():
        print("Le texte ne peut pas être vide. Veuillez entrer un texte valide.")
        text = input("Saisir le texte à convertir : ")
    return text

text = get_valid_text()
ascii_converter(text)
