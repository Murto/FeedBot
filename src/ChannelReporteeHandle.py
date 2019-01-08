from discord import send_message

class ChannelReporteeHandle(ReporteeHandle):
  def __init__(self, channel):
    self.channel

  def getUser(self):
    return self.user

  def send(self, sendable):
    if (isinstance(sendable, str)):
      send_message(destination=self.channel, content=sendable)
    elif (isinstance(sendable, Embed)):
      send_message(destination=self.channel, embed=sendable)

