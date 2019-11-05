from consts import *


def time_hard_constraints(schedule):
    sorted_schedule = sorted(schedule, key=lambda c: c[TIME][0])

    for i in range(len(sorted_schedule)-1):
        if schedule[i][TIME][1] > schedule[i+1][TIME][0]:
            return False

    return True


def apply_hard_constraints(schedules):
    return list(filter(time_hard_constraints, schedules))