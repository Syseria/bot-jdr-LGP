import nextcord
from nextcord.ext import commands


class Test(commands.Cog, name='Test'):
    """Test command"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="test", description="Test a command.")
    async def test(self, ctx: commands.Context):
        await ctx.send('Test')
        await ctx.send('Does nothing.')

    @nextcord.slash_command(name="test", description="Test a command.")
    async def slash_test(self, interaction: nextcord.Interaction):
        """Test a command"""


def setup(bot: commands.Bot):
    bot.add_cog(Test(bot))
