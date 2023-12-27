from Classes.Appliance import Appliance


class ApplianceSlot:
    __slots__ = [
        "__slot_number",
        "__appliance",
    ]

    def __init__(
        self,
        slot_number: str,
        appliance: Appliance,
    ):
        self.__slot_number = slot_number
        self.__appliance = appliance

    def get_slot_number(self) -> str:
        return self.__slot_number

    def get_appliance(self) -> Appliance:
        return self.__appliance

    def __repr__(self) -> str:
        return str(self.__appliance) + " " + str(self.__slot_number)
