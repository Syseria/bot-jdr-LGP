import nextcord
from nextcord.ext import commands

from config import RULES_CHANNEL, BOT_CHANNEL
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
        channel = ctx.guild.get_channel(RULES_CHANNEL)
        bot_channel = ctx.guild.get_channel(BOT_CHANNEL)
        view = RulesView()
        try:
            last_message = await channel.fetch_message(channel.last_message_id)
        except nextcord.NotFound:
            last_message = None

        if last_message:
            await last_message.edit(embed=await set_rules(), view=view)
            await bot_channel.send(f"Rules in {channel.mention} have been updated.", ephemeral=True)
        else:
            await channel.send(embed=await set_rules(), view=view)
            await bot_channel.send(f"Rules sent to {channel.mention}.", ephemeral=True)
        await view.wait()

    @nextcord.slash_command(name="rules", description="Send the rules with the accept button.")
    @commands.has_permissions(administrator=True)
    async def slash_setup_rules(self, interaction: nextcord.Interaction):
        """Send the rules with the accept button."""
        channel = interaction.guild.get_channel(RULES_CHANNEL)
        view = RulesView()
        try:
            last_message = await channel.fetch_message(channel.last_message_id)
        except nextcord.NotFound:
            last_message = None

        if last_message:
            await last_message.edit(embed=await set_rules(), view=view)
            await interaction.response.send_message(f"Rules in {channel.mention} have been updated.", ephemeral=True)
        else:
            await channel.send(embed=await set_rules(), view=view)
            await interaction.response.send_message(f"Rules sent to {channel.mention}.", ephemeral=True)
        await view.wait()


def setup(bot: commands.Bot):
    bot.add_cog(Rules(bot))



