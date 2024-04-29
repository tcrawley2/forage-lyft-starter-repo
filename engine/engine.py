from abc import ABC, abstractmethod

class Engine(ABC):
  def __init__(self, last_service_milage, current_milage):
    self.last_service_milage = last_service_milage
    self.current_milage = current_milage

  
  @abstractmethod
  def needs_service():
    pass