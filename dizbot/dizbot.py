import click
from .dizbot_config import DizbotConfig, DEFAULT_NOT_SET
from .dizbot_utils import DizbotUtils
from .dizbot_generator import DizbotGenerator

pass_dizbot_config = click.make_pass_decorator(DizbotConfig, ensure=True)
dizbot_run_choices = ["prefix", "command", "event", "token", "create", "exit"]


@click.group(invoke_without_command=True)
@click.pass_context
@pass_dizbot_config
def cli(dizbot_config, ctx):
  if ctx.invoked_subcommand is None:
    DizbotUtils.output("dizbot is a command line tool to help you seemlessly create discord bots in python!")
    click.echo("Use: dizbot run\n")

@cli.command()
@pass_dizbot_config
def run(dizbot_config):
  DizbotUtils.output("dizbot will now walk you through creating a discord bot")
  DizbotUtils.handle_persistent_config(dizbot_config)
  choice = click.prompt("Which option do you pick?", type=click.Choice(dizbot_run_choices))
  while choice != "exit":
    if choice == "prefix":
      handle_prefix(dizbot_config)
    elif choice == "command":
      handle_commands(dizbot_config)
    elif choice == "event":
      handle_events(dizbot_config)
    elif choice == "token":
      handle_client_token(dizbot_config)
    elif choice == "create":
      save_config_and_create_bot(dizbot_config)
    choice = click.prompt("What do you want to do?", type=click.Choice(dizbot_run_choices))

def handle_prefix(dizbot_config):
  DizbotUtils.input_command_prefix_from_user(dizbot_config)

def handle_commands(dizbot_config):
  choice = click.prompt("Do you want to add or remove commands?", type=click.Choice(["add", "remove"]))
  if (choice == "add"):
    add_commands(dizbot_config)
  else:
    remove_commands(dizbot_config)

def add_commands(dizbot_config):
  if dizbot_config.command_prefix == DEFAULT_NOT_SET:
    DizbotUtils.input_command_prefix_from_user(dizbot_config)
  DizbotUtils.input_command_from_user(dizbot_config)
  while click.confirm("Want to add more commands?"):
    DizbotUtils.input_command_from_user(dizbot_config)

def remove_commands(dizbot_config):
  if len(dizbot_config.commands) == 0:
    click.secho("No commands present in current configuration", fg="red")
    return
  click.echo(dizbot_config.commands_to_str())
  choices = list(dizbot_config.commands.keys())
  to_delete = click.prompt("Which command would you like to delete", type=click.Choice(choices))
  dizbot_config.commands.pop(to_delete)
  choices.remove(to_delete)
  click.secho("Removed command " + to_delete, fg="green")
  while len(choices) > 0 and click.confirm("Do you want to remove more?"):
    to_delete = click.prompt("Which command would you like to delete", type=click.Choice(choices))
    dizbot_config.commands.pop(to_delete)
    click.secho("Removed command " + to_delete, fg="green")
  if len(choices) == 0:
    click.echo("Note: all commands have been removed")

def handle_events(dizbot_config):
  if click.confirm("Do you want to send a Direct Message to a member when he joins your server?"):
    msg = ""
    if dizbot_config.on_member_join_message != DEFAULT_NOT_SET:
      click.echo("On member join event is already being handled by sending the following message: " + dizbot_config.on_member_join_message)
      if click.confirm("Do you want to change it?"):
        msg = click.prompt("What message would you like the bot to send", type=str)
      else:
        msg = dizbot_config.on_member_join_message
    else:
      msg = click.prompt("What message would you like the bot to send", type=str)
    dizbot_config.on_member_join_message = msg
  else:
    dizbot_config.on_member_join_message = DEFAULT_NOT_SET

def handle_client_token(dizbot_config):
  token = click.prompt("Dicord client token", type=str)
  dizbot_config.client_token = token
  click.secho("Added discord token", fg="green")

def save_config_and_create_bot(dizbot_config):
  DizbotUtils.give_client_token_information()
  dizbot_config.save_config_to_file()
  click.secho("Bot config created successfully!", fg="green")
  DizbotUtils.output(str(dizbot_config))
  generator = DizbotGenerator(dizbot_config)
  generator.output_bot_code()
  click.secho("Bot code generated successfully!", fg="green")

