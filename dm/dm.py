import asyncio
import discord
from discord.ext import commands

class dmplugin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @checks.has_permissions(PermissionLevel.OWNER)
    @commands.command()
    async def dm(ctx, userid: int,*, dm: str):
       lol = ctx.get_user(userid)
       await lol.send(dm)
       await ctx.send('DM sent!')

    @checks.has_permissions(PermissionLevel.OWNER)
    @commands.command()
    async def spam(ctx, userid: int,*, dm: str):
       while True:
        lol = ctx.get_user(userid)
        await lol.send(dm)
        await ctx.send('DM sent!')
    
def setup(bot):
    bot.add_cog(dmplugin(bot))
