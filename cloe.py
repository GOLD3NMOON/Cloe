import discord
import json
from discord.ext.commands import Bot 
import os

with open("config.json") as f:
  configData = json.load(f)

client = Bot(command_prefix="!", intents=discord.Intents.all())

# Carregar os comandos
for filename in os.listdir("./commands"):
  if filename.endswith(".py") and not filename.startswith("__"):
    client.load_extension("commands.{0}".format(filename[:-3]))

# Carregar os eventos
for filename in os.listdir("./events"):
  if filename.endswith(".py") and not filename.startswith("__"):
    client.load_extension("events.{0}".format(filename[:-3]))

client.run(configData["token"])
