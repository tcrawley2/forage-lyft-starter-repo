from serviceable import Serviceable


class Car(Serviceable):
    def __init__(self, engine, battery, tires):
        super().__init__(engine, battery, tires)

    def needs_service(self):
        if self.engine.needs_service() or self.battery.needs_service() or self.tires.needs_service():
            return True
        else:
            return False
