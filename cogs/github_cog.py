import discord # Currently unused. Used in sending Discord messages.
from discord.ext import commands
import urllib
import json

class GitHubCog(commands.Cog): # Defines the cog name.
    async def get_latest_commit(self):
        """
        retrieves the informations of the last commit from github as json
        and converts the information into a python object
        for example the object contains the last commit date and the last commit sha
        This function should not be called very often, because GitHub has a rate limit implemented
        """
        url = "https://github.com/AetheriaMod-UnrealEngine/Aetheria-Unreal/commits/main"
        req = urllib.request.Request(
            url,
            data=None,
            headers={
                'User-Agent': 'easywall by github.com/jpylypiw/easywall'
            }
        )
        response = urllib.request.urlopen(req)
        return json.loads(response.read().decode('utf-8'))


    def __init__(self, bot): # Initializes the cog.
        self.bot = bot

    @commands.command(name='commit', help='Retrieve the latest Github commit from the repository.')
    async def commit(self, ctx): # Adds a simple template command.
        await ctx.send(await self.get_latest_commit())

def setup(bot): # Loads the cog into the bot.
    bot.add_cog(GitHubCog(bot))
    print('GitHub cog successfully loaded.')