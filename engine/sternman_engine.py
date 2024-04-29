from engine.engine import Engine


class SternmanEngine(Engine):
    def __init__(self, last_service_mileage, current_mileage, warning_light_is_on):
        super().__init__(last_service_mileage, current_mileage)
        self.warning_light_is_on = warning_light_is_on

    def needs_service(self):
        if self.warning_light_is_on:
            return True
        else:
            return False
