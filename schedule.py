import numpy as np
from itertools import product
import ConvertClassesToTimeline as ct


def get_schedules(timeline):  # returns list of tuples of all possible schedule combinations
    list_of_schedules = list(product(*timeline.values()))
    return list_of_schedules


def analize_schedule(list_of_schedules, time_constraints):  # list of time constraints
    time_constraints = time_converter(time_constraints)
    classesList = []
    for classTup in list_of_schedules:
        for i in range(len(classTup)):
            for time in time_constraints:
                if (time[0] == classTup[i]['time'][0] or abs(time[0] - classTup[i]['time'][0]) <= 30) and (classTup[i]["days"] == time[1]):
                    if time[0] <= classTup[i]['time'][0] or time[0] >= classTup[i]['time'][1]:
                        if classTup[i] not in classesList:
                            classesList.append(classTup[i])
    return classesList


def time_converter(time_constraints):  # takes in a list of time constraints from user
    convertedTime_constraints = []
    for time in time_constraints:
        if time[0][-2:] == 'am':
            timeInt = int(time[0][:-2])
            hr_to_min = timeInt * 60
            convertedTime_constraints.append(hr_to_min)  # convert to military time
        elif time[0][-2:] == 'pm':
            timeInt = int(time[0][:-2])
            hr_to_min = (timeInt + 12) * 60
            convertedTime_constraints.append(hr_to_min)
    return convertedTime_constraints


def testcode():
    class_timeline = ct.classTimeline('testClasses.json')
    list_of_schedules = get_schedules(class_timeline)
    time_constraints = [('9am', 'TR'), ('11am', 'MWF'), ('1pm', 'MWF'), ('4pm', 'MWF')]

    classesList = analize_schedule(list_of_schedules, time_constraints)
    print(classesList)


if __name__ == "__main__":
    testcode()
