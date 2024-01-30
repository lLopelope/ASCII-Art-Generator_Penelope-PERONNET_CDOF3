try:
    import pyfiglet
except ImportError:
    print("Le module pyfiglet n'est pas installé. Installation en cours...")
    subprocess.check_call(["python", "-m", "pip", "install", "pyfiglet"])
    import pyfiglet

def ascii_converter(text):
    ascii_art = pyfiglet.figlet_format(text)
    print(ascii_art)

text =input("saisir le texte à convertir :")
ascii_converter(text)
    