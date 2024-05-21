import nextcord
from nextcord.ext import commands

import config
from cogs.rules.embed import set_rules
from cogs.rules.rules_view import RulesView


class Rules(commands.Cog, name='Rules'):
    """Setup the Rules channel"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        """Called when the cog is loaded"""
        self.bot.add_view(RulesView())

    @commands.command(name="rules", description="Send the rules with the accept button.")
    @commands.has_permissions(administrator=True)
    async def setup_rules(self, ctx: commands.Context):
        """Send the rules with the accept button."""
        await ctx.send(embed=await set_rules(config.BASE_CHANNEL), view=RulesView())
        await RulesView.wait()

    @nextcord.slash_command(name="rules", description="Send the rules with the accept button.")
    @commands.has_permissions(administrator=True)
    async def slash_setup_rules(self, interaction: nextcord.Interaction):
        """Send the rules with the accept button."""
        await interaction.response.send_message(embed=await set_rules(config.BASE_CHANNEL), view=RulesView())
        await RulesView.wait()


def setup(bot: commands.Bot):
    bot.add_cog(Rules(bot))



