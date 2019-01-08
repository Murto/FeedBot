from discord import send_message

class UserReporteeHandle(ReporteeHandle):

  def __init__(self, user):
    self.user = user

  def getUser(self):
    return self.user

  def send(self, sendable):
    if (isinstance(sendable, str)):
      send_message(destination=self.user, content=sendable)
    elif (isinstance(sendable, Embed)):
      send_message(destination=self.user, embed=sendable)

