from rich.theme import Theme
custom_theme = Theme({
    "number": "red",
    "text": "bold white",
    "title": "bold #ffffff"
})

title = """
   ▄███████▄    ▄████████    ▄████████    ▄████████  ▄█     █▄   ▄██████▄     ▄████████ ████████▄  
  ███    ███   ███    ███   ███    ███   ███    ███ ███     ███ ███    ███   ███    ███ ███   ▀███ 
  ███    ███   ███    ███   ███    █▀    ███    █▀  ███     ███ ███    ███   ███    ███ ███    ███ 
  ███    ███   ███    ███   ███          ███        ███     ███ ███    ███  ▄███▄▄▄▄██▀ ███    ███ 
▀█████████▀  ▀███████████ ▀███████████ ▀███████████ ███     ███ ███    ███ ▀▀███▀▀▀▀▀   ███    ███ 
  ███          ███    ███          ███          ███ ███     ███ ███    ███ ▀███████████ ███    ███ 
  ███          ███    ███    ▄█    ███    ▄█    ███ ███ ▄█▄ ███ ███    ███   ███    ███ ███   ▄███ 
 ▄████▀        ███    █▀   ▄████████▀   ▄████████▀   ▀███▀███▀   ▀██████▀    ███    ███ ████████▀  
                                                                             ███    ███
"""

text = """
██████╗ ███╗   ███╗
██╔══██╗████╗ ████║
██████╔╝██╔████╔██║
██╔═══╝ ██║╚██╔╝██║
██║     ██║ ╚═╝ ██║
╚═╝     ╚═╝     ╚═╝
"""

menu = {
    '1': "Create a new key",
    '2': "Load an existing key",
    '3': "Create a new password file",
    '4': "Load an existing password file",
    '5': "Add a new password",
    '6': "Get a password",
    '7': "List all passwords",
    'q': "Quit"
}
