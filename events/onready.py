import discord
from discord.ext import commands


class OnReady(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        super().__init__()

    @commands.Cog.listener()
    async def on_ready(self):
        print("━━━━━━━━━━━━━━━━")
        print(" Bot conectado e pronto para uso ")
        print("━━━━━━━━━━━━━━━━")
        print(f" Nome do bot: {self.bot.user.name} ")
        print(f" ID do bot: {self.bot.user.id} ")
        print(f" Quantidade de servidores: {len(self.bot.guilds)} ")
        print("━━━━━━━━━━━━━━━━")

        await self.bot.change_presence(
            status=discord.Status.idle,
            activity=discord.Activity(type=discord.ActivityType.listening, name="brilho da lua.")
        )


def setup(bot: commands.Bot):
    bot.add_cog(OnReady(bot))
