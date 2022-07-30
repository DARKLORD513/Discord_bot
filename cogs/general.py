from os import getenv
import discord
from discord.ext import commands
from dotenv import load_dotenv
import random
import discord.utils
import asyncio
import datetime
import json

class General(commands.Cog):
  def __init__(self, bot):
    self.bot=bot

  @commands.command(help="Sends info about your account or mentioned account", brief="Sends info about your account or mentioned account", aliases=["ui", "whois"])
  async def userinfo(self,ctx,member:discord.Member=None):
      if member==None:
          member=ctx.message.author
      roles = [role for role in member.roles]
      embed_whois = discord.Embed(description=member.mention, color=member.color,)
      embed_whois.set_thumbnail(url=member.display_avatar)
      embed_whois.set_author(icon_url=ctx.author.display_avatar, name=member.name)
      embed_whois.add_field(name="ID", value=member.id, inline=True)
      embed_whois.add_field(name="NICKNAME", value=member.nick, inline=True)
      #embed_whois.add_field(name='AVATAR URL',value=f"[AVATAR URL]({member.display_avatar})",inline=False)
      #embed_whois.add_field(name="ACCOUNT CREATED", value=f"<t:{member.created_at.strftime('%s')}:F>",inline=False)
      embed_whois.add_field(name="JOINED SERVER", value=f"<t:{member.joined_at.strftime('%s')}:F>", inline=False)
      embed_whois.add_field(name="USER STATUS",value=member.status,inline=False)
      embed_whois.add_field(name="FLAGS",value=member.public_flags,inline=False)
      embed_whois.add_field(name="HIGHEST ROLE", value=member.top_role.mention,inline=False)
      embed_whois.add_field(name=f"ROLES  [{len(roles)}]",value=" ".join([role.mention for role in member.roles]),inline=True)
      embed_whois.set_footer(icon_url=ctx.author.display_avatar, text=f"Requested by {ctx.author.name}")
      if member.banner:
          embed_whois.set_image(url=member.banner)
      await ctx.send(embed=embed_whois)


  @commands.command(help="Sends profile pic of mentioned user", brief="Sends profile pic of your account or mentioned account", aliases=["av"])
  async def avatar(self,ctx, member: discord.Member=None):
        if member ==None:
            member = ctx.message.author
        embed_av = discord.Embed(title=member.name,color=member.color,description=f"[AVATAR URL]({member.display_avatar})")
        embed_av.set_footer(text=f"Requested by {ctx.author.name}", icon_url = ctx.author.display_avatar,)
        embed_av.set_image(url=member.display_avatar)
        await ctx.send(embed=embed_av)

  @commands.command(help="Sends the number of members present in the server", brief="Sends the number of members present in the server", aliases=["mc"])
  async def membercount(self,ctx):
        server = ctx.message.guild
        embed_mc = discord.Embed(title=f"Membercount of {server.name}",color= ctx.author.color,timestamp=ctx.message.created_at,)
        embed_mc.set_thumbnail(url=server.icon)
        embed_mc.add_field(name="MEMBERS", value=server.member_count, inline=False)
        await ctx.send(embed=embed_mc)


  @commands.command(pass_context=True, help="Sends various information about the server", brief="Sends various information about the server", aliases=["si"])
  async def serverinfo(self,ctx):
        server=ctx.message.guild
        role_count = len(ctx.guild.roles)
        embed_si = discord.Embed(title=f'Server info of {server.name}',color=discord.Color.random(),)
        embed_si.set_thumbnail(url=server.icon)
        embed_si.add_field(name="SERVER OWNER",value=f"<@{server.owner_id}>`{server.owner_id}`",inline=True)
        embed_si.add_field(name="SERVER ID", value=server.id, inline=True)
        embed_si.set_footer(icon_url=ctx.author.display_avatar, text=f"Requested by {ctx.author.name}")
        embed_si.add_field(name="DESCRIPTION",value=server.description,inline=False)
        #embed_si.add_field(name="CREATED ON",value=f"<t:{server.created_at.strftime('%s')}:F>", inline=False)
        embed_si.add_field(name="SERVER BOOSTS",value=f"Level {server.premium_tier}, Boosts : {server.premium_subscription_count}",inline=False)
        if server.rules_channel:
         embed_si.add_field(name="RULES CHANNELS",value=server.rules_channel.mention,inline=False)
        embed_si.add_field(name="VERIFICATION LEVEL",value=server.verification_level,inline=False)
        embed_si.add_field(name="MEMBERS",value=server.member_count,inline=False)
        embed_si.add_field(name="ROLES",value=role_count,inline=False)
        embed_si.add_field(name="HIGHEST ROLE",value=ctx.guild.roles[-1],inline=False)
        embed_si.add_field(name=f"Channels [{len(server.channels)}]", value=f"Categories [{len(server.categories)}]\n Text Channels [{len(server.text_channels)}]\nVoice Channels  [{len(server.voice_channels)}] \n Threads [{len(server.threads)}]",inline=False)
        if server.banner:
         embed_si.set_image(url=server.banner)
        await ctx.send(embed=embed_si)

  @commands.command(help="Sends information about mentioned role", brief="Sends various information about mentioned role", aliases=["ri"])
  async def roleinfo(self,ctx, role: discord.Role):
        embed_ri = discord.Embed(title=f"{role.name} INFO",color=role.color,timestamp=ctx.message.created_at)
        embed_ri.add_field(name="ROLE ID :", value=f"{role.id}",inline=False)
        #embed_ri.add_field(name="CREATED ON",value=f"<t:{role.created_at.strftime('%s')}:F>", inline=False)
        embed_ri.add_field(name="POSITION", value=role.position,inline=False)
        embed_ri.add_field(name="COLOUR",value=role.colour,inline=False)
        embed_ri.add_field(name="MENTIONABLE",value=role.mentionable,inline=False)
        embed_ri.add_field(name="MANAGED",value=role.managed,inline=False)
        embed_ri.add_field(name="HOISTED",value=role.hoist,inline=False)
        embed_ri.add_field(name="Members", value=f"{len(role.members)}", inline=False)
        embed_ri.add_field(name="Bot Role", value=role.is_bot_managed(), inline=False)
        embed_ri.add_field(name=f"PERMISSIONS",value=role.permissions,inline=False)
        if role.icon:
            embed_ri.set_thumbnail(url=role.icon)
        embed_ri.set_footer(icon_url=ctx.author.display_avatar, text=f"Requested by {ctx.author.name}")
        await ctx.send(embed=embed_ri)
  
  """@commands.command(help="Sends information about the invite of a user", brief="Sends information about the invite of a user")
  async def inviteinfo(self,ctx, invite: discord.Invite):
   emb=discord.Embed(title=f"Invite code info of {invite.code}", color=ctx.author.color, timestamp=ctx.message.created_at,)
   emb.add_field(name="Code", value=invite.code, inline=False)
   emb.add_field(name="Created By", value=f"{invite.inviter.mention} ```{invite.inviter.id}```", inline=False)
   emb.add_field(name="Created At", value=invite.created_at, inline=False)
   emb.add_field(name="Server", value=f"{invite.guild.name} ```{invite.guild.id}```", inline=False)
   emb.add_field(name="Max Age", value=invite.max_age, inline=False)
   emb.add_field(name="Max Usage", value=invite.max_uses, inline=False)
   emb.add_field(name="Uses", value=invite.uses, inline=False)
   emb.add_field(name="Is Temporary", value=invite.temporary, inline=False)
   emb.add_field(name="Channel", value=invite.channel.mention, inline=False)
   emb.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar_url)
   await ctx.send(embed=emb)"""
  

  @commands.command(help="Sends information about the emoji", brief="Sends various information about the emoji", aliases=["ei"])
  async def emojiinfo(self,ctx,emoji: discord.Emoji):
        embed_ei = discord.Embed(title=f"Info about {emoji.name}",color=discord.Colour.random(),timestamp=ctx.message.created_at,)
        embed_ei.add_field(name="EMOJI ID",value=emoji.id,inline=False)
        embed_ei.add_field(name="EMOJI SERVER",value=f"{emoji.guild.name}  `{emoji.guild_id}`",inline=False)
        embed_ei.add_field(name="MANAGED",value=emoji.managed,inline=False)
        #embed_ei.add_field(name="CREATED ON",value=f"<t:{emoji.created_at.strftime('%s')}:F>", inline=False)
        embed_ei.add_field(name="EMOJI URL",value=f"[EMOJI URL]({emoji.url})",inline=False)
        embed_ei.set_thumbnail(url=emoji.url)
        await ctx.send(embed=embed_ei)

    #emoji enlarge
  @commands.command(aliases=['el'])
  async def enlarge(self,ctx,emoji:discord.Emoji):
      await ctx.send(emoji.url)

def setup(bot):
  bot.add_cog(General(bot))