import nextcord
import os
from nextcord.ext import commands

from cogs.rules.rules_view import RulesView


class Rules(commands.Cog, name='Rules Roles'):
    """Creates buttons that assign roles"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        """Called when the cog is loaded"""
        self.bot.add_view(RulesView())

    @commands.command(name="rulesView", description="Creates a new role view for the rules.")
    @commands.has_permissions(administrator=True)
    async def rules_role(self, ctx: commands.Context):
        """Creates a new role view for the rules."""
        await ctx.send("Test", view=RulesView())


def setup(bot: commands.Bot):
    bot.add_cog(Rules(bot))



