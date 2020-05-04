import json
import click

CONFIG_FILE_NAME = "dizbot_config.json"

class DizbotConfig:
    """ Configurations of the discord bot to build """
    def __init__(self):
        self.commands = dict()
        self.command_prefix = ""
        self.client_token = ""
    
    def save_config_to_file(self):
        with click.open_file(CONFIG_FILE_NAME, mode="w", lazy=True) as f:
            json.dump(self.__dict__, f)
            f.close()

