from tires.tires import Tires

class OctoprimeTires(Tires):
  def __init__(self, tire_wear):
    self.tire_wear = tire_wear
  
  def needs_service(self):
    accumulated_wear = 0
    for tire in self.tire_wear:
      accumulated_wear += tire
    
    return accumulated_wear > 0.9