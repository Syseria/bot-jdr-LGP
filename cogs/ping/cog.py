import nextcord
from nextcord.ext import commands


class Ping(commands.Cog, name='Ping'):
    """Receives ping commands"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="ping", description="Checks for a response from the bot")
    async def ping(self, ctx: commands.Context):
        """Checks for a response from the bot"""
        latency = self.bot.latency * 1000

        embed = nextcord.Embed(
            title="Pong!",
            description=f"Latency: {latency:.2f}ms",
            colour=nextcord.Color.blurple()
        )
        embed.set_thumbnail(url=ctx.author.display_avatar)
        await ctx.send(embed=embed)

    @nextcord.slash_command(name="ping", description="Checks for a response from the bot")
    async def slash_ping(self, interaction: nextcord.Interaction):
        latency = self.bot.latency * 1000

        embed = nextcord.Embed(
            title="Pong!",
            description=f"Latency: {latency:.2f}ms",
            colour=nextcord.Color.blurple()
        )
        embed.set_thumbnail(url=interaction.user.display_avatar)
        await interaction.response.send_message(embed=embed)


def setup(bot: commands.Bot):
    bot.add_cog(Ping(bot))
