import click

@click.group(invoke_without_command=True)
@click.pass_context
def cli(ctx):
  if ctx.invoked_subcommand is None:
    click.echo("You are using dizbot, a command line tool to help you seemlessly create discord bots in python!")

@cli.command()
def create():
  click.echo("You discord bot will now be created")

