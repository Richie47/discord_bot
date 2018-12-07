import discord
from discord.ext import commands 

bot = commands.Bot(command_prefix=".")


@bot.event
async def on_ready():
    print('User: ')

@bot.command()
async def ping(ctx):
    """See if there's a reason why I'm running slow"""
    await ctx.send(f'Pong! {bot.latency}')

bot.run('bot token here')
