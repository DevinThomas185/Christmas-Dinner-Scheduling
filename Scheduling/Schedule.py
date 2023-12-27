import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import randomcolor
from Utilities.utils import get_time_string_from_date_time
from Problems.Problem import Problem
from datetime import timedelta


class Schedule:
    __slots__ = [
        "__appliance_slot_schedules",
    ]

    def __init__(self, schedule={}) -> None:
        self.__appliance_slot_schedules = schedule

    def __repr__(self) -> str:
        s = ""
        for (
            appliance_slot,
            appliance_slot_schedule,
        ) in self.__appliance_slot_schedules.items():
            s += f"{appliance_slot}:"
            for food_item in appliance_slot_schedule:
                s += f"{food_item}, "
            s += "\n"
        s += "\n"
        return s

    def get_appliance_slot_schedules(self) -> dict:
        return self.__appliance_slot_schedules

    def get_max_appliance_slot_schedule(self) -> int:
        max_appliance_slot_schedule = 0
        for appliance_slot_schedule in self.__appliance_slot_schedules.values():
            time = 0
            for food_item in appliance_slot_schedule:
                time += food_item.get_total_time()
            if time > max_appliance_slot_schedule:
                max_appliance_slot_schedule = time
        return max_appliance_slot_schedule

    def get_neighbour(self, problem: Problem) -> "Schedule":
        """
        Gets a neighbour of the schedule.

        :return: The neighbour.
        """
        # Pick random number between 1 and total number of food items
        n = np.random.randint(1, len(problem.get_food_items()))

        # Deep copy the schedule
        neighbour = Schedule(
            {
                appliance_slot: appliance_slot_schedule.copy()
                for appliance_slot, appliance_slot_schedule in self.__appliance_slot_schedules.items()
            }
        )

        for _ in range(n):
            # Choose a random food item from the appliance slot
            food_item = np.random.choice(problem.get_food_items())

            # Remove the food item its the appliance slot
            for (
                appliance_slot_schedule
            ) in neighbour.__appliance_slot_schedules.values():
                if food_item in appliance_slot_schedule:
                    appliance_slot_schedule.remove(food_item)
                    break

            # Choose a random appliance slot to move the food item to such that the appliance matches the old appliance cooking method
            new_appliance_slot = np.random.choice(
                [
                    appliance_slot
                    for appliance_slot in neighbour.__appliance_slot_schedules.keys()
                    if food_item.get_cooking_method()
                    in appliance_slot.get_appliance().get_cooking_methods()
                ]
            )

            # Add the food item to the new appliance slot in random position
            pos = (
                np.random.randint(
                    0, len(neighbour.__appliance_slot_schedules[new_appliance_slot])
                )
                if len(neighbour.__appliance_slot_schedules[new_appliance_slot]) > 0
                else 0
            )

            neighbour.__appliance_slot_schedules[new_appliance_slot].insert(
                pos, food_item
            )

        return neighbour

    def graph_schedule(self, problem: Problem, cost: float) -> None:
        colour_generator = randomcolor.RandomColor()

        _, ax = plt.subplots()

        # Set the title
        ax.set_title(f"Schedule for {problem.get_name()} | Cost: {cost}")

        # Set the y-axis labels to the appliance names
        y_labels = [
            str(appliance_slot)
            for appliance_slot in self.__appliance_slot_schedules.keys()
        ]
        ax.set_yticks(range(len(y_labels)))
        ax.set_yticklabels(y_labels)

        # Plot the schedule as horizontal bars in reverse
        for i, (_, appliance_slot_schedule) in enumerate(
            self.__appliance_slot_schedules.items()
        ):
            if len(appliance_slot_schedule) == 0:
                continue

            current_time = problem.get_serve_time()
            for food_item in reversed(appliance_slot_schedule):
                colour = colour_generator.generate(hue="blue")[0]

                end_time = current_time

                end_cooking_time = end_time - timedelta(
                    minutes=food_item.get_resting_time()
                )
                end_preparation_time = end_cooking_time - timedelta(
                    minutes=food_item.get_cooking_time()
                )
                start_time = current_time - timedelta(
                    minutes=food_item.get_total_time()
                )

                print(
                    f"{food_item} | IN: {get_time_string_from_date_time(start_time)} | OUT: {get_time_string_from_date_time(current_time)}"
                )

                # Plot the resting time
                ax.barh(
                    i,
                    timedelta(minutes=food_item.get_resting_time()),
                    left=end_cooking_time,
                    color="#FF" + colour[1:],
                )

                # Plot the cooking time
                ax.barh(
                    i,
                    timedelta(minutes=food_item.get_cooking_time()),
                    left=end_preparation_time,
                    color="#3C" + colour[1:],
                )

                # Plot the preparation time
                ax.barh(
                    i,
                    timedelta(minutes=food_item.get_preparation_time()),
                    left=start_time,
                    color="#1E" + colour[1:],
                )

                # Put food item name in the middle of the bar
                ax.text(
                    start_time + timedelta(minutes=food_item.get_total_time() / 2),
                    i,
                    food_item.get_name()
                    + f" ({food_item.get_cooking_temperature()}°C)",
                    ha="center",
                    va="center",
                )

                current_time -= timedelta(minutes=food_item.get_total_time())

        # Find longest appliance schedule and set the x-axis limits
        max_appliance_slot_schedule = self.get_max_appliance_slot_schedule()

        ax.set_xlim(
            problem.get_serve_time() - timedelta(minutes=max_appliance_slot_schedule),
            problem.get_serve_time(),
        )

        # TODO: Convert x-axis to time, not floats
        xs = mdates.date2num(ax.get_xticks())
        hfmt = mdates.DateFormatter("%H:%M")

        ax.xaxis.set_major_formatter(hfmt)

        # Show the plot
        plt.show()
