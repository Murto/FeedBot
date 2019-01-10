import discord
from discord import Channel
from discord import Embed
from typing import NoReturn
from typing import Union


class ChannelReporteeHandle(ReporteeHandle):
  
  def __init__(self, channel : Channel) -> NoReturn:
    self.channel = channel

  def getChannel(self) -> Channel:
    return self.channel

  def send(self, sendable : Union[str, Embed]) -> NoReturn:
    if (isinstance(sendable, str)):
      send_message(destination=self.channel, content=sendable)
    elif (isinstance(sendable, Embed)):
      send_message(destination=self.channel, embed=sendable)

