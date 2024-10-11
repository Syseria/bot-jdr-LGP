import nextcord
from nextcord.ext import commands

from config import INFO_CHANNEL
from cogs.information.embed import set_info


class Information(commands.Cog, name='Information'):
    """Setup the information channel"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        """Called when the cog is loaded"""

    @commands.command(name="information", description="Setups the information channel.")
    @commands.has_permissions(administrator=True)
    async def setup_info(self, ctx: commands.Context):
        """Setups the information channel."""
        channel = self.bot.get_channel(INFO_CHANNEL)
        await channel.send(embed=await set_info())

    @nextcord.slash_command(name="information", description="Setups the information channel.")
    @commands.has_permissions(administrator=True)
    async def slash_setup_info(self, interaction: nextcord.Interaction):
        """Setups the information channel."""
        channel = interaction.guild.get_channel(INFO_CHANNEL)
        try:
            last_message = await channel.fetch_message(channel.last_message_id)
        except nextcord.NotFound:
            last_message = None

        if last_message is None:
            await channel.send(embed=await set_info())
            await interaction.response.send_message(f"Informations sent to {channel.mention}.", ephemeral=True)
        else:
            await last_message.edit(embed=await set_info())
            await interaction.response.send_message(f"Informations in {channel.mention} have been updated.",
                                                    ephemeral=True)


def setup(bot: commands.Bot):
    bot.add_cog(Information(bot))



