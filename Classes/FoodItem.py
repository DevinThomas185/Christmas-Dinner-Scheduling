from Classes.CookingMethod import CookingMethod


class FoodItem:
    __slots__ = [
        "__name",
        "__preparation_time",
        "__cooking_time",
        "__resting_time",
        "__cooking_method",
        "__cooking_temperature",
    ]

    def __init__(
        self,
        name: str,
        preparation_time: int,
        cooking_time: int,
        resting_time: int,
        cooking_method: CookingMethod,
        cooking_temperature: int = None,
    ):
        self.__name = name
        self.__preparation_time = preparation_time
        self.__cooking_time = cooking_time
        self.__resting_time = resting_time
        self.__cooking_method = cooking_method
        self.__cooking_temperature = cooking_temperature

    def get_name(self) -> str:
        return self.__name

    def get_preparation_time(self) -> int:
        return self.__preparation_time

    def get_cooking_time(self) -> int:
        return self.__cooking_time

    def get_resting_time(self) -> int:
        return self.__resting_time

    def get_cooking_method(self) -> CookingMethod:
        return self.__cooking_method

    def get_cooking_temperature(self) -> int:
        return self.__cooking_temperature

    def get_total_time(self) -> int:
        return self.__preparation_time + self.__cooking_time + self.__resting_time

    def __repr__(self) -> str:
        return self.__name
