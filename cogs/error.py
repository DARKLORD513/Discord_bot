from os import getenv
import discord
from discord.ext import commands
from dotenv import load_dotenv
import random
import discord.utils
import asyncio
import datetime
import json
load_dotenv()
#974312785599135744
class error(commands.Cog):

    def __init__(self,bot):
        self.bot= bot
    

    #error management
    @commands.Cog.listener()
    async def on_command_error(self,ctx, error):
        c = self.bot.get_channel(974312792809144322)
        if isinstance(error, commands.MissingPermissions):
            embed_mp = discord.Embed(description="<a:cross:935620121936937050> " + "You do not have permissions to do that :(",color=discord.Colour.red())
            await ctx.send(embed=embed_mp, delete_after=4)
        elif isinstance(error, commands.MissingRequiredArgument):
            embed_mra = discord.Embed(description="<a:cross:935620121936937050> " + "Please provide all the required arguments", color=discord.Colour.red())
            await ctx.send(embed=embed_mra, delete_after=4)
        elif isinstance(error, commands.BadArgument):
            embed_ba = discord.Embed(description="<a:cross:935620121936937050> " + " Please provide the correct arguments", color=discord.Colour.red())
            await ctx.send(embed=embed_ba, delete_after=4)
        elif isinstance(error, commands.MissingAnyRole):
            embed_mp = discord.Embed(description="<a:cross:935620121936937050> " + "You do not have the required roles to do that :(",color=discord.Colour.red())
            await ctx.send(embed=embed_mp, delete_after=4)
        elif isinstance(error, commands.CommandOnCooldown):
            col =f" Please try again after {error.retry_after:.2f}s..."
            await ctx.send(col)
        elif isinstance(error, commands.CheckFailure):
            embed_mp = discord.Embed(description="<a:cross:935620121936937050> " + "You do not have permissions to do that :(",color=discord.Colour.red())
            await ctx.send(embed=embed_mp)
        elif isinstance(error, commands.BotMissingPermissions):
            embed_mp = discord.Embed(description="<a:cross:935620121936937050> " + "I do not have permissions to do that :(",color=discord.Colour.red())
            await ctx.send(embed=embed_mp, delete_after=4)
        elif isinstance(error, commands.NotOwner):
            return
        elif isinstance(error, commands.CommandNotFound):
            return
        else:
            await c.send(f"{error} \n https://discord.com/channels/{ctx.guild.id}/{ctx.channel.id}/{ctx.message.id}")

def setup(bot):
  bot.add_cog(error(bot))