import discord
from discord.ext import commands
#from pretty_help import PrettyHelp#, Navigation (QUARANTINED)
#from asyncio import sleep
import os
#####
from routes.utils import app
from quart import Quart, redirect, url_for, render_template, request

app = Quart(__name__)

@app.route("/")
async def home():
  return "I'm alive"

#####

# Define the TOKEN var and acquire it from storage.
TOKEN = os.environ['BOT_TOKEN']

# Define the run function.
def run():
  bot.run(TOKEN)
  bot.loop.create_task(app.run_task(host='0.0.0.0', port=8080))

# Set prefix and description for and of bot.
bot = commands.Bot(command_prefix="`", description="Project manager for Aetheria Unreal project.")

# Show bot is ready.
@bot.event
async def on_ready():
  print("The Pointy-Haired Bot is ready for micromanagement.")

  # Changes the bot's status on Discord.
  await bot.change_presence(status=discord.Status.online, activity=discord.Game('Aetheria Project Management'))
  
  # Loads cogs.
  for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')



## COMMANDS
# Todo

# Run the bot.
run()
