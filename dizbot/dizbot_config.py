import json
import click

CONFIG_FILE_NAME = "dizbot_config.json"

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
