import discord
from discord.ext import commands
import datetime, time, asyncio
dark = "<a:dark:957357794296737853>"
url="https://discord.com/api/oauth2/authorize?client_id=904285165675749426&permissions=1101927671894&scope=bot"

class Bot(commands.Cog):
  def __init__(self, bot):
    self.bot=bot
    self.started= time.time()

  @commands.command(help="Shows the ping of bot", brief="Returns latency of bot in 'ms'")
  @commands.cooldown(1,2,commands.BucketType.member)
  async def ping(self,ctx):
        embed_ping = discord.Embed(description=(f'**BOT LATENCY :**  `{round(self.bot.latency * 1000)}`ms'), color=discord.Color.random())
        await ctx.send(embed=embed_ping)    


  @commands.command(help="Gives invite link of the bot", brief="Gives invite link of the bot")
  async def invite(self,ctx):
   emb=discord.Embed(color=discord.Color.green())
   emb.add_field(name="INVITE LINK : ",value=f"[Click here](https://discord.com/api/oauth2/authorize?client_id=975053562566557836&permissions=8&scope=bot%20applications.commands)",inline=False)
   await ctx.send(embed=emb)

  @commands.command(help='Returns prefix of the bot', brief='Returns prefix of the bot')
  async def prefix(self,ctx):
   emb=discord.Embed(description=(f'**My prefix is `!`**'), color=discord.Color.gold())
   await ctx.send(embed=emb)

  @commands.command()
  async def botinfo(self,ctx):
        name = await self.bot.application_info()
        embed_bi = discord.Embed(title="DARKLØRÐ",color= discord.Colour.random())
        embed_bi.add_field (name=f"<:games_dot:937350977588178996> ID : 904285165675749426",inline=False,value=f"_ _")
        embed_bi.add_field (name=f"<:games_dot:937350977588178996> Total Servers : {len(self.bot.guilds)}",inline=False,value=f"_ _")
        embed_bi.add_field (name=f"<:games_dot:937350977588178996> Total Users : {len(self.bot.users)}",inline=False,value=f"_ _")
        #embed_bi.add_field (name=f"<:games_dot:937350977588178996> Uptime : {str(datetime.timedelta(seconds=int(round(time.time()-time.time()))))}",inline=False,value=f"_ _")
        embed_bi.add_field (name=f"<:games_dot:937350977588178996> Ping : {round(self.bot.latency * 1000)} ms",inline=False,value=f"_ _")
        embed_bi.add_field (name=f"<:games_dot:937350977588178996> Developers : ",inline=False,value=f"{dark}   [{name.owner}](https://discord.com/users/853550854162743296)")
        embed_bi.set_thumbnail(url=self.bot.user.display_avatar)
        embed_bi.set_footer(icon_url=self.bot.user.display_avatar,text="Made with 🧡 and 💻 in discord.py")
        await ctx.send(embed=embed_bi)

  @commands.Cog.listener()
  async def on_guild_join(self,guild):
    c = self.bot.get_channel(975787780162605146)
    await c.send(f"GUILD NAME : {guild.name}\n GUILD OWNER : {guild.owner}\n Members : {guild.member_count}")

  @commands.Cog.listener()
  async def on_guild_remove(self,guild):
     c = self.bot.get_channel(974312785599135744)
     await c.send(f"GUILD NAME : {guild.name}\n GUILD OWNER : {guild.owner}\n Members : {guild.member_count}")

   

  """@commands.command()
  async def vote(self,ctx):
    emb=discord.Embed(title="Vote", url="https://top.gg/bot/807615902870536213/vote", description="You can vote me here :)",color=discord.Color.green())
    await ctx.send(embed=emb)"""
    
def setup(bot):
  bot.add_cog(Bot(bot))