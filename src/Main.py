import asyncio
import discord
from discord.ext import commands
import json
import requests


prefix = "!"
description = "Test description please ignore"
bot = commands.Bot(command_prefix=prefix, description=description)

tokenFile = open("token/token.txt")
if (not tokenFile):
  print("Token could not be read, exiting...")
else:
  token = tokenFile.read().strip()
  bot.run(token)
