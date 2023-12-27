from Classes.CookingMethod import CookingMethod


class Appliance:
    __slots__ = [
        "__name",
        "__cooking_methods",
    ]

    def __init__(
        self,
        name: str,
        cooking_methods: CookingMethod,
    ):
        self.__name = name
        self.__cooking_methods = cooking_methods

    def get_name(self) -> str:
        return self.__name

    def get_cooking_methods(self) -> CookingMethod:
        return self.__cooking_methods

    def __repr__(self) -> str:
        return self.__name
