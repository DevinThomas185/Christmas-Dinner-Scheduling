from Problems.ChristmasDinner2023 import ChristmasDinner2023
from Scheduling.Scheduler import schedule_dinner
from Utilities.cost_functions import total_earliness


def main():
    problem = ChristmasDinner2023()
    schedule, cost = schedule_dinner(problem, total_earliness, 1_000_0)
    print(schedule)
    schedule.graph_schedule(problem, cost)

    print(total_earliness(schedule))


if __name__ == "__main__":
    main()
