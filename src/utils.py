import asyncio
import discord


def makeUsageText(prefix="", name=None, parameters=[], optionals=[]):
  
  assert(all([ optional in parameters for optional in optionals ]))

  return ("`Usage: %s%s " % (prefix, name)) + " ".join([ "[%s]" % p if p in optionals else "<%s>" % p for p in parameters ]) + "`" 


async def sendSelfDestruct(embed, sendFun, delFun, time=5):
  footer = "This message will self destruct in %d seconds..." % time
  embed.set_footer(text=footer)
  msg = await sendFun(embed=embed)
  await asyncio.sleep(time)
  await delFun(msg)



async def sendFailureMessage(title=None, description=None, sendFun=None, delFun=None, selfDestruct=False, time=5):
  
  assert(title)

  assert(sendFun)

  assert(delFun)
  
  title = "__%s__" % title

  e = discord.Embed()
  e.title = title
  e.description = description
  e.colour = discord.Colour.red()
  if (selfDestruct):
    await sendSelfDestruct(e, sendFun, delFun)
  else:
    await sendFun(embed=e)
