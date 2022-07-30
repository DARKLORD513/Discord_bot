import discord
from discord.ext import commands
import datetime, time, asyncio, humanfriendly

class mute(commands.Cog):
  def __init__(self, bot):
    self.bot=bot


  #mute members
  @commands.command()
  @commands.has_permissions(moderate_members=True)
  @commands.cooldown(1,3,commands.BucketType.member)
  async def mute(self,ctx, member: discord.Member,time="7days",*,reason="No reason provided"):
      time = humanfriendly.parse_timespan(time)
      embed_mute = discord.Embed(description="<:tick_yes:746298071951867906>  " + member.mention + "  has been timed out.. |  "+reason, color=discord.Colour.green())
      embed_mute_no = discord.Embed(description="<a:cross:935620121936937050>" + "You do not have permissions to do that :(",color=discord.Colour.red())
      try :
        await member.timeout(until = discord.utils.utcnow()+ datetime.timedelta(seconds=time),reason=reason)
        await ctx.send(embed=embed_mute)
      except discord.Forbidden:
          await ctx.send(embed=embed_mute_no,delete_after = 4)  

#unmute members
  @commands.command()
  @commands.has_permissions(moderate_members=True)
  async def unmute(self,ctx, member: discord.Member, *, reason="NO reason provided"):
      embed_unmute = discord.Embed(description="<:tick_yes:746298071951867906>  " + f"Timeout has been removed from   {member.mention} | " + reason,color=discord.Colour.green())
      embed_unmute_no = discord.Embed(description="<a:cross:935620121936937050>" + "You do not have permissions to do that :(",color=discord.Colour.red())
      try :
        await member.timeout(until=None,reason=reason)
        await ctx.send(embed=embed_unmute)
      except discord.Forbidden:
        await ctx.send(embed=embed_unmute_no,delete_after = 4)
def setup(bot):
 bot.add_cog(mute(bot))