import asyncio
import discord
from discord.ext import commands
import json
import requests


prefix = "!"
description = "Test description please ignore"
bot = commands.Bot(command_prefix=prefix, description=description)


@bot.event
async def on_ready():
  print("Bot ready")


@bot.command()
async def ping():
  await bot.say("pong")


@bot.command()
async def github():
  githubFile = open("data/github.txt")
  url = githubFile.read().strip()
  await bot.say("Github: %s" % url)


tokenFile = open("token/token.txt")
if (not tokenFile):
  print("Token could not be read, exiting...")
else:
  token = tokenFile.read().strip()
  bot.run(token)
