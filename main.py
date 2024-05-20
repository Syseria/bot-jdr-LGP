import config
from dotenv import load_dotenv

import nextcord
from nextcord.ext import commands
import os

load_dotenv()

intents = nextcord.Intents.all()
intents.members = True

bot = commands.Bot(command_prefix='$', intents=intents)


@bot.event
async def on_ready():
    print(f"Bot {bot.user.name} is ready with id ({bot.user.id}).")
    channel = bot.get_channel(config.BASE_CHANNEL)
    await channel.send('Bot is ready.')

# Load Cogs
for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        bot.load_extension(f"cogs.{filename[:-3]}")


'''
Error Handling
'''
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('Command not found!')
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Missing required argument!')
    if isinstance(error, commands.MissingPermissions):
        await ctx.send('Missing permissions!')
    if isinstance(error, commands.BotMissingPermissions):
        await ctx.send('Bot missing permissions!')
    if isinstance(error, commands.NoPrivateMessage):
        await ctx.send('This command cannot be used in private messages.')
    if isinstance(error, commands.MissingRole):
        await ctx.send('Missing role!')
    if isinstance(error, commands.BotMissingRole):
        await ctx.send('Bot missing role!')


bot.run(config.BOT_TOKEN)
