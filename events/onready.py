import discord
from discord.ext import commands

class OnReady(commands.Cog):
  
  def __init__(self, bot: commands.Bot) -> None:
    self.bot = bot
    super().__init__()
   
  @commands.Cog.listener()
  async def on_ready(self):
    print(f"Entrei como {self.bot.user}")
    

def setup(bot: commands.Bot):
  bot.add_cog(OnReady(bot))
