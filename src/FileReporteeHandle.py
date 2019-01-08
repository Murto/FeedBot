class FileReporteeHandle:

  def __init__(self, filename):
    self.filename = filename

  def send(self, sendable):
    with open(self.filename, 'w') as f:
      f.write(sendable)

