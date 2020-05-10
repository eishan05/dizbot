import click
from .dizbot_config import DizbotConfig, DEFAULT_NOT_SET
from .dizbot_utils import DizbotUtils
from .dizbot_generator import DizbotGenerator

pass_dizbot_config = click.make_pass_decorator(DizbotConfig, ensure=True)

@click.group(invoke_without_command=True)
@click.pass_context
@pass_dizbot_config
def cli(dizbot_config, ctx):
  if ctx.invoked_subcommand is None:
    DizbotUtils.output("You are using dizbot, a command line tool to help you seemlessly create discord bots in python!")

@cli.command()
@pass_dizbot_config
def create(dizbot_config):
  DizbotUtils.handle_persistent_config(dizbot_config)
  if click.confirm("Do you want to add commands to the bot?"):
    add_commands(dizbot_config)
  if click.confirm("Do you want to add event handlers to the bot?"):
    add_event_handlers(dizbot_config)
  if click.confirm("Do you want dizbot to add your bot's client token to your bot for you?"):
    add_client_token(dizbot_config)
  DizbotUtils.give_client_token_information()
  dizbot_config.save_config_to_file()
  click.secho("Bot config created successfully!", fg="green")
  DizbotUtils.output(str(dizbot_config))
  generator = DizbotGenerator(dizbot_config)
  generator.output_bot_code()
  click.secho("Bot code generated successfully!", fg="green")

def add_commands(dizbot_config):
  DizbotUtils.input_command_prefix_from_user(dizbot_config)
  DizbotUtils.input_command_from_user(dizbot_config)
  while click.confirm("Want to add more commands?"):
    DizbotUtils.input_command_from_user(dizbot_config)

def add_event_handlers(dizbot_config):
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

def add_client_token(dizbot_config):
  token = click.prompt("Dicord client token", type=str)
  dizbot_config.client_token = token
  click.secho("Added discord token", fg="green")
