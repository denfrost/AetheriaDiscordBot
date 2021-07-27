import discord
from discord.ext import commands
from pretty_help import Navigation, PrettyHelp
from asyncio import sleep
import random
import os

# Define the TOKEN var and acquire it from storage.
TOKEN = os.environ['BOT_TOKEN']

# Set prefix and description.
bot = commands.Bot(command_prefix="`", description="Project manager for Aetheria Unreal project.")

# Show bot is ready.
@bot.event
async def on_ready():
  print("I'm in")

