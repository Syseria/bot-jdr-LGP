import nextcord
from nextcord.ext import commands


class Test(commands.Cog, name='Test'):
    """Test command"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="test", description="Test a command.")
    async def test(self, ctx: commands.Context):
        await ctx.send('Test')
        """Test a command"""
        val = 1242467877735633008
        channel = 'TEST_CHANNEL'
        path = '../../requirements.txt'
        lineFound: bool = False
        with open("./.env", 'r+') as file:
            lineNum = 0
            for line in file:
                lineNum += 1
                if line.startswith(channel):
                    await ctx.send("Yes")
                    file.seek(lineNum, 1)
                    file.write(f'{channel}={val}')
                    lineFound = True
        #if not lineFound:
        #   with open(path, 'a') as file:
        #      file.write(f'{channel}={val}')

    @nextcord.slash_command(name="test", description="Test a command.")
    async def slash_test(self, interaction: nextcord.Interaction):
        """Test a command"""


def setup(bot: commands.Bot):
    bot.add_cog(Test(bot))
