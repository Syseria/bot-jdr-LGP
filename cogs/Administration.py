import nextcord
from nextcord.ext import commands
from config import BASE_CHANNEL
import os
from Functions.functions import set_rules, set_info, set_welcome

'''
    Bot
'''


class Administration(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="setup", description="Setups the server.")
    @commands.has_permissions(administrator=True)
    async def setup_discord(self, ctx):
        channels_to_create = ["bienvenue", "information", "règles"]
        await ctx.send("Setting up the server...")
        # retrieves all the categories' names for this discord
        categories = [x for x in ctx.guild.categories]
        # retrieves all the text channels for this discord
        channels = ctx.guild.text_channels

        await ctx.send("Creating required text channels:")

        # Checks if Accueil already exists
        if nextcord.utils.get(categories, name="Accueil"):
            await ctx.send("Accueil existe !")
            category = nextcord.utils.get(categories, name="Accueil")
        else:
            category = await ctx.guild.create_category(name="Accueil", position=0)

        for channel2 in channels_to_create:
            await ctx.send(f"Creating {channel2}")
            new_chan = await ctx.guild.create_text_channel(name=channel2, category=category)
            match channel2:
                case "bienvenue":
                    await set_welcome(new_chan)

                case "règles":
                    await set_rules(new_chan)

                case "information":
                    await set_info(new_chan)


def setup(bot):
    bot.add_cog(Administration(bot))
    print('Cog AdministrationSlash has been loaded!')
