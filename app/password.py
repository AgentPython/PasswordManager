from cryptography.fernet import Fernet
from .case_dict import CaseInsensitiveDict
class PasswordManager:

    def __init__(self):
        self.key = None
        self.password_file = None
        self.password_dict = {}

    def create_key(self, path):
        path = 'output/keys/' + path + '.key'
        self.key = Fernet.generate_key()
        with open(path, 'wb') as file:
            file.write(self.key)

    def load_key(self, path):
        path = 'output/keys/' + path + '.key'
        with open(path, 'rb') as file:
            self.key = file.read()

    def create_password_file(self, path, initial_values=None):
        path = 'output/passwords/' + path + '.pw'
        self.password_file = path

        if initial_values is not None:
            for key, value in initial_values.items():
                self.add_password(key, value.email, value.password)

    def load_password_file(self, path):
        path = 'output/passwords/' + path + '.pw'
        self.password_file = path

        with open(path, 'r') as file:
            for line in file:
                site, encrypted_email, encrypted_password = line.split(":")
                if self.key is not None:
                    self.password_dict[site] = {
                        "email": Fernet(self.key).decrypt(encrypted_email.encode()).decode(),
                        "password": Fernet(self.key).decrypt(encrypted_password.encode()).decode()
                    }

    def add_password(self, site, email, password):
        self.password_dict[site] = {
            "email": email,
            "password": password
        }

        if self.password_file is not None:
            with open(self.password_file, 'a+') as file:
                if self.key is not None:
                    encrypted_email = Fernet(self.key).encrypt(email.encode())
                    encrypted_password = Fernet(self.key).encrypt(password.encode())
                    file.write(site + ":" + encrypted_email.decode() + ":" + encrypted_password.decode() + "\n")

    def get_password(self, site):
        new_dict = CaseInsensitiveDict(data=self.password_dict)
        return new_dict[site]

    def get_all_passwords(self):
        return self.password_dict
