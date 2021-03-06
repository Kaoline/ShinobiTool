# file --config.py--

import filesystem
import hashlib


class Config:
    pswd = ""
    accounts = {}

    @staticmethod
    def load():
        (Config.pswd, Config.accounts) = filesystem.load_config()

    @staticmethod
    def has_pm_access():
        d = hashlib.sha1(Config.pswd.encode()).hexdigest()
        has_access = d == "e60ec4f5170634d65f6e0d466acd9b921822230a"
        if not has_access:
            print("Mot de passe pour le MPeur incorrect. Envoyez un MP à Kazue pour l'avoir.")
        return has_access

    @staticmethod
    def add_account(login, password):
        Config.accounts[login] = password
        filesystem.save_config(Config.accounts)
