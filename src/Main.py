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
  text = githubFile.read()
  await bot.say(text)


tokenFile = open("data/token.txt")
if (not tokenFile):
  print("Token could not be read, exiting...")
else:
  token = tokenFile.read().strip()
  bot.run(token)
