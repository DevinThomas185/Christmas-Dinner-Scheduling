from datetime import datetime


def get_time_string_from_date_time(date_time: datetime):
    """
    Gets a time string from a datetime object.

    :param date_time: The datetime object.
    :return: The time string.
    """
    return date_time.strftime("%H:%M")
