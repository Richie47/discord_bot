import discord 
import requests
import sys
import traceback
import time
from discord.ext import commands

bot = commands.Bot(command_prefix="!")

extensions = ['cogs.members', 'cogs.fun', 'cogs.guilds', 'cogs.music']

if __name__ == '__main__':
    for extension in extensions:
        try:
            bot.load_extension(extension)
            print(f'{extension} loaded!')
        except Exception as e:
            print(f'Warning: failed to load extension {extension}.', file = sys.stderr)
            traceback.print_exc()

@bot.event
async def on_ready():
    print(f'Logged in as: {bot.user.name}')
    print(f'ID: {bot.user.id}')
    print(f'Version {discord.__version__}')
    await bot.change_presence(activity = discord.Streaming(name='Making a music bot!', url='https://www.twitch.tv/twitchpresents', type = 1))




@bot.event
async def on_command_error(ctx, error):
    """The event triggered when an error is raised while invoking a command.
    ctx   : Context
    error : Exception"""

    print(error)
    if hasattr(error, 'NameError'):
        await ctx.send('Name is not defined, try again.')
        print('nameError occured')

    await ctx.send('Did you really think I would let you do that? :thinking:')



@bot.command()
async def ping(ctx):
    """See if there's a reason why I'm running slow"""
    await ctx.send(f'Pong! {round(bot.latency, 2)}s response time.')


#TODO: Make a clear messages cmd, create channels/channel management, mute/ban/deaf members

@bot.command()
async def roles(ctx):
    await ctx.send(f' {ctx.guild.roles} ')


@bot.command()
async def dm(ctx, member : discord.Member, msg : str):
    if member is None:
        await ctx.send("You didn't specify a member!")

    elif msg is None:
        await ctx.send("You didn't supply a message to send!")
    
    else:
        await member.send(msg)   

bot.run('NDgzMTI1NDcyNzgwMjIyNDk1.DypJFg.XJKogfY77Yr4jP4xj8tn5Kwr6nU', bot=True, reconnect=True)
