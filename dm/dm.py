import asyncio
import discord
from discord.ext import commands

class dmplugin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        bot = lol
    
    @commands.command()
    async def dm(ctx, userid: int,*, dm: str):
       lol = bot.get_user(userid)
       await lol.send(dm)
       await ctx.send('DM sent!')

    @commands.command()
    async def spam(ctx, userid: int,*, dm: str):
       while True:
        lol = bot.get_user(userid)
        await lol.send(dm)
        await ctx.send('DM sent!')
    
def setup(bot):
    bot.add_cog(dmplugin(bot))
