from typing import NoReturn


class FileReporteeHandle:

  def __init__(self, filename : str) -> NoReturn:
    self.filename = filename

  def send(self, sendable : str) -> NoReturn:
    with open(self.filename, 'w') as f:
      f.write(sendable)

