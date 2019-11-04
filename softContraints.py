from consts import *
import json


def startTimeSoftConstraint(start_time, schedule):
    schedule_start_time = float("inf")

    for c in schedule:
        schedule_start_time = min(c[TIME][0], schedule_start_time)

    return (start_time - schedule_start_time)**2


def endTimeSoftConstraint(end_time, schedule):
    schedule_start_time = float("inf")

    for c in schedule:
        schedule_start_time = max(c[TIME][1], schedule_start_time)

    return (end_time - schedule_start_time)**2


def creditHoursSoftConstraint(total_hours, schedule):
    schedule_total_hours = 0

    for c in schedule:
        schedule_total_hours += c[HOURS]

    return (total_hours - schedule_total_hours)**2


def difficultySoftConstraint(difficulty, schedule):
    avg_difficulty = 0

    for c in schedule:
        avg_difficulty += c[DIFFICULTY]

    if len(schedule) == 0:
        return float('inf')
    else:
        avg_difficulty /= len(schedule)

    return (avg_difficulty - difficulty)**2


def grade_soft_constraints(schedule):
    with open('preferences.json', 'r') as pref_data_file:
        pref_json = json.load(pref_data_file)

        start_time_metric = startTimeSoftConstraint(pref_json[START_TIME], schedule)
        end_time_metric = endTimeSoftConstraint(pref_json[END_TIME], schedule)
        credit_hours_metric = creditHoursSoftConstraint(pref_json[TOTAL_HOURS], schedule)
        difficulty_metric = difficultySoftConstraint(pref_json[DIFFICULTY], schedule)

        return start_time_metric + end_time_metric + credit_hours_metric + difficulty_metric
