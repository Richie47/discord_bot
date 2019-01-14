import discord 
import requests
import sys
import traceback
from discord.ext import commands

bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print(f'Logged in as: {bot.user.name}')
    print(f'ID: {bot.user.id}')
    game = discord.Game('without 2 monitors Þ:')
    await bot.change_presence(status=discord.Status.dnd, activity=game)

@bot.event
async def on_command_error(ctx, error):
    """The event triggered when an error is raised while invoking a command.
    ctx   : Context
    error : Exception"""

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
async def test(ctx):
    await ctx.send('You can manage messages.')

@bot.command(aliases=['Addrole'])
@commands.has_permissions(manage_roles=True)
@commands.guild_only() # Rewrite Only: Command cannot be used in private messages. (Replaces no_pm=True)
async def addrole(ctx, mem: str, ro: str):
    """Grant a role to a member"""
    member = getUser(ctx, mem)
    role = getRole(ctx, ro)
    if member and role:
        if role not in member.roles:
            roles = member.roles
            roles.append(role)
            await member.edit(roles=roles)

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
