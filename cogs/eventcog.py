import discord # Currently unused. Used in sending Discord messages.
from discord.ext import commands
import json

def split(word):
      return [char for char in word]

class Events(commands.Cog): # Defines the cog name.
    def __init__(self, bot): # Initializes the cog.
        self.bot = bot

    @commands.command(name='addevent', help='Add an event to the event list. Usage: `addevent <name of event> <time to execute, format dd:hh:mm>')
    async def addevent(self, ctx, name: str, time: str): # Adds a simple template command.
        with open('events.json','r+') as file:
          data = json.loads(file.read())
        time1 = split(time)
        day = time1[0] + time1[1]
        hour = time1[3] + time1[4]
        minute = time1[6] + time1[7]
        entry = '{"name": '+ name +', "time": {"day": ' + day + ',"hour": ' + hour + ',"minute": '+ minute +',"executed": false}'
        data['events'].append(entry)

def setup(bot): # Loads the cog into the bot.
    bot.add_cog(Events(bot))
    print('Events cog successfully loaded.')