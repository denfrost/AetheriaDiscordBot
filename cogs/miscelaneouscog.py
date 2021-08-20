import discord # Currently unused. Used in sending Discord messages.
from discord.ext import commands
from random import randint

class Miscellaneous(commands.Cog, description='Random, unassigned commands.'): # Defines the cog name.
    def __init__(self, bot): # Initializes the cog.
        self.bot = bot

    @commands.command(name='buzzword', help='Prints a random buzzword.')
    async def command(self, ctx): # Adds a simple template command.
        buzzwordList = ["Advertainment", "Big Data", "Content Is King", "Customer Journey", "Deep Dive", "Growth Hacking", "Hyperlocal", "Low Hanging Fruit", "Move the Needle", "Retargeting", "Alignment", "Disruptor/Disruptive", "Freemium", "Leverage", "Quick Win", "Quota", "Value Add", "Wheelhouse", "Customer Acquisition", "Customer-Centric/Customer Centricity", "Customer Lifecycle", "Customer Retention", "Personalization", "Touchpoint", "Voice of the Customer", "Clickbait", "Earned Media", "Live Streaming", "Micro-Influencer", "User-Generated Content", "FOMO", "Lit", "Spilling Tea", "TL;DR"]
        randChoice = randint(0, len(buzzwordList)-1)
        buzzword = buzzwordList[randChoice]
        await ctx.send(buzzword)

def setup(bot): # Loads the cog into the bot.
    bot.add_cog(Miscellaneous(bot))
    print('Miscellaneous cog successfully loaded.')