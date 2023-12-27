from Classes.Appliance import Appliance
from Classes.ApplianceSlot import ApplianceSlot
from Classes.FoodItem import FoodItem
from datetime import datetime


class Problem:
    __slots__ = [
        "_name",
        "_appliances",
        "_appliance_slots",
        "_food_items",
        "_serve_time",
        "_maximum_temperature_difference",
    ]

    def __init__(
        self,
        name: str,
        serve_time: datetime,
        maximum_temperature_difference: int = 20,
    ):
        self._name = name
        self._appliances = []
        self._appliance_slots = []
        self._food_items = []
        self._serve_time = serve_time
        self._maximum_temperature_difference = maximum_temperature_difference

    def get_name(self) -> str:
        return self._name

    def get_appliances(self) -> list[Appliance]:
        return self._appliances

    def get_appliance_slots(self) -> list[ApplianceSlot]:
        return self._appliance_slots

    def get_food_items(self) -> list[FoodItem]:
        return self._food_items

    def get_serve_time(self) -> datetime:
        return self._serve_time

    def get_maximum_temperature_difference(self) -> int:
        return self._maximum_temperature_difference

    def __repr__(self) -> str:
        return self._name
