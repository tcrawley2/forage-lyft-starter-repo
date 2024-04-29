from abc import ABC, abstractmethod

class Serviceable(ABC):
  def __init__(self, engine, battery, tires):
    self.engine = engine
    self.battery = battery
    self.tires = tires
  
  @abstractmethod
  def needs_service(self):
    pass