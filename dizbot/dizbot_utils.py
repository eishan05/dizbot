import click
import keyword
import builtins
from .dizbot_config import DEFAULT_NOT_SET

COMMAND_PROMPT_NAME = "command name"
PREFIX_PROMPT_NAME = "prefix"

class DizbotUtils:

    @staticmethod
    def give_client_token_information():
        click.echo()
        click.secho("WARNING: Please make sure you keep your client token safe, and not give anyone else access to it!", bg="blue", fg="white", bold=True, blink=True)
        click.secho("Please do not push the client_token.txt file to GitHub or any publicly accessible website", bg="blue", fg="white", bold=True, blink=True)
        click.echo()
    
    @staticmethod
    def input_command_prefix_from_user(dizbot_config):
        prefix = ""
        if dizbot_config.command_prefix != DEFAULT_NOT_SET:
            if click.confirm("You have already set the prefix to " + dizbot_config.command_prefix + " do you want to change it"):
                prefix = DizbotUtils.prompt_input_from_user(PREFIX_PROMPT_NAME)
            else:
                prefix = dizbot_config.command_prefix
        else:
            prefix = DizbotUtils.prompt_input_from_user(PREFIX_PROMPT_NAME)
        dizbot_config.command_prefix = prefix

    @staticmethod
    def input_command_from_user(dizbot_config):
        command_name = DizbotUtils.prompt_input_from_user(COMMAND_PROMPT_NAME)
        while command_name in dizbot_config.commands:
            if click.confirm("Command already present in bot configurations with response: " + dizbot_config.commands[command_name] + ", overwrite it?"):
                break
            else:
                command_name = DizbotUtils.prompt_input_from_user(COMMAND_PROMPT_NAME)
        command_response = click.prompt("What should be the bot's response to " + dizbot_config.command_prefix + command_name, type=str)
        dizbot_config.commands[command_name] = command_response
        click.secho("Added command " + dizbot_config.command_prefix + command_name, fg="green")
    
    @staticmethod
    def handle_persistent_config(dizbot_config):
          if dizbot_config.read_config_from_file():
            DizbotUtils.output("Already found bot config", text_color="green")
            DizbotUtils.output(str(dizbot_config))
            if (click.confirm("Do you want to overwrite the config?")):
                dizbot_config.clear()
                DizbotUtils.output("Overwriting previous bot config", text_color="green")
            else:
                DizbotUtils.output("Keeping previous bot config", text_color="green")
    
    @staticmethod
    def prompt_input_from_user(prompt_name):
        command_input = click.prompt("Please enter " + prompt_name, type=str)
        while not DizbotUtils.is_command_input_clean(command_input, prompt_name):
            command_input = click.prompt("Please enter " + prompt_name + " again", type=str)
        return command_input
    
    @staticmethod
    def is_command_input_clean(input, prompt_name):
        if " " in input:
            click.secho("No whitespace allowed in " + prompt_name, fg="red")
            return False
        elif keyword.iskeyword(input) or input in dir(builtins):
            click.secho(prompt_name + " cannot be reserved keywords in python", fg="red")
            return False
        return True
    
    @staticmethod
    def output(str, text_color=""):
        click.secho("\n" + str + "\n", fg=text_color)
