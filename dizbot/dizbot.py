import click
from .dizbot_config import DizbotConfig

pass_dizbot_config = click.make_pass_decorator(DizbotConfig, ensure=True)

@click.group(invoke_without_command=True)
@click.pass_context
@pass_dizbot_config
def cli(dizbot_config, ctx):
  if ctx.invoked_subcommand is None:
    click.echo("You are using dizbot, a command line tool to help you seemlessly create discord bots in python!")

@cli.command()
@pass_dizbot_config
def create(dizbot_config):
  if click.confirm("Do you want to add commands to the bot?"):
    add_commands(dizbot_config)
  if click.confirm("Do you want to add event handlers to the bot?"):
    add_event_handlers()
  if click.confirm("Do you want dizbot to add your bot's client token to your bot for you?"):
    add_client_token()
  give_client_token_information()
  dizbot_config.save_config_to_file()
  click.secho("Bot created successfully!", fg="green")

def add_commands(dizbot_config):
  prefix = click.prompt("What should be your bot's command prefix")
  dizbot_config.command_prefix = prefix
  input_command_from_user(dizbot_config, prefix)
  while click.confirm("Want to add more commands?"):
    input_command_from_user(dizbot_config, prefix)
  click.echo("Adding commands!")
  click.echo(dizbot_config.commands)

def add_event_handlers():
  click.echo("Adding event handlers!")

def add_client_token(dizbot_config):
  token = click.prompt("Dicord client token")
  dizbot_config.client_token = token
  click.secho("Added discord token", fg="green")

def give_client_token_information():
  click.echo("You can add/change your bot's client token manually to the file client_token.txt")
  click.secho("WARNING: Please make sure you keep your client token safe, and not give anyone else access to it!", bg="blue", fg="white", bold=True, blink=True)
  click.secho("Please do not push the client_token.txt file to GitHub or any publicly accessible website", bg="blue", fg="white", bold=True, blink=True)

def input_command_from_user(dizbot_config, prefix):
  command_name = click.prompt("What should be the command name")
  while command_name in dizbot_config.commands.keys():
    if click.confirm("Command already present in bot configurations with response: " + dizbot_config.commands[command_name] + ", overwrite it?"):
      break
    else:
      command_name = click.prompt("What should be the command name")
  command_response = click.prompt("What should be the bot's response to " + prefix + command_name)
  dizbot_config.commands[command_name] = command_response

