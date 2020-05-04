import click

@click.group(invoke_without_command=True)
@click.pass_context
def cli(ctx):
  if ctx.invoked_subcommand is None:
    click.echo("You are using dizbot, a command line tool to help you seemlessly create discord bots in python!")

@cli.command()
def create():
  if click.confirm("Do you want to add commands to the bot?"):
    add_commands()
  if click.confirm("Do you want to add event handlers to the bot?"):
    add_event_handlers()
  if click.confirm("Do you want dizbot to add your bot's client token to your bot for you?"):
    add_client_token()
  give_client_token_information()
  click.secho("Bot created successfully!", fg="green")

def add_commands():
  click.echo("Adding commands!")

def add_event_handlers():
  click.echo("Adding event handlers!")

def add_client_token():
  token = click.prompt("Dicord client token: ")
  with click.open_file("client_token.txt", mode="w", lazy=True) as f:
    f.write(token)
  click.secho("Added discord token", fg="green")

def give_client_token_information():
  click.echo("You can add/change your bot's client token manually to the file client_token.txt")
  click.secho("WARNING: Please make sure you keep your client token safe, and not give anyone else access to it!", bg="blue", fg="white", bold=True, blink=True)
  click.secho("Please do not push the client_token.txt file to GitHub or any publicly accessible website", bg="blue", fg="white", bold=True, blink=True)
