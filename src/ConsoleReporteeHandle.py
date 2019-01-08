class ConsoleReporteeHandle(ReporteeHandle):

  def __init__(self, name):
    self.name = name

  def getName(self):
    return self.name

  def send(self, sendable):
    print("[" + self.name + "] " + sendable)
