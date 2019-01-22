from typing import List

class ScheduleProvider:
  
  def get_schedule(self) -> List[ScheduleEvent]:
    pass

  def get_next_scheduled(self, num : int = 1) -> ScheduleEvent:
    pass
