import discord # Currently unused. Used in sending Discord messages.
from discord.ext import commands

class CogName(commands.Cog): # Defines the cog name.
    def __init__(self, client): # Initializes the cog.
        self.bot = client

    @commands.Cog.listener()
    async def on_ready(self): # Sends a console messages when the cog is loaded.
        print('Template cog successfully loaded.')

    @commands.command(name='command', help='A simple description of the command.')
    async def command(self, ctx): # Adds a simple template command.
        await print('Template command used.')

def setup(bot): # Loads the cog into the bot.
    bot.add_cog(CogName(bot))