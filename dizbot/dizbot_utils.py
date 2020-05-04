import click

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
        if dizbot_config.command_prefix != dizbot_config.DEFAULT_NOT_SET:
            if click.confirm("You have already set the prefix to " + dizbot_config.command_prefix + " do you want to change it"):
                prefix = click.prompt("What should be your bot's command prefix")
            else:
                prefix = dizbot_config.command_prefix
        else:
            prefix = click.prompt("What should be your bot's command prefix")
        dizbot_config.command_prefix = prefix

    @staticmethod
    def input_command_from_user(dizbot_config):
        command_name = click.prompt("What should be the command name")
        while command_name in dizbot_config.commands:
            if click.confirm("Command already present in bot configurations with response: " + dizbot_config.commands[command_name] + ", overwrite it?"):
                break
            else:
                command_name = click.prompt("What should be the command name")
        command_response = click.prompt("What should be the bot's response to " + dizbot_config.command_prefix + command_name)
        dizbot_config.commands[command_name] = command_response
    
    @staticmethod
    def handle_persistent_config(dizbot_config):
          if dizbot_config.read_config_from_file():
            click.echo("Already found bot config")
            click.echo(str(dizbot_config))
            if (click.confirm("Do you want to overwrite the config?")):
                dizbot_config.clear()
                click.echo("Overwriting previous bot config")
            else:
                click.echo("Keeping previous bot config")
