from Problems.Problem import Problem
from Classes.Appliance import Appliance
from Classes.ApplianceSlot import ApplianceSlot
from Classes.FoodItem import FoodItem
from Classes.CookingMethod import CookingMethod
from Scheduling.Scheduler import generate_initial_schedule
from datetime import datetime


class ChristmasDinner2023(Problem):
    __slots__ = []

    def __init__(self) -> None:
        super().__init__(
            name="Christmas Dinner 2023",
            serve_time=datetime(2023, 12, 25, 14),
            maximum_temperature_difference=20,
        )

        # Appliances
        main_oven = Appliance("Main Oven", [CookingMethod.OVEN])
        side_oven = Appliance("Side Oven", [CookingMethod.OVEN])
        hob = Appliance("Hob", [CookingMethod.HOB])
        grill = Appliance("Grill", [CookingMethod.GRILL])
        microwave = Appliance(
            "Microwave",
            [CookingMethod.MICROWAVE, CookingMethod.GRILL],
        )

        self._appliances = [
            main_oven,
            side_oven,
            hob,
            grill,
            microwave,
        ]

        # Appliance Slots for Appliances
        main_oven1 = ApplianceSlot(1, main_oven)
        main_oven2 = ApplianceSlot(2, main_oven)
        main_oven3 = ApplianceSlot(3, main_oven)
        side_oven1 = ApplianceSlot(1, side_oven)
        side_oven2 = ApplianceSlot(2, side_oven)
        side_oven3 = ApplianceSlot(3, side_oven)
        side_oven4 = ApplianceSlot(4, side_oven)
        side_oven5 = ApplianceSlot(5, side_oven)
        hob1 = ApplianceSlot(1, hob)
        hob2 = ApplianceSlot(2, hob)
        hob3 = ApplianceSlot(3, hob)
        hob4 = ApplianceSlot(4, hob)
        hob5 = ApplianceSlot(5, hob)
        grill = ApplianceSlot(1, grill)
        microwave = ApplianceSlot(1, microwave)

        self._appliance_slots = [
            main_oven1,
            main_oven2,
            main_oven3,
            side_oven1,
            side_oven2,
            side_oven3,
            side_oven4,
            side_oven5,
            hob1,
            hob2,
            hob3,
            hob4,
            hob5,
            grill,
            microwave,
        ]

        # Food Items
        # beef_sear = FoodItem("Beef Sear", 0, 10, 0, CookingMethod.OVEN, 220)
        # beef_cook = FoodItem("Beef Cook", 0, 90, 0, CookingMethod.OVEN, 180)
        # gammon_sear = FoodItem("Gammon Sear", 0, 30, 0, CookingMethod.OVEN, 200)
        # gammon_cook = FoodItem("Gammon Cook", 0, 131, 15, CookingMethod.OVEN, 180)
        beef_gammon = FoodItem("Beef and Gammon", 0, 161, 15, CookingMethod.OVEN, 180)
        nut_roast = FoodItem("Nut Roast", 0, 30, 0, CookingMethod.OVEN, 160)
        pigs_in_blankets = FoodItem(
            "Pigs in Blankets", 0, 27, 0, CookingMethod.OVEN, 180
        )
        onion_artichoke = FoodItem(
            "Onion and Artichoke Tart", 0, 30, 0, CookingMethod.OVEN, 200
        )
        scallop_chorizo = FoodItem("Scallop Chorizo", 0, 26, 0, CookingMethod.OVEN, 180)

        cauliflower_cheese = FoodItem(
            "Cauliflower Cheese", 0, 35, 0, CookingMethod.OVEN, 170
        )
        goose_potatoes = FoodItem(
            "Goose Fat Potatoes", 0, 45, 0, CookingMethod.OVEN, 200
        )
        veg_potatoes = FoodItem(
            "Vegetarian Potatoes", 0, 45, 0, CookingMethod.OVEN, 220
        )
        parsnips = FoodItem("Parsnips", 0, 40, 0, CookingMethod.OVEN, 180)

        brussel_sprouts = FoodItem("Brussel Sprouts", 0, 5, 0, CookingMethod.MICROWAVE)

        red_cabbage = FoodItem("Red Cabbage", 0, 6, 0, CookingMethod.MICROWAVE)

        mash = FoodItem("Mash", 0, 6, 0, CookingMethod.MICROWAVE)



        self._food_items = [
            # beef_sear,
            # beef_cook,
            # gammon_sear,
            # gammon_cook,
            beef_gammon,
            nut_roast,
            pigs_in_blankets,
            onion_artichoke,
            scallop_chorizo,
            cauliflower_cheese,
            goose_potatoes,
            veg_potatoes,
            parsnips,
            brussel_sprouts,
            red_cabbage,
            mash,
        ]

        generate_initial_schedule(self)
