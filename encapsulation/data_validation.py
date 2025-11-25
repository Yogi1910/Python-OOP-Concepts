"""Uses properties to validate data assignments."""

from __future__ import annotations


class TemperatureSensor:
    def __init__(self, celsius: float) -> None:
        self.celsius = celsius

    @property
    def celsius(self) -> float:
        return self._celsius

    @celsius.setter
    def celsius(self, value: float) -> None:
        if value < -273.15:
            raise ValueError("Temperature cannot go below absolute zero")
        self._celsius = value


if __name__ == "__main__":
    sensor = TemperatureSensor(20.0)
    sensor.celsius = 25.0
    print(sensor.celsius)
