from consts import *
import numpy as np
import json
from itertools import product
from timeline import *
from softContraints import *


# returns list of tuples of all possible schedule combinations
def get_schedules(timeline):
    list_of_schedules = list(product(*timeline.values()))

    return list_of_schedules


def main():
    with open('classes.json', 'r') as class_data_file:
        classes_json = json.load(class_data_file)

        class_timeline = convertToTimeline(classes_json)
        all_schedules = get_schedules(class_timeline)

        all_schedules_ex_empty_class = []

        for s in all_schedules:
            schedules_ex_empty_class = remove_empty_classes(s)
            if schedules_ex_empty_class:
                all_schedules_ex_empty_class.append(schedules_ex_empty_class)

        soft_sorted_schedules = sorted(all_schedules_ex_empty_class, key=grade_soft_constraints)

        print(soft_sorted_schedules)


if __name__ == '__main__':
    main()
