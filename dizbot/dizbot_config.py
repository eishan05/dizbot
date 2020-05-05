import json
import click

CONFIG_FILE_NAME = "dizbot_config.json"
CLIENT_TOKEN_FILE_NAME = "client_token.txt"
GITIGNORE_FILE_NAME = ".gitignore"

class DizbotConfig:
    """ Configurations of the discord bot to build """

    DEFAULT_NOT_SET = "not-set"

    def __init__(self):
        self.commands = dict()
        self.command_prefix = self.DEFAULT_NOT_SET
        self.client_token = self.DEFAULT_NOT_SET
    
    def save_config_to_file(self):
        with click.open_file(CONFIG_FILE_NAME, mode="w", lazy=True) as f:
            json.dump(self.__dict__, f)
            f.close()
        with click.open_file(CLIENT_TOKEN_FILE_NAME, mode="w", lazy=True) as f:
            f.write(self.client_token)
            f.close()
        with click.open_file(GITIGNORE_FILE_NAME, mode="a+", lazy=True) as f:
            f.seek(0)
            file_data = f.read()
            if CONFIG_FILE_NAME not in file_data:
                f.write("\n# dizbot files\n\n")
                f.write(CONFIG_FILE_NAME + "\n")
            if CLIENT_TOKEN_FILE_NAME not in file_data:
                f.write(CLIENT_TOKEN_FILE_NAME + "\n")
    
    def read_config_from_file(self):
        """ Returns true if successfully read """
        success = True
        try:
            with click.open_file(CONFIG_FILE_NAME, mode="r", lazy=True) as f:
                json_object = json.load(f)
                if type(json_object["commands"]) is dict:
                    self.commands = json_object["commands"]
                else:
                    success = False
                if type(json_object["command_prefix"]) is str:
                    self.command_prefix = json_object["command_prefix"]
                else:
                    success = False
                if type(json_object["client_token"]) is str:
                    self.client_token = json_object["client_token"]
                else:
                    success = False
                f.close()
        except FileNotFoundError:
            success = False
        return success

    def clear(self):
        self.commands = dict()
        self.command_prefix = self.DEFAULT_NOT_SET
        self.client_token = self.DEFAULT_NOT_SET
    
    def __str__(self):
        bot_commands = "Commands: " + str(self.commands)
        bot_prefix = "Prefix: " + self.command_prefix
        bot_client_token = "Client token: " + self.client_token
        return bot_commands + "\n" + bot_prefix + "\n" + bot_client_token
