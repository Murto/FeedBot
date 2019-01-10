from discord import Embed
from discord import send_message
from discord import User
from typing import NoReturn

class UserReporteeHandle(ReporteeHandle):

  def __init__(self, user) -> NoReturn:
    self.user = user

  def getUser(self) -> User:
    return self.user

  def send(self, sendable : Union[str, Embed]) -> NoReturn:
    if (isinstance(sendable, str)):
      send_message(destination=self.user, content=sendable)
    elif (isinstance(sendable, Embed)):
      send_message(destination=self.user, embed=sendable)

