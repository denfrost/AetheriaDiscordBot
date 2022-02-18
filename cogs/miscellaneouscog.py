import discord # Currently unused. Used in sending Discord messages.
from discord.ext import commands
from random import randint

class Miscellaneous(commands.Cog, description='Random, unassigned commands.'):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='buzzword', help='Prints a random buzzword.')
    async def buzzword(self, ctx):
        buzzwordList = ["Advertainment", "Big Data", "Content Is King", "Customer Journey", "Deep Dive", "Growth Hacking", "Hyperlocal", "Low Hanging Fruit", "Move the Needle", "Retargeting", "Alignment", "Disruptor/Disruptive", "Freemium", "Leverage", "Quick Win", "Quota", "Value Add", "Wheelhouse", "Customer Acquisition", "Customer-Centric/Customer Centricity", "Customer Lifecycle", "Customer Retention", "Personalization", "Touchpoint", "Voice of the Customer", "Clickbait", "Earned Media", "Live Streaming", "Micro-Influencer", "User-Generated Content", "FOMO", "Lit", "Spilling Tea", "TL;DR"]
        randChoice = randint(0, len(buzzwordList)-1)
        buzzword = buzzwordList[randChoice]
        await ctx.send(buzzword)
    
    @commands.command(name='version', help='Shows the current version of the bot.')
    async def version(self, ctx):
      with open('./static/version.txt', "r") as file:
        version = file.read()
      await ctx.send('Current bot version: `' + version + '`')
    
    @commands.command(name='dashboard', help="DM's the user a link to the  bot dashboard.")
    @commands.has_role('Head Developer')
    async def dashboard(self, ctx):
      user = ctx.author
      await user.send('Dashboard: https://phbconsole.ddns.net/')
    
    @dashboard.error # <- name of the command + .error
    async def dashboard_error(ctx, error):
      if isinstance(error, commands.MissingRole):
        await ctx.send('Only Aetheria developers can use this command. You lack the role Head Developer.')

def setup(bot):
    bot.add_cog(Miscellaneous(bot))
    print('Miscellaneous cog successfully loaded.')