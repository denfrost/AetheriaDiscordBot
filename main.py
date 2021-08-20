# Imports
import discord
from discord.ext import commands
from pretty_help import PrettyHelp
import os
import keep_alive

# Defines necessary variables.
TOKEN = os.environ['BOT_TOKEN']
description = 'The manager of the Aetheria Project.'

# Keeps web dashboard online.
keep_alive.keep_alive()

# Defines 'bot', and it's prefix and description.
bot = commands.Bot(command_prefix='`', help_command=PrettyHelp(color=5, index_title='Command Categories'), description=description)

@bot.event
async def on_ready():
    # Prints a message showing the bot is online.
    print(f'{bot.user.name} is ready for micromanagement.')

    # Changes the bot's status.
    await bot.change_presence(status=discord.Status.online, activity=discord.Game('Aetheria Project Management'))

    for filename in os.listdir('./cogs'):
      if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')


bot.run(TOKEN, reconnect=True)
