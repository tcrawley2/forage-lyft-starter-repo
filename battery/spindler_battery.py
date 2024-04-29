from datetime import datetime
from battery.battery import Battery

class SpindlerBattery(Battery):
  def __init__(self, last_service_date, current_date):
    super().__init__(last_service_date, current_date)
  
  def needs_service(self) -> bool:
    service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 3)
    if service_threshold_date < datetime.today().date():
      return True
    else:
      return False