#no pycord here
import discord
from discord.ext import commands
from discord.ext.commands import MissingPermissions
import random, datetime, time
import asyncio
import json
from os import getenv
from dotenv import load_dotenv
import os
import requests


load_dotenv()

invite_link = "https://discord.com/api/oauth2/authorize?client_id=975053562566557836&permissions=8&scope=bot%20applications.commands"
cross = "<a:cross:935620121936937050>"
tick = "<:tick_yes:746298071951867906>"
info = "<a:info:936164908188446780>"
warn = "<a:bot_warn:933020574052126790>"
started = time.time()


async def getPrefix(client, msg):
  owner = await client.is_owner(msg.author)
  if owner:
    return commands.when_mentioned_or("!", "")(client, msg)
  else:
    return commands.when_mentioned_or("!")(client, msg)

bot = commands.Bot(command_prefix=getPrefix,
                   intents=discord.Intents.all(),case_insensitive=True,
                   owner_ids={853550854162743296})
bot.remove_command('help')


@bot.event
async def on_ready():
    print("logged in as {0.user}".format(bot))
    await bot.change_presence(activity=discord.Activity(
        type=discord.ActivityType.watching, name=f"!help"))


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')


def owner(ctx):
    if ctx.author.id == 853550854162743296:
      return True

@bot.command()
@commands.check(owner)
async def reload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')
    bot.load_extension(f'cogs.{extension}')
    await ctx.send(f'Reloaded {extension}')


@bot.command()
@commands.check(owner)
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}')
    await ctx.send(f'Loaded {extension}')


@bot.command()
@commands.check(owner)
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')
    await ctx.send(f'Unoaded {extension}')

@bot.command()
@commands.check(owner)
async def guilds(ctx):
  guilds=bot.guilds
  a=[]
  for i in guilds:
    a.append(f"{i.name} : {i.member_count}")
  await ctx.send(a)

  
@bot.group(invoke_without_command=True)
async def help(ctx):
    emb = discord.Embed(
        title="DARKLØRÐ HELP",
        color=discord.Color.gold(),
        timestamp=ctx.message.created_at,
    )
    emb.add_field(name="Bot",
                  value="```ping, prefix, invite, botinfo,```",
                  inline=False)
    emb.add_field(
        name="General",
        value=
        "```avatar, userinfo, serverinfo, emojiinfo, membercount```",
        inline=False)
    emb.add_field(
        name="Moderation",
        value=
        "```purge, kick, ban, unban, massrole, removerole, addrole, delrole, mute, unmute```",
        inline=False)
    emb.add_field(name="Miscellaneous",
                  value="```joke, meme, quote, weather, gif```",
                  inline=False)
    emb.add_field(name="Links",
                  value=f"[Invite Me](https://discord.com/api/oauth2/authorize?client_id=975053562566557836&permissions=8&scope=bot%20applications.commands)\n",
                  inline=False)
    emb.set_footer(text=f"Use help <command> for more info on that command.",
                   icon_url=bot.user.display_avatar)
    emb.set_thumbnail(url=bot.user.display_avatar)
    await ctx.send(embed=emb)


@help.command()
async def ping(ctx):
    em = discord.Embed(
        title="Ping",
        color=discord.Color.gold(),
        timestamp=ctx.message.created_at,
    )
    em.add_field(name="Description",
                 value="Returns bot latency/ping",
                 inline=False)
    em.add_field(name="**Syntax**", value="```!ping```", inline=False)
    await ctx.send(embed=em)


@help.command()
async def prefix(ctx):
    em = discord.Embed(
        title="Prefix",
        color=discord.Color.gold(),
        timestamp=ctx.message.created_at,
    )
    em.add_field(name="Description",
                 value="Returns the prefix of bot",
                 inline=False)
    em.add_field(name="**Syntax**",
                 value="```@DARKLØRÐ prefix```",
                 inline=False)
    await ctx.send(embed=em)


@help.command()
async def invite(ctx):
    em = discord.Embed(
        title="Invite",
        color=discord.Color.gold(),
        timestamp=ctx.message.created_at,
    )
    em.add_field(name="Description",
                 value="Generates invite link of the bot",
                 inline=False)
    em.add_field(name="**Syntax**", value="```!invite```", inline=False)
    await ctx.send(embed=em)


@help.command()
async def botinfo(ctx):
    em = discord.Embed(
        title="Bot Info",
        color=discord.Color.gold(),
        timestamp=ctx.message.created_at,
    )
    em.add_field(name="Description",
                 value="Sends various information about the bot",
                 inline=False)
    em.add_field(name="**Syntax**", value="```!botinfo```", inline=False)
    await ctx.send(embed=em)


@help.command(aliases=["av"])
async def avatar(ctx):
    em = discord.Embed(
        title="Avatar",
        color=discord.Color.gold(),
        timestamp=ctx.message.created_at,
    )
    em.add_field(name="Description",
                 value="Sends the profile picture of the user if mentioned",
                 inline=False)
    em.add_field(name="Aliases", value="av",
                 inline=False).add_field(name="**Syntax**",
                                         value="```!avatar [user]```",
                                         inline=False)
    em.add_field(name="Example", value="!avatar @DARKLØRÐ#1007", inline=False)
    await ctx.send(embed=em)


@help.command(aliases=["ui", "whois"])
async def userinfo(ctx):
    em = discord.Embed(
        title="User Info",
        color=discord.Color.gold(),
        timestamp=ctx.message.created_at,
    )
    em.add_field(name="Description",
                 value="Sends various information about the user if mentioned",
                 inline=False)
    em.add_field(name="Aliases", value="ui", inline=False)
    em.add_field(name="**Syntax**",
                 value="```!userinfo [user]```",
                 inline=False)
    em.add_field(name="Example", value="!ui @DARKLØRÐ#1201", inline=False)
    await ctx.send(embed=em)


@help.command(aliases=["si"])
async def serverinfo(ctx):
    em = discord.Embed(
        title="Server Info",
        color=discord.Color.gold(),
        timestamp=ctx.message.created_at,
    )
    em.add_field(name="Description",
                 value="Sends information about the server",
                 inline=False)
    em.add_field(name="Aliases", value="si", inline=False)
    em.add_field(name="**Syntax**", value="```!serverinfo```", inline=False)
    await ctx.send(embed=em)


@help.command(aliases=["ei"])
async def emojiinfo(ctx):
    em = discord.Embed(
        title="Emoji Info",
        color=discord.Color.gold(),
        timestamp=ctx.message.created_at,
    )
    em.add_field(name="Description",
                 value="Sends information about the emoji",
                 inline=False)
    em.add_field(name="Aliases", value="ei", inline=False)
    em.add_field(name="**Syntax**",
                 value="```!emojiinfo <emoji>```",
                 inline=False)
    em.add_field(name="Example", value="!ei :DARKLØRÐ:", inline=False)
    await ctx.send(embed=em)


@help.command(aliases=["mc"])
async def membercount(ctx):
    em = discord.Embed(
        title="Member Count",
        color=discord.Color.gold(),
        timestamp=ctx.message.created_at,
    )
    em.add_field(name="Description",
                 value="Returns the number of members in the server",
                 inline=False)
    em.add_field(name="Aliases", value="mc", inline=False)
    em.add_field(name="**Syntax**", value="```!membercount```", inline=False)
    await ctx.send(embed=em)


@help.command()
async def purge(ctx):
    em = discord.Embed(
        title="Purge",
        color=discord.Color.gold(),
        timestamp=ctx.message.created_at,
    )
    em.add_field(name="Description",
                 value="Deletes specified number of messages from the channel",
                 inline=False)
    em.add_field(name="**Syntax**",
                 value="```!purge <amount>```",
                 inline=False)
    em.add_field(name="Example", value="!purge 69", inline=False)
    await ctx.send(embed=em)


@help.command()
async def kick(ctx):
    em = discord.Embed(
        title="Kick",
        color=discord.Color.gold(),
        timestamp=ctx.message.created_at,
    )
    em.add_field(name="Description",
                 value="Kicks mentioned user from the server",
                 inline=False)
    em.add_field(name="**Syntax**",
                 value="```!kick <user> [reason]```",
                 inline=False)
    em.add_field(name="Example",
                 value="!kick @DARKLØRÐ#2441 sending msg",
                 inline=False)
    await ctx.send(embed=em)


@help.command()
async def ban(ctx):
    em = discord.Embed(
        title="Ban",
        color=discord.Color.gold(),
        timestamp=ctx.message.created_at,
    )
    em.add_field(name="Description",
                 value="Bans user from the server",
                 inline=False)
    em.add_field(name="**Syntax**",
                 value="```!ban <user> [reason]```",
                 inline=False)
    em.add_field(name="Example",
                 value="!ban @DARKLØRÐ#1234 spamming",
                 inline=False)
    await ctx.send(embed=em)


@help.command()
async def unban(ctx):
    em = discord.Embed(
        title="Unban",
        color=discord.Color.gold(),
        timestamp=ctx.message.created_at,
    )
    em.add_field(name="Description",
                 value="Unbans user from the server by user's discriminator",
                 inline=False)
    em.add_field(name="**Syntax**", value="```!unban <user id>```", inline=False)
    em.add_field(name="Example", value="!unban 975053562566557836", inline=False)
    await ctx.send(embed=em)

@help.command(aliases=["mr", "mass_role"])
async def massrole(ctx):
    em = discord.Embed(
        title="Mass Role",
        color=discord.Color.gold(),
        timestamp=ctx.message.created_at,
    )
    em.add_field(name="Description",
                 value="Gives role to mentioned user",
                 inline=False)
    em.add_field(name="Aliases", value="mr, mass_role", inline=False)
    em.add_field(name="**Syntax**",
                 value="```!massrole <role> <members>```",
                 inline=False)
    em.add_field(name="Example",
                 value="!massrole @test @DARKLØRÐ#1234",
                 inline=False)
    await ctx.send(embed=em)


@help.command(aliases=["rm", "remove_role"])
async def removerole(ctx):
    em = discord.Embed(
        title="Remove Role",
        color=discord.Color.gold(),
        timestamp=ctx.message.created_at,
    )
    em.add_field(name="Description",
                 value="Removes role from mentioned user",
                 inline=False)
    em.add_field(name="Aliases", value="rm, remove_role", inline=False)
    em.add_field(name="**Syntax**",
                 value="```!removerole <role> <members>```",
                 inline=False)
    em.add_field(name="Example",
                 value="!removerole @test @DARKLØRÐ#1234",
                 inline=False)
    await ctx.send(embed=em)


@help.command(aliases=["createrole", "create_role"])
async def addrole(ctx):
    em = discord.Embed(
        title="Add Role",
        color=discord.Color.gold(),
        timestamp=ctx.message.created_at,
    )
    em.add_field(name="Description", value="Creates a role", inline=False)
    em.add_field(name="Aliases", value="createrole, create_role", inline=False)
    em.add_field(name="**Syntax**",
                 value="```!addrole <role>```",
                 inline=False)
    em.add_field(name="Example", value="!addrole test role", inline=False)
    await ctx.send(embed=em)


@help.command()
async def delrole(ctx):
    em = discord.Embed(
        title="Delete Role",
        color=discord.Color.gold(),
        timestamp=ctx.message.created_at,
    )
    em.add_field(name="Description",
                 value="Deletes mentioned role",
                 inline=False)
    em.add_field(name="**Syntax**",
                 value="```!delrole <role>```",
                 inline=False)
    em.add_field(name="Example", value="!delrole @test", inline=False)
    await ctx.send(embed=em)


@help.command()
async def joke(ctx):
    em = discord.Embed(
        title="Joke",
        color=discord.Color.gold(),
        timestamp=ctx.message.created_at,
    )
    em.add_field(name="Description", value="Sends random joke", inline=False)
    em.add_field(name="**Syntax**", value="```!joke```", inline=False)
    await ctx.send(embed=em)


@help.command()
async def meme(ctx):
    em = discord.Embed(
        title="Meme",
        color=discord.Color.gold(),
        timestamp=ctx.message.created_at,
    )
    em.add_field(name="Description", value="Sends random meme", inline=False)
    em.add_field(name="**Syntax**", value="```!meme```", inline=False)
    await ctx.send(embed=em)


@help.command()
async def quote(ctx):
    em = discord.Embed(
        title="Quote",
        color=discord.Color.gold(),
        timestamp=ctx.message.created_at,
    )
    em.add_field(name="Description",
                 value="Sends random inspiring quote",
                 inline=False)
    em.add_field(name="**Syntax**", value="```!quote```", inline=False)
    await ctx.send(embed=em)


@help.command()
async def weather(ctx):
    em = discord.Embed(
        title="Weather",
        color=discord.Color.gold(),
        timestamp=ctx.message.created_at,
    )
    em.add_field(name="Description",
                 value="Displays weather information of a place",
                 inline=False)
    em.add_field(name="Syntax", value="```!weather <place>```", inline=False)
    em.add_field(name="Example", value="!weather Mumbai", inline=False)
    await ctx.send(embed=em)

@help.command()
async def vote(ctx):
  em=discord.Embed(title="Vote", color=discord.Color.gold(), timestamp=ctx.message.created_at,)
  em.add_field(name="Description", value="Sends vote link for the bot", inline=False)
  em.add_field(name="Syntax", value="```!vote```", inline=False)
  await ctx.send(embed=em)


@help.command()
async def gif(ctx):
    em = discord.Embed(
        title="Gif",
        color=discord.Color.gold(),
        timestamp=ctx.message.created_at,
    )
    em.add_field(name="Description",
                 value="Sends gif by searching a keyword",
                 inline=False)
    em.add_field(name="**Syntax**", value="```!gif <search term>```", inline=False)
    em.add_field(name="Example", value="!gif cheems", inline=False)
    await ctx.send(embed=em)

@help.command()
async def mute(ctx):
    em = discord.Embed(
        title="Mute",
        color=discord.Color.gold(),
        timestamp=ctx.message.created_at,
    )
    em.add_field(name="Description",
                 value="Mutes mentioned user",
                 inline=False)
    em.add_field(name="**Syntax**", value="```!mute <user> <time> [reason]```", inline=False)
    em.add_field(name="Example", value="!mute @DARKLØRÐ#1234 5m Spamming", inline=False)
    await ctx.send(embed=em)


@help.command()
async def unmute(ctx):
    em = discord.Embed(
        title="Unmute",       color=discord.Color.gold(),
        timestamp=ctx.message.created_at,
    )
    em.add_field(name="Description",
                 value="Unmutes mentioned user",
                 inline=False)
    em.add_field(name="**Syntax**", value="```!unmute <user> [reason]```", inline=False)
    em.add_field(name="Example", value="!unmute @DARKLØRÐ#2441",inline=False)
    await ctx.send(embed=em)

api="83TTL3RYS8U5"
lmt=1
def getgif(search_term):
  r = requests.get(
    "https://g.tenor.com/v1/search?q=%s&key=%s&limit=%s" % (search_term, api, lmt))
  if r.status_code == 200:
    top_8gifs = json.loads(r.content)
    url = top_8gifs['results'][0]['media'][0]['gif']['url']
    return url
  else:
    top_8gifs = None
@bot.command()
@commands.has_permissions(embed_links=True)
async def gif(ctx,*,term):
  gif = getgif(term)
  await ctx.send(gif)


@bot.command()
@commands.is_owner()
async def ver(ctx):
      await ctx.send(discord.__version__)

bot.load_extension("jishaku")
bot.run(getenv('TOKEN'))
