import ctypes
import colorama
from colorama import Fore, Style

# Inicjalizacja biblioteki colorama
colorama.init(autoreset=True)

# Załaduj bibliotekę
# Dla Linuxa
game_lib = ctypes.CDLL("./game_linux.so")
# Dla Windows
# game_lib = ctypes.CDLL("./game.dll")

# Zdefiniuj argumenty i typy zwracane dla funkcji C
game_lib.print_greeting.restype = None
game_lib.get_computer_choice.restype = ctypes.c_char
game_lib.get_computer_choice.argtypes = []
game_lib.determine_winner.restype = None
game_lib.determine_winner.argtypes = [ctypes.c_char, ctypes.c_char]

def response(word):
    print(Fore.GREEN + word + "\n")

def gra_papier_kamien_nozyce():
    opcje = ['k', 'p', 'n']
    while True:
        user_choice = input(Fore.CYAN + "Wybierz swoją opcję (k dla kamienia, p dla papieru, n dla nożyc, q aby zakończyć grę): ").lower().strip()
        if user_choice == 'q':
            break
        elif user_choice not in opcje:
            print(Fore.RED + "Niepoprawny wybór, spróbuj ponownie.")
            continue
        
        computer_choice = game_lib.get_computer_choice()
        game_lib.determine_winner(ctypes.c_char(user_choice.encode('utf-8')), computer_choice)

def main():
    game_lib.print_greeting()
    print(Fore.YELLOW + "Cześć! Jestem Twoim asystentem. Napisz 'exit' aby zakończyć.")
    
    while True:
        response_moo = input(Fore.CYAN + "> ").strip()
        
        if response_moo.lower() == "exit":
            print(Fore.RED + "Do zobaczenia!")
            break
        elif response_moo.lower() in ["hi", "hello", "hej", "cześć"]:
            response("Cześć! Jak mogę Ci pomóc?")
        elif response_moo.lower() in ["jak się masz", "jak tam", "co słychać"]:
            response("Wszystko w porządku, dzięki! A u Ciebie?")
        elif response_moo.lower() in ["dziękuję", "dzieki", "thx"]:
            response("Nie ma za co!")
        elif response_moo.lower() == "graj":
            gra_papier_kamien_nozyce()
        else:
            response("Przepraszam, nie rozumiem. Możesz spróbować powiedzieć coś innego.")

if __name__ == "__main__":
    main()
