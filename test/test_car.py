import unittest
from datetime import datetime

# import sys
# sys.path.append('/Users/timcrawley/Desktop/projects/Forage-projects/Lyft-project-new/forage-lyft-starter-repo')
from engine.engine import Engine
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery

class TestCapulet(unittest.TestCase):
    # > 30000
    def test_engine_should_be_serviced(self):
        current_mileage = 70000
        last_service_mileage = 30000
        capulet_engine = CapuletEngine(last_service_mileage, current_mileage)
        self.assertTrue(capulet_engine.needs_service())

    def test_engine_should_not_be_serviced(self):
        current_mileage = 50000
        last_service_mileage = 30000
        capulet_engine = CapuletEngine(last_service_mileage, current_mileage)
        self.assertFalse(capulet_engine.needs_service())

class TestSternman(unittest.TestCase):
    # service light
    def test_engine_should_be_serviced(self):
        current_mileage = 70000
        last_service_mileage = 30000
        sternman_engine = SternmanEngine(last_service_mileage, current_mileage, True)
        self.assertTrue(sternman_engine.needs_service())

    def test_engine_should_not_be_serviced(self):
        current_mileage = 70000
        last_service_mileage = 30000
        sternman_engine = SternmanEngine(last_service_mileage, current_mileage, False)
        self.assertFalse(sternman_engine.needs_service())

class TestWilloughby(unittest.TestCase):
    # > 60000
    def test_engine_should_be_serviced(self):
        current_mileage = 130000
        last_service_mileage = 60000
        willoughby_engine = WilloughbyEngine(last_service_mileage, current_mileage)
        self.assertTrue(willoughby_engine.needs_service())

    def test_engine_should_not_be_serviced(self):
        current_mileage = 110000
        last_service_mileage = 60000
        willoughby_engine = WilloughbyEngine(last_service_mileage, current_mileage)
        self.assertFalse(willoughby_engine.needs_service())

class TestNubbin(unittest.TestCase):
    # 4 years
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        five_years_ago = today.replace(year=today.year-5)
        nubbin = NubbinBattery(five_years_ago, today)
        self.assertTrue(nubbin.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        three_years_ago = today.replace(year=today.year-3)
        nubbin = NubbinBattery(three_years_ago, today)
        self.assertFalse(nubbin.needs_service())

class TestSpindler(unittest.TestCase):
    # 2 years
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        three_years_ago = today.replace(year=today.year-3)
        nubbin = SpindlerBattery(three_years_ago, today)
        self.assertTrue(nubbin.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        one_year_ago = today.replace(year=today.year-1)
        nubbin = SpindlerBattery(one_year_ago, today)
        self.assertFalse(nubbin.needs_service())

if __name__ == '__main__':
    unittest.main()