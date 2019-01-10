from typing import List

class ScheduleProvider:
  
  def getSchedule(self) -> List[ScheduleEvent]:
    pass

  def getNextScheduled(self, num : int = 1) -> ScheduleEvent:
    pass
