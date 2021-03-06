from ReporteeHandle import ReporteeHandle
from typing import NoReturn
from typing import Union


class ConsoleReporteeHandle(ReporteeHandle):

  def __init__(self, name : str) -> NoReturn:
    self.name = name

  def get_name(self) -> str:
    return self.name

  def send(self, sendable : str) -> NoReturn:
    print("[" + self.name + "] " + sendable)
