import unittest

from tires.carrigan_tires import CarriganTires
from tires.octoprime_tires import OctoprimeTires

class TestCarriganTires(unittest.TestCase):
  def test_tires_should_be_serviced(self):
    tire_wear = [0.5, 0.6, 0.9, 0.7]
    carrigan_tires = CarriganTires(tire_wear)
    self.assertTrue(carrigan_tires.needs_service())
  
  def test_tires_should_not_be_serviced(self):
    tire_wear = [0.5, 0.6, 0.8, 0.7]
    carrigan_tires = CarriganTires(tire_wear)
    self.assertFalse(carrigan_tires.needs_service())

class TestOctoprimeTires(unittest.TestCase):
  def test_tires_should_be_serviced(self):
    tire_wear = [0.2, 0.3, 0.25, 0.25]
    octoprime_tires = OctoprimeTires(tire_wear)
    self.assertTrue(octoprime_tires.needs_service())
  
  def test_tires_should_not_be_serviced(self):
    tire_wear = [0.2, 0.2, 0.2, 0.2]
    octoprime_tires = OctoprimeTires(tire_wear)
    self.assertFalse(octoprime_tires.needs_service())

if __name__ == '__main__':
  unittest.main()
