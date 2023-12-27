from Scheduling.Schedule import Schedule
from datetime import timedelta


def total_earliness(schedule: Schedule) -> int:
    """
    Calculates the total earliness of the schedule.

    :param schedule: The schedule to calculate the earliness for.
    :param problem: The problem to calculate the earliness for.
    :return: The total earliness.
    """
    earliness = []

    for _, appliance_slot_schedule in schedule.get_appliance_slot_schedules().items():
        current_time = 0
        for food_item in reversed(appliance_slot_schedule):
            earliness.append(abs(current_time))
            current_time -= food_item.get_total_time()

    return sum(earliness)
