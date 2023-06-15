import pyfiglet
import time
from colorama import Fore, Style

def print_typewriter_colored(text):
    for char in text:
        color = Fore.GREEN  # Change the color here
        print(f"{color}{char}{Style.RESET_ALL}", end='', flush=True)
        time.sleep(0.001)  # Adjust the delay as desired

# Example usage
text = "ZEUS..."
ascii_art = pyfiglet.figlet_format(text)
print_typewriter_colored(ascii_art)
print("hel")
import time

def print_with_delay(statement, delay):
    for char in statement:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

# Example usage
statement = "Hello, world!"
delay = 0.1  # Time gap between each character (in seconds)

print_with_delay(statement, delay)
