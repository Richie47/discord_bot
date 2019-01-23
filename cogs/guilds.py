"""
Anything about server/channel management will go here
"""
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!")

class GuildsCog:
    def __init__(self,bot):
        self.bot = bot

    #TODO: check if a channel already exists
    @bot.command(alaises=['new_channel','createchannel','newchannel'])
    @commands.has_permissions(manage_channels=True)
    @commands.guild_only()
    async def create_channel(ctx, name : str):
        """
        Create a new channel in the server
        """
        if name is None:
            await ctx.send("You haven't specified a channel name.")
        channel = await ctx.guild.create_text_channel(name)

    #eventually convert to cogs.
    @bot.command(alaises=['clr','cls'])
    @commands.has_permissions(manage_channels=True)
    async def clear(ctx, amount : int):
        """Cleans up messages in the channel you call the command in"""
        if amount is None:
            await ctx.channel.purge(limit = 100)
        else:
            await ctx.channel.purge(limit = amount)

        await ctx.send(f'Cleared messages in {ctx.channel}!')
        asyncio.sleep(5)
        await ctx.channel.purge(limit = 1)