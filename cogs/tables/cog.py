import nextcord
from nextcord.ext import commands

from config import NEW_TABLE_CHANNEL, BOT_CHANNEL
from cogs.tables.embed import set_new_table
from cogs.tables.table_view import NewTableView


class NewTable(commands.Cog, name='NewTable'):
    """Setup the New Table channel"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        """Called when the cog is loaded"""
        self.bot.add_view(NewTableView())

    @commands.command(name="tables", description="Send the rules with the accept button.")
    @commands.has_permissions(administrator=True)
    async def setup_new_tables(self, ctx: commands.Context):
        """Send the rules with the accept button."""
        channel = ctx.guild.get_channel(NEW_TABLE_CHANNEL)
        bot_channel = ctx.guild.get_channel(BOT_CHANNEL)
        view = NewTableView()
        try:
            last_message = await channel.fetch_message(channel.last_message_id)
        except nextcord.NotFound:
            last_message = None

        if last_message:
            await last_message.edit(embed=await set_new_table(), view=view)
            await bot_channel.send(f"Rules in {channel.mention} have been updated.", ephemeral=True)
        else:
            await channel.send(embed=await set_new_table(), view=view)
            await bot_channel.send(f"Rules sent to {channel.mention}.", ephemeral=True)
        await view.wait()

    @nextcord.slash_command(name="tables", description="Send the rules with the accept button.")
    @commands.has_permissions(administrator=True)
    async def slash_setup_rules(self, interaction: nextcord.Interaction):
        """Send the rules with the accept button."""
        channel = interaction.guild.get_channel(NEW_TABLE_CHANNEL)
        view = NewTableView()
        try:
            last_message = await channel.fetch_message(channel.last_message_id)
        except nextcord.NotFound:
            last_message = None

        if last_message:
            await last_message.edit(embed=await set_new_table(), view=view)
            await interaction.response.send_message(f"Rules in {channel.mention} have been updated.", ephemeral=True)
        else:
            await channel.send(embed=await set_new_table(), view=view)
            await interaction.response.send_message(f"Rules sent to {channel.mention}.", ephemeral=True)
        await view.wait()


def setup(bot: commands.Bot):
    bot.add_cog(NewTable(bot))



