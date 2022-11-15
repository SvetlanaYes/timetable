from datetime import time
# You can use timedelta for the times by that you will avoid this kind of code

def add_times(time1, time2):
    hour = time1.hour + time2.hour
    minute = time1.minute + time2.minute
    if minute > 59:
        hour += 1
        minute -= 60
    if hour > 23:
        return False
    return time(hour, minute)


def sub_times(time1, time2):
    hour = time1.hour - time2.hour
    minute = time1.minute - time2.minute
    if minute < 0:
        hour -= 1
        minute *= -1
    if hour < 0:
        return False
    return time(hour, minute)
