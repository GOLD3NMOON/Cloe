import discord
from discord.ext import commands

class BasicCommands(commands.Cog):
  
  def __init__(self, bot: commands.Bot) -> None:
    
    self.bot = bot
    
    super().__init__()
    
  @discord.slash_command(name="hello", description="comando teste")
  async def NomeSimbolico(self, Interaction: discord.Interaction):
    await Interaction.response.send_message("Hello world", ephemeral = True)
    
def setup(bot: commands.Bot):
  bot.add_cog(BasicCommands(bot))
