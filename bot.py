import discord 
import requests
from discord.ext import commands 

bot = commands.Bot(command_prefix="!")


@bot.event
async def on_ready():
    print(f'Logged in as: {bot.user.name}')
    print(f'ID: {bot.user.id}')
    game = discord.Game('without 2 monitors Þ:')
    await bot.change_presence(status=discord.Status.dnd, activity=game)

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
async def roles(ctx):
    await ctx.send(f' {ctx.guild.roles} ')


@bot.command()
@commands.has_role('Role-Test')
async def kick_user(ctx, member: discord.Member):
    await member.kick() 


@bot.command()
@commands.has_role('Role-Test')
async def kick1(ctx, member : discord.Member, *, reason : str):
    await ctx.guild.kick(member)
    await member.send(reason)
   

@bot.command()
async def dm(ctx, member : discord.Member, msg : str):
    await member.send(msg)    



bot.run('')
