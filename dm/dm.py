import asyncio
import discord
from discord.ext import commands

from core import checks
from core.models import PermissionLevel

class dmplugin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @checks.has_permissions(PermissionLevel.OWNER)
    @commands.command()
    async def dm(ctx, bot, userid: int,*, dm: str):
       lol = bot.get_user(userid)
       await lol.send(dm)
       await ctx.send('DM sent!')

    @checks.has_permissions(PermissionLevel.OWNER)
    @commands.command()
    async def spam(ctx, bot, userid: int,*, dm: str):
       while True:
        lol = bot.get_user(userid)
        await lol.send(dm)
        await ctx.send('DM sent!')
    
def setup(bot):
    bot.add_cog(dmplugin(bot))
