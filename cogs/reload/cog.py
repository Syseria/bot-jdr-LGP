import nextcord
import os
from nextcord.ext import commands


class Reload(commands.Cog, name='Reload'):
    """Reloads the bot"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="reload", description="Reloads the bot.")
    @commands.has_permissions(administrator=True)
    async def reload(self, ctx):
        for filename_reload in os.listdir("./cogs"):
            if filename_reload.endswith(".py"):
                self.bot.reload_extension(f"cogs.{filename_reload[:-3]}")
                print(f"Reloaded: {filename_reload}")
        await ctx.send(f"Bot reloaded !")

    @nextcord.slash_command(name="reload", description="Reloads the bot.")
    @commands.has_permissions(administrator=True)
    async def reload(self, interaction: nextcord.Interaction):
        for filename_reload in os.listdir("./cogs"):
            if filename_reload.endswith(".py"):
                self.bot.reload_extension(f"cogs.{filename_reload[:-3]}")
                print(f"Reloaded: {filename_reload}")
        await interaction.response.send_message(f"Bot reloaded !")


def setup(bot: commands.Bot):
    bot.add_cog(Reload(bot))



