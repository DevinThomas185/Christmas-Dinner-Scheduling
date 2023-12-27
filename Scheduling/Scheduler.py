from Classes.CookingMethod import CookingMethod
from Problems.Problem import Problem
from Classes.Appliance import Appliance
from Scheduling.Schedule import Schedule


def get_items_currently_in_appliance(
    time: int, schedule: Schedule, appliance: Appliance
):
    """
    Gets the items currently in the appliance.

    :param schedule: The schedule to get the items from.
    :param appliance: The appliance to get the items from.
    :return: The items currently in the appliance.
    """
    items = []
    for (
        appliance_slot,
        appliance_slot_schedule,
    ) in schedule.get_appliance_slot_schedules().items():
        current_time = 0
        if appliance_slot.get_appliance() == appliance:
            for food_item in appliance_slot_schedule:
                if current_time <= time <= current_time + food_item.get_total_time():
                    items.append(food_item)
                current_time += food_item.get_total_time()
    return items


def check_schedule_valid(schedule: Schedule, problem: Problem) -> bool:
    """
    Checks if the schedule is valid.

    :return: True if the schedule is valid, False otherwise.
    """

    # Check if all food items scheduled for an appliance can be cooked by that appliance
    for (
        appliance_slot,
        appliance_slot_schedule,
    ) in schedule.get_appliance_slot_schedules().items():
        for food_item in appliance_slot_schedule:
            if (
                food_item.get_cooking_method()
                not in appliance_slot.get_appliance().get_cooking_methods()
            ):
                return False

    # Check if all food items are scheduled
    for food_item in problem.get_food_items():
        scheduled = False
        for appliance_slot_schedule in schedule.get_appliance_slot_schedules().values():
            if food_item in appliance_slot_schedule:
                scheduled = True
                break
        if not scheduled:
            return False

    # Check that the items that in the same appliance at the same time have roughly equal cooking temperatures
    for appliance in problem.get_appliances():
        for time in range(schedule.get_max_appliance_slot_schedule()):
            items = get_items_currently_in_appliance(time, schedule, appliance)
            # print(appliance, items, time)
            cooking_temperatures = [item.get_cooking_temperature() for item in items if item.get_cooking_method() == CookingMethod.OVEN]
            if len(cooking_temperatures) > 0:
                if (
                    max(cooking_temperatures) - min(cooking_temperatures)
                    > problem.get_maximum_temperature_difference()
                ):
                    return False

    return True


def generate_initial_schedule(problem: Problem) -> Schedule:
    """
    Generates an initial schedule.

    :param problem: The problem to generate the schedule for.
    :return: The initial schedule.
    """

    appliance_slot_schedules = {}

    for appliance_slot in problem.get_appliance_slots():
        appliance_slot_schedules[appliance_slot] = []

    for food_item in problem.get_food_items():
        for appliance_slot in problem.get_appliance_slots():
            if (
                food_item.get_cooking_method()
                in appliance_slot.get_appliance().get_cooking_methods()
            ):
                appliance_slot_schedules[appliance_slot].append(food_item)
                break

    return Schedule(appliance_slot_schedules)


def schedule_dinner(
    problem: Problem,
    cost_function: callable,
    iterations: int = 10,
) -> Schedule:
    """
    Schedule the problem using Tabu Search.

    :param problem: The problem to schedule.
    """
    best_schedule = generate_initial_schedule(problem)
    best_cost = cost_function(best_schedule)

    for i in range(iterations):
        if (i + 1) % 1000 == 0:
            print(f"Iteration {i + 1}, Cost: {best_cost}")
            print(best_schedule)

        neighbour_schedule = best_schedule.get_neighbour(problem)
        while not check_schedule_valid(neighbour_schedule, problem):
            neighbour_schedule = best_schedule.get_neighbour(problem)

        neighbour_cost = cost_function(neighbour_schedule)

        if neighbour_cost < best_cost:
            best_schedule = neighbour_schedule
            best_cost = neighbour_cost

    return best_schedule, best_cost
