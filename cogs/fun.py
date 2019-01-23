"""
Several miscellanious commands below, most will be free to use by all users as they are harmless
fun commands
"""

import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!")

class FunCog:
    def __init__(self,bot):
        self.bot = bot

    @bot.command(alaises=['bc', 'bit'])
    async def bitcoin(ctx):
        """See the live time value of BitCoin!"""
        url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
        response = requests.get(url)
        value = response.json()['bpi']['USD']['rate']
        await ctx.send(f'Bitcoin price is currently ${value}')

    @commands.command(name='embeds')
    @commands.guild_only()
    async def example_embed(self, ctx):
        """A simple command which showcases the use of embeds.
        Have a play around and visit the Visualizer."""

        embed = discord.Embed(title='Example Embed',
                              description='Showcasing the use of Embeds...\nSee the visualizer for more info.',
                              colour=0x98FB98)
        embed.set_author(name='MysterialPy',
                         url='https://gist.github.com/MysterialPy/public',
                         icon_url='http://i.imgur.com/ko5A30P.png')
        embed.set_image(url='https://cdn.discordapp.com/attachments/84319995256905728/252292324967710721/embed.png')

        embed.add_field(name='Embed Visualizer', value='[Click Here!](https://leovoel.github.io/embed-visualizer/)')
        embed.add_field(name='Command Invoker', value=ctx.author.mention)
        embed.set_footer(text='Made in Python with discord.py@rewrite', icon_url='http://i.imgur.com/5BFecvA.png')

        await ctx.send(content='**A simple Embed for discord.py@rewrite in cogs.**', embed=embed)


def setup(bot):
    bot.add_cog(FunCog(bot))