import nextcord
from nextcord.ext import commands

import config
from cogs.information.embed import set_info
from cogs.information.info_view import InfoView


class Information(commands.Cog, name='Information'):
    """Setup the information channel"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        """Called when the cog is loaded"""
        self.bot.add_view(InfoView())

    @commands.command(name="information", description="Setups the information channel.")
    @commands.has_permissions(administrator=True)
    async def setup_info(self, ctx: commands.Context):
        """Setups the information channel."""
        await ctx.send(embed=await set_info(config.BASE_CHANNEL), view=InfoView())
        await InfoView.wait()

    @nextcord.slash_command(name="information", description="Setups the information channel.")
    @commands.has_permissions(administrator=True)
    async def slash_setup_info(self, interaction: nextcord.Interaction):
        """Setups the information channel."""
        await interaction.response.send_message(embed=await set_info(config.BASE_CHANNEL), view=InfoView())
        await InfoView.wait()


def setup(bot: commands.Bot):
    bot.add_cog(Information(bot))



