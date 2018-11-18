import asyncio
import discord
from discord.ext import commands
import json
import requests
import utils

prefix = "!"
description = "Test description please ignore"
bot = commands.Bot(command_prefix=prefix, description=description)
feeds = dict()


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


@bot.command(pass_context=True)
async def feed(ctx, source=None, calendar=None):
  if (source and calendar):
    reply = discord.Embed()
    reply.title = "Feed"
    reply.type = "rich"
    reply.description = "Feed created"
    await bot.say(embed=reply)
  else:
    usageText = utils.makeUsageText(prefix=prefix, name="feed", parameters=["drive", "calendar"])
    def delAll(msg):
      bot.delete_message(ctx)
      bot.delete_message(msg)
    await utils.sendFailureMessage(title="Unknown", description=usageText, sendFun=bot.say, delFun=bot.delete_message, selfDestruct=False)


tokenFile = open("data/discord/token.txt")
if (not tokenFile):
  print("Token could not be read, exiting...")
else:
  token = tokenFile.read().strip()
  bot.run(token)
