import nextcord
import os
from nextcord.ext import commands

from cogs.button_roles.role_view import RoleView


class ButtonRoles(commands.Cog, name='Roles Roles'):
    """Creates buttons that assign roles"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        """Called when the cog is loaded"""
        self.bot.add_view(RoleView())

    @commands.command(name="roleView", description="Creates a new role view for the rules.")
    @commands.has_permissions(administrator=True)
    async def roles(self, ctx: commands.Context):
        """Creates a new role view for the rules."""
        await ctx.send("test", view=RoleView())


def setup(bot: commands.Bot):
    bot.add_cog(ButtonRoles(bot))



