import discord 
import requests
import sys
import traceback
import time
from discord.ext import commands

bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print(f'Logged in as: {bot.user.name}')
    print(f'ID: {bot.user.id}')
    game = discord.Game('without a and ! :/ broke my keyboard kinda')
    await bot.change_presence(status=discord.Status.dnd, activity=game)


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
async def bitcoin(ctx):
    url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
    response = requests.get(url)
    value = response.json()['bpi']['USD']['rate']
    await ctx.send(f'Bitcoin price is currently ${value}')

@bot.command()
async def ping(ctx):
    """See if there's a reason why I'm running slow"""
    await ctx.send(f'Pong! {round(bot.latency, 2)}s response time.')

@bot.command()
@commands.has_permissions(manage_messages=True)
async def test(ctx, mem:discord.Member):
    await ctx.send(f'{type(mem.roles)}')


#TODO: Make a clear messages cmd, create channels/channel management, mute/ban/deaf members

@bot.command()
@commands.has_permissions(manage_channels=True)
async def create_channel(ctx, name : str):
    """
    Create a new channel in the server
    """
    channel = await ctx.guild.create_text_channel(name)

#eventually convert to cogs.
@bot.command()
@commands.has_permissions(manage_channels=True)
async def clear(ctx, amount : int):
    await ctx.channel.purge(limit = amount)
    await ctx.send(f'Cleared messages in {ctx.channel}!')
    time.sleep(5)
    await ctx.channel.purge(limit = 1)

@bot.command(aliases=['promote'])
@commands.has_permissions(manage_roles=True)
@commands.guild_only() # Rewrite Only: Command cannot be used in private messages. (Replaces no_pm=True)
async def addrole(ctx, mem: discord.Member, ro: discord.Role):
    await ctx.send(mem.roles)
    await ctx.send(ctx.guild.roles)

    """Grant a role to a member"""
    if mem and ro:
        if ro is None:
            return await ctx.send("You haven't specified a role!")
        
        elif ro not in ctx.guild.roles:
            return await ctx.send('This role does not exist!')

        elif ro not in mem.roles:
            await mem.add_roles(ro)
            await ctx.send(f'{ro} has been added to user {mem}!')

        else:
            print('Something happened that should not of happened (promoting a user)')

@bot.command(aliases=['demote'])
@commands.has_permissions(manage_roles=True)
@commands.guild_only()
async def remove_role(ctx, mem: discord.Member, ro: discord.Role):
    if mem and ro:
        if ro is None:
            return await ctx.send("You haven't specified a role!")

        elif ro not in ctx.guild.roles:
            return await ctx.send('This role does not exist!')

        elif ro not in mem.roles:
            return await ctx.send(f'{mem} does not have the role {ro}.')

        elif ro in mem.roles:
            await mem.remove_roles(ro)
            await ctx.send(f'{ro} has been removed from {mem} :flushed:')

        else:
            print('Something happened that should not of happened. (demoting a user)')

@bot.command()
async def roles(ctx):
    await ctx.send(f' {ctx.guild.roles} ')


@bot.command()
@commands.has_role('Role-Test')
async def kick_user(ctx, member: discord.Member):
    await member.kick() 



#bot and user needs permissions
@bot.command()
@commands.has_permissions(ban_members =  False)
@commands.bot_has_permissions(ban_members = False)
async def kick1(ctx, member : discord.Member, *, reason : str):


    await ctx.guild.kick(member)
    await member.send(reason)
   
@bot.command()
async def dm(ctx, member : discord.Member, msg : str):
    await member.send(msg)    



bot.run('')
