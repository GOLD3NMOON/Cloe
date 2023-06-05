import discord
from discord.ext import commands


class OnReady(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        super().__init__()

    @commands.Cog.listener()
    async def on_ready(self):
        print("╭─━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━─╮")
        print("   Bot conectado e pronto para uso   ")
        print("╰─━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━─╯")
        print(f"     Nome do bot: {self.bot.user.name}   ")
        print(f"     ID do bot: {self.bot.user.id}   ")
        print(f"     Quantidade de servidores: {len(self.bot.guilds)}   ")
        print("╭─━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━─╮")
        print("   Servidores conectados:   ")
        for guild in self.bot.guilds:
            print(f"     Nome do servidor: {guild.name}   ")
            print(f"     ID do servidor: {guild.id}   ")
            print("╰─━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━─╯")


def setup(bot: commands.Bot):
    bot.add_cog(OnReady(bot))
