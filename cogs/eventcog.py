import discord # Currently unused. Used in sending Discord messages.
from discord.ext import commands
import json

class Events(commands.Cog): # Defines the cog name.
    def __init__(self, bot): # Initializes the cog.
        self.bot = bot

    @commands.command(name='addevent', help='Add an event to the event list. Usage: `addevent <name of event> <time to execute, format dd:hh:mm>')
    async def addevent(self, ctx, name: str, time: str): # Adds a simple template command.
        i = 0
        events = open("events.json","w+")
        await events.write(time + "\n")
        await events.write(name)
        await ctx.send('Added event "' + name + '" to event register.')

def setup(bot): # Loads the cog into the bot.
    bot.add_cog(Events(bot))
    print('Events cog successfully loaded.')