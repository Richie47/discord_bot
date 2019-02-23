"""
Several miscellanious commands below, most will be free to use by all users as they are harmless
fun commands
"""

import discord
from random import *
import requests
import json
from discord.ext import commands
import random

bot = commands.Bot(command_prefix="!")

class FunCog:
    def __init__(self,bot):
        self.bot = bot

    @bot.command(alaises=['bc', 'bit'])
    async def bitcoin(self,ctx):
        """See the live time value of BitCoin!"""
        url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
        response = requests.get(url)
        value = response.json()['bpi']['USD']['rate']
        await ctx.send(f'Bitcoin price is currently ${value}')

    @bot.command(alaises= ['meme', 'greentext', 'anon'])
    @commands.guild_only()
    async def meme(self, ctx):
        """A simple command which showcases the use of embeds.
        Have a play around and visit the Visualizer."""

        subreddits = ['dankmemes', 'memes', 'blackpeopletwitter','195', 'whitepeopletwitter', 'funny', 'bettereveryloop'
        , 'facepalm', 'oldpeoplefacebook', 'insanepeoplefacebook', 'woahdude']
        # TODO: figure out how to deal with .gif or gfycat links and see if theyre even possible to use.
        url = f'http://reddit.com/r/{subreddits[random.randint(0, len(subreddits) - 1)]}/random.json'
        response = requests.get(url, headers = {'User-agent': 'bender'}) #https://www.reddit.com/r/nba/robots.txt for why I chose bender

        title = response.json()[0]['data']["children"][0]["data"]["title"]
        url = response.json()[0]['data']['children'][0]['data']['url']


        print(title)
        print(url)

        x = randint(0,499)
        embed = discord.Embed(title=f'{title}',
                              description='I just want this finished',
                              colour=0x98FB98)
        embed.set_author(name='Anon',
                         url=f'https://gist.github.com/MysterialPy/public',
                         icon_url='http://i.imgur.com/ko5A30P.png')
        embed.set_image(url=f'{url}')

        embed.add_field(name='Embed Visualizer', value='[Click Here!](https://leovoel.github.io/embed-visualizer/)')
        embed.add_field(name='Command Invoker', value=ctx.author.mention)
        embed.set_footer(text='Made in Python with discord.py@rewrite', icon_url='http://i.imgur.com/5BFecvA.png')

        await ctx.send(content='**A simple Embed for discord.py@rewrite in cogs.**', embed=embed)


def setup(bot):
    bot.add_cog(FunCog(bot))

