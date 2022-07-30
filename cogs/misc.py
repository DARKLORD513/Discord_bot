import discord
from discord.ext import commands
import json, requests, asyncio, aiohttp, random

class Misc(commands.Cog):
  def __init__(self, bot):
    self.bot=bot
  
  
  @commands.command(help="Sends a random inspiring quote", brief="Sends a random inspiring quote")
  async def quote (self,ctx):
   def get_quote():
    response =requests.get("https://zenquotes.io/api/random")
    json_data= json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return (quote)
   output=get_quote()
   emb = discord.Embed(title="Quote", description=(output), color=discord.Color.gold())
   await ctx.send(embed=emb)

  """@commands.command(pass_context=True, help="Sends the text specified after the command", brief="Sends the text specified after the command")
  async def say(self,ctx, *args):
   response = ""
   for arg in args:
     response = response + " " + arg
   await ctx.send(response)
   await ctx.message.delete()"""

  @commands.command(help="Search the weather of a place", brief="Sends the weather description of a place")
  async def weather(self,ctx, *, city: str):
   base_url = "http://api.openweathermap.org/data/2.5/weather?"
   api_key = "563edfafe056557a77ede010adfe982a"
   city_name=city
   complete_url=base_url+"appid="+api_key+"&q="+city_name
   response=requests.get(complete_url)
   x=response.json()
   channel=ctx.message.channel
   if x["cod"]!="404":
     async with channel.typing():
       y=x["main"]
       current_temp=y["temp"]
       temp_c=str(round(current_temp-273.15))
       current_press=y["pressure"]
       current_humidity=y["humidity"]
       z=x["weather"]
       desc=z[0]["description"]
       emb=discord.Embed(title=(f"Weather in {city_name}"), color=discord.Color.gold(), timestamp=ctx.message.created_at, )
    
       emb.add_field(name="Description", value=f"**{desc}**", inline=False)
     emb.add_field(name="Temperature", value=f"**{temp_c} °C**", inline=False)
     emb.add_field(name="Humidity", value=f"**{current_humidity}%**", inline=False)
     emb.add_field(name="Atmospheric Pressure", value=f"**{current_press} hPa**", inline=False)
     emb.set_thumbnail(url="https://i.ibb.co/CMrsxdX/weather.png")
     emb.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.display_avatar)
     await ctx.send(embed=emb)
   else:
     cross = "<:no:933679544861327372>"
     emb1=discord.Embed(description=(f"{cross} Please enter a valid location"), color=discord.Color.red())
     await ctx.send(embed=emb1)


  @commands.command(help="Sends random joke",brief=",Sends random joke")
  async def joke(self,ctx):  
   api = 'https://icanhazdadjoke.com/'  
   async with aiohttp.request('GET', api, headers={'Accept': 'text/plain'}) as r:   
    result = await r.text()   
    em=discord.Embed(title="Joke", description=result, color=ctx.message.author.color)
    await ctx.send(embed=em)

  @commands.command(help="Sends random meme",brief="Sends random meme")
  async def meme(self,ctx):
   embed = discord.Embed(title="Meme", color=ctx.message.author.color, timestamp=ctx.message.created_at,)
   async with ctx.message.channel.typing():
    async with aiohttp.ClientSession() as cs:
     async with cs.get(f'https://www.reddit.com/r/memes/new.json?sort=hot') as r:
      res = await r.json()
      embed.set_image(url=res['data']['children'] [random.randint(0, 20)]['data']['url'])
      embed.set_footer(text=f"Requested by {ctx.message.author}", icon_url=ctx.message.author.display_avatar)
      await ctx.send(embed=embed)
def setup(bot):
  bot.add_cog(Misc(bot))