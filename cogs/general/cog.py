import nextcord
from nextcord.ext import commands
from datetime import datetime, timedelta, timezone
from config import BOT_CHANNEL


class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        guild = member.guild
        channel = guild.get_channel(BOT_CHANNEL)

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
                                                      "Tu pourras trouver plein d'information utiles telles que ("
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
        channel = guild.get_channel(BOT_CHANNEL)

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


def setup(bot: commands.Bot):
    bot.add_cog(General(bot))
