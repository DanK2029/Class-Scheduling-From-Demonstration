import numpy as np
from itertools import product


timeline = {"4:15": ["c1", "c2", "c3", "EC"], "5:15": ["c1", "c2", "EC"], "6:15": ["c1", "c2", "c3", "c4", "EC"]}


def get_schedules(timeline):  # returns list of tuples of all possible schedule combinations
    list_of_schedules = list(product(*timeline.values()))
    print(list_of_schedules)
    return list_of_schedules
