import asyncio
import discord
from discord.ext import commands

class DmPlugin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

@commands.Cog.listener()
async def dm(ctx, userid: int,*, dm: str):
    boi = bot.get_user(userid)
    await boi.send(dm)
    await ctx.send('DM sent!')

@commands.Cog.listener()
async def spam(ctx, userid: int,*, dm: str):
    while True:
        boi = bot.get_user(userid)
        await boi.send(dm)
        await ctx.send('DM sent!')
    
def setup(bot):
    bot.add_cog(DmPlugin(bot))
