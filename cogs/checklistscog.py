import discord # Currently unused. Used in sending Discord messages.
from discord.ext import commands

class Checklists(commands.Cog): # Defines the cog name.
    def __init__(self, bot): # Initializes the cog.
        self.bot = bot

    @commands.command(name='createchecklist', help='Main command for the checklists function.')
    async def checklist(self, ctx): # Adds a simple template command.
        print('')
        # TODO

def setup(bot): # Loads the cog into the bot.
    bot.add_cog(Checklists(bot))
    print('Checklists cog successfully loaded.')