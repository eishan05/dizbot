import click
from .dizbot_config import CLIENT_TOKEN_FILE_NAME

INDENT = "\t"
BOT_VARIABLE = "bot"
BOT_CODE_FILE = "bot.py"

class DizbotGenerator:

    def __init__(self, dizbot_config):
        self.dizbot_config = dizbot_config

    
    def output_bot_code(self):
        code = self.generate_bot_code()
        with click.open_file(BOT_CODE_FILE, mode="w", lazy=True) as f:
            f.write(code)
            f.close()

    def generate_bot_code(self):
        code = self.generate_import_code()
        code += self.generate_bot_declaration_code()
        code += self.generate_commands()
        code += self.generate_run_bot_code()
        return code

    def generate_run_bot_code(self):
        code = "f = open('" + CLIENT_TOKEN_FILE_NAME + "', 'r')\n"
        code += "bot.run(f.read())\n"
        return code
    
    def generate_import_code(self):
        code = "from discord.ext import commands\n\n"
        return code
    
    def generate_bot_declaration_code(self):
        code = BOT_VARIABLE + " = commands.Bot(command_prefix='" + self.dizbot_config.command_prefix + "')\n\n"
        return code
    
    def generate_commands(self):
        code = ""
        for key in self.dizbot_config.commands:
            code += self.generate_command_code(key, self.dizbot_config.commands[key])
        return code

    def generate_command_code(self, command_name, command_response):
        code = "@" + BOT_VARIABLE + ".command()\n"
        code += "async def " + command_name + "(ctx, *args):\n"
        code += INDENT + "await ctx.send('" + command_response + "')\n\n"
        return code
