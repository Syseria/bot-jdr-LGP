import nextcord
from datetime import datetime, timedelta, timezone
from nextcord.ext import commands
from config import CHANNEL_ID


class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="ping", description="Test")
    async def ping(self, ctx):
        latency = self.bot.latency * 1000

        embed = nextcord.Embed(
            title="Pong!",
            description=f"Latency: {latency:.2f}ms",
            colour=nextcord.Color.blurple()
        )
        embed.set_thumbnail(url=ctx.author.display_avatar)
        await ctx.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_join(self, member):
        guild = member.guild
        channel = guild.get_channel(CHANNEL_ID)

        if channel:
            # Example of an embed message
            embed = nextcord.Embed(
                title="Bienvenu !",
                description=f"Bienvenu sur le Discord {guild.name}, {member.mention} !",
                color=nextcord.Color.green()
            )
            embed.set_thumbnail(url=member.display_avatar)
            embed.add_field(name='Information', value="Ce Discord a pour bût de faciliter la gestion et la "
                                                      "communication de l'espace JdR du festival La Grande Partie "
                                                      "qui aura lieu du 8 au 10 Novembre 2024!\n\n"
                                                      "Tu pourras trouver plein d'informations utiles telles que ("
                                                      "mais pas seulement):\n"
                                                      "- La Liste des JdRs proposés lors de l'événement ainsi qu'une "
                                                      "brève introduction de ceux-ci,\n"
                                                      "- Les heures et sessions des différents JdRs,\n"
                                                      "- Comment t'inscrire à un de ces JdRs.",
                            inline=True)
            embed.add_field(name='Joined', value=member.joined_at.strftime("%A, %B %d %Y - %H:%M:%S"),
                            inline=False)

            await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        guild = member.guild
        channel = guild.get_channel(CHANNEL_ID)

        if channel:
            embed = nextcord.Embed(
                title="Au revoir !",
                description=f"Au revoir {member.mention}, merci de ta visite et au plaisir de te voir au festival !",
                color=nextcord.Color.red()
            )
            embed.set_thumbnail(url=member.display_avatar)
            embed.add_field(name='Left', value=datetime.datetime.now().strftime("%A, %B %d %Y - %H:%M:%S"),
                            inline=False)

            await channel.send(embed=embed)


class GeneralSlash(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @nextcord.slash_command(name="ping", description="Test")
    async def ping(self, interaction: nextcord.Interaction):
        latency = self.bot.latency * 1000

        embed = nextcord.Embed(
            title="Pong!",
            description=f"Latency: {latency:.2f}ms",
            colour=nextcord.Color.blurple()
        )
        embed.set_thumbnail(url=interaction.user.display_avatar)
        await interaction.response.send_message(embed=embed)


def setup(bot):
    bot.add_cog(General(bot))
    print('Cog General has been loaded!')
    bot.add_cog(GeneralSlash(bot))
    print('Cog GeneralSlash has been loaded!')
