import discord
from discord.ext import commands


bot = commands.Bot(command_prefix="!")

class MembersCog:
    def __init__(self, bot):
        
        self.bot = bot

    @commands.command()
    @commands.guild_only()
    async def joined(self, ctx, *, member: discord.Member):
        """Says when a member joined."""
        if member is None:
            await ctx.send("You haven't specified a member!")

        else:
            await ctx.send(f'{member.display_name} joined on {member.joined_at}')

    @commands.command(name='top_role', aliases=['toprole'])
    @commands.guild_only()
    async def show_toprole(self, ctx, *, member: discord.Member=None):
        """Simple command which shows the members Top Role."""

        if member is None:
            member = ctx.author

        await ctx.send(f'The top role for {member.display_name} is {member.top_role.name}')
    


def setup(bot):
    bot.add_cog(MembersCog(bot))

