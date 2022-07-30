import discord
from discord.ext import commands
import json, requests, asyncio
from discord.ext.commands import MissingPermissions
cross = "<a:cross:935620121936937050>"
tick = "<:tick_yes:746298071951867906>"
info = "<a:info:936164908188446780>"

class Moderator(commands.Cog):
  def __init__(self, bot):
    self.bot=bot


  @commands.command(pass_context=True, help="Deletes specified role", brief="Deletes specified role")
  @commands.has_permissions(manage_roles=True)
  async def deleterole(self,ctx, role: discord.Role):
        embed_del = discord.Embed(description=f"{tick} **{role.name}** has been deleted !", color = discord.Colour.random())
        embed_del_1 = discord.Embed(description=f"{cross} You do not have the permissions to do that :(", color=discord.Colour.random())
        embed_del_2 = discord.Embed(description=f"{info} Does that role even exist ? lmao",color=discord.Colour.random())
        if role:
            try:
                await role.delete()
                await ctx.send(embed=embed_del)
            except discord.Forbidden:
                await ctx.send(embed=embed_del_1)
        else:
            await ctx.send(embed=embed_del_2)

  @commands.command(pass_context=True, help='Gives role to mentioned user or users', brief='Gives role to mentioned user or users', aliases=['mr','massrole'])
  @commands.has_permissions(manage_roles=True)
  async def mass_role(self,ctx, role:discord.Role,members:commands.Greedy[discord.Member]):
        embed_role = discord.Embed(description=f"{tick} {role} is given to the mentioned user(s)",color=discord.Colour.random())
        embed_role_no = discord.Embed(description=f"{cross}  you do not have permissions to do that :(",color=discord.Colour.red())
        try:
            for roles in members:
                await roles.add_roles(role)
                await asyncio.sleep(0)
            await ctx.send(embed=embed_role)
        except discord.Forbidden:
            await ctx.send(embed=embed_role_no)

  @commands.command(pass_context=True, help='Removes role from mentioned user or users', brief='Removes role from mentioned user or users', aliases=['rm'])
  @commands.has_permissions(manage_roles=True)
  async def removerole(self,ctx, role:discord.Role,members:commands.Greedy[discord.Member]):
        embed_rr = discord.Embed(description=f"{tick} {role} is removed from mentioned users",color=discord.Colour.green())
        embed_rr_no = discord.Embed(description=f"{cross}  you do not have permissions to do that :(",color=discord.Colour.red())
        try:
            for roles in members:
                await roles.remove_roles(role)
                await asyncio.sleep(0)
            await ctx.send(embed=embed_rr)
        except discord.Forbidden:
            await ctx.send(embed=embed_rr_no)


  @commands.command(pass_context=True, help="Deletes specified number of messages from the channel", brief="Deletes specified number of messages from the channel")
  @commands.has_permissions(manage_messages=True)
  async def purge(self,ctx,  amount=1,):
          check_func = lambda msg: not msg.pinned
          await ctx.channel.purge(limit=amount+1,check= check_func)
          embed_purge = discord.Embed(description=tick + f" {ctx.author.mention} purged {amount} messages", color=discord.Colour.green())
          embed_purge_1 = discord.Embed(description=tick + f" {ctx.author.mention} purged {amount} message",color=discord.Colour.green())
          if amount > 1.1:
            await ctx.send(embed=embed_purge, delete_after=3)
          else:
            await ctx.send(embed=embed_purge_1, delete_after=3)

  """@commands.command(help='Locks current channel', brief='Locks current channel')
  @commands.has_permissions(manage_channels=True)
  async def lock(self,ctx):
   cross = "<:no:933679544861327372>"
   warn = "<a:bot_warn:933020574052126790>"
   tick = "<:yes:933679493342699611>"
   try:
     await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False)
     emb=discord.Embed(description=(f'{tick} LOCKED **{ctx.channel}**.'), color=discord.Color.green())
     await ctx.send(embed=emb)
   except discord.Forbidden:
     emb1=discord.Embed(description=(f'{cross} MISSING PERMISSIONS TO LOCK THIS CHANNEL'), color=discord.Color.red())
     await ctx.send(embed=emb1)"""

  """@commands.command(help='Unlocks current channel', brief='Unlocks current channel')
  @commands.has_permissions(manage_channels=True)
  async def unlock(self,ctx):
   cross = "<:no:933679544861327372>"
   warn = "<a:bot_warn:933020574052126790>"
   tick = "<:yes:933679493342699611>"
   try:
     await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True)
     emb=discord.Embed(description=(f'{tick} UNLOCKED **{ctx.channel}**.'), color=discord.Color.green())
     await ctx.send(embed=emb)
   except discord.Forbidden:
     emb1=discord.Embed(description=(f'{cross} MISSING PERMISSIONS TO UNLOCK THIS CHANNEL'), color=discord.Color.red())
     await ctx.send(embed=emb1)"""

  @commands.command(pass_context=True, help='Kicks mentioned user', brief='Kicks mentioned user')
  @commands.has_permissions(kick_members=True)
  async def kick(self,ctx, member: discord.Member, *, reason="NO reason provided"):
        embed_kick = discord.Embed(description="<:tick_yes:746298071951867906>  "+member.name + f"  Has been kicked from {ctx.message.guild.name} , " + reason,color=discord.Colour.green())
        embed_self = discord.Embed(description="<a:cross:935620121936937050>" + "  You cannot do that :(",color=discord.Colour.red())
        if ctx.author == member : 
          await ctx.send(embed=embed_self)
          return False
        try:
            await member.kick(reason=reason)
            await ctx.send(embed=embed_kick)
        except discord.Forbidden:
            embed_cir = discord.Embed(description="<a:cross:935620121936937050>" + "You do not have permissions to do that :(",color=discord.Colour.red())
            await ctx.send(embed=embed_cir,delete_after=3)


  @commands.command(pass_context=True, help='Bans mentioned user', brief='Bans mentioned user')
  @commands.has_permissions(ban_members=True)
  async def ban(self,ctx, member: discord.Member, *, reason="NO reason provided"):
        embed_ban = discord.Embed(description="<:tick_yes:746298071951867906> " + member.name + f"  has been banned from {ctx.message.guild.name} , " + reason,color=discord.Colour.green())
        embed_self = discord.Embed(description="<a:cross:935620121936937050>" + "  You cannot do that :(",color=discord.Colour.red())
        if ctx.author == member : 
          await ctx.send(embed=embed_self)
          return False
        try:
            await member.ban(reason=reason)
            await ctx.send(embed=embed_ban)
        except discord.Forbidden:
            embed_ban_cir = discord.Embed(description="<a:cross:935620121936937050>" + "You do not have permissions to do that :(",color=discord.Colour.red())
            await ctx.send(embed=embed_ban_cir, delete_after=3)



  @commands.command(help="Unbans specified user", brief="Unbans specified user (by discriminator)")
  @commands.has_permissions(ban_members = True)
  async def unban(self,ctx, *,id:int):
      if len(str(id)) == 18:
        try:
         user = await self.bot.fetch_user(id)
         embed_unban = discord.Embed(description=f"<:tick_yes:746298071951867906>  **{user.name}**   has been unbanned from {ctx.message.guild.name}",color=discord.Colour.green())
         await ctx.guild.unban(user)
         await ctx.send(embed=embed_unban)
        except discord.HTTPException:
          emb = discord.Embed(description=f"<a:cross:935620121936937050>  **{user.name}** is not banned... ",color=discord.Colour.red())
          await ctx.send(embed=emb,delete_after=3)
      else:
        embed_unban_cir = discord.Embed(description=f"<a:cross:935620121936937050> Please provide a valid id... ",color=discord.Colour.red())
        await ctx.send(embed=embed_unban_cir,delete_after=3)



  @commands.command(help="Creates a role", brief="Creates a role", aliases=["addrole", "create_role"])
  @commands.has_permissions(manage_roles = True)
  async def createrole(self,ctx,*,name ,hoisted=False,mention=False):
        embed_ar = discord.Embed(description=f"{tick}  **{name}** HAS BEEN  CREATED",color=discord.Colour.random())
        guild = ctx.guild
        await guild.create_role(name= f"{name}",hoist=hoisted,mentionable=mention)
        await ctx.send(embed=embed_ar)

def setup(bot):
  bot.add_cog(Moderator(bot))