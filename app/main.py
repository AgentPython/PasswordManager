from rich.table import Table
from rich.console import Console
from rich import box
from rich.text import Text
from rich.prompt import Prompt

from .password import PasswordManager
from .config import menu, text
from os import system

clear = lambda: system('clear')

pm = PasswordManager()

table = Table(box=box.ROUNDED, show_header=False)
table.add_column("")
table.add_column("", style="green")

for key, item in menu.items():
    table.add_row(key, item)

console = Console()

is_done = False
def switch_choices(choice: str):
    clear()
    match(choice):
        case "1":
            print("Please enter the information")
            name = Prompt.ask("Key Name")
            pm.create_key(name)
        case "2":
            print("Please enter the information")
            name = Prompt.ask("Key Name")
            pm.load_key(name)
        case "3":
            print("Please enter the information")
            name = Prompt.ask("Password Manager Name")
            pm.create_password_file(name)
        case "4":
            print("Please enter the information")
            name = Prompt.ask("Password Manager Name")
            pm.load_password_file(name)
        case "5":
            print("Please enter your account info")
            email = Prompt.ask("Email")
            password = Prompt.ask("Password")
            site = Prompt.ask("Site (Not URL)")
            pm.add_password(site, email, password)
        case "6":
            print("Please enter the info")
            site = Prompt.ask("Site (Not URL)")
            print(pm.get_password(site))
        case "7":
            new_table = Table(box=box.ROUNDED, show_lines=True)
            new_table.add_column("Email")
            new_table.add_column("Password")
            new_table.add_column("Site")

            data = pm.get_all_passwords()
            for site, d in data.items():
                new_table.add_row(d['email'], d['password'], site)

            console.print(new_table)
        case "q":
            global is_done
            is_done = True

def main():
    title = Text(text)
    title.stylize("bold magenta")
    global is_done
    while not is_done:
        console.print(title)
        console.print(table)
        choice_initialize = Prompt.ask("Select using number of choice")
        switch_choices(choice_initialize)


if __name__ == "__main__":
    main()
