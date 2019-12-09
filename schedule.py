from consts import *
import numpy as np
import json
from itertools import product
from timeline import *
from softConstraints import *
from hardConstraints import *
from scheduleGui import *
import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from util import *


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
            convertedTime_constraints.append([hr_to_min, time[1]])  # convert to military time
        elif time[0][-2:] == 'pm':
            timeInt = int(time[0][:-2])
            hr_to_min = (timeInt + 12) * 60
            convertedTime_constraints.append([hr_to_min, time[1]])
    return convertedTime_constraints


def main():
    classesJsonList = []
    constraintsList = []

    with open('classes.json', 'r') as class_data_file:
        classes_json = json.load(class_data_file)

        class_timeline = convertToTimeline(classes_json)
        all_schedules = get_schedules(class_timeline)

        all_schedules_ex_empty_class = []

        for s in all_schedules:
            schedules_ex_empty_class = remove_empty_classes(s)
            if schedules_ex_empty_class:
                all_schedules_ex_empty_class.append(schedules_ex_empty_class)

        with open('timePreferences.json', 'r') as time_preferences_data_file:
            time_preferences_json = json.load(time_preferences_data_file)

        hard_constraints_schedules = apply_hard_constraints(all_schedules_ex_empty_class)

        soft_sorted_schedules = sorted(hard_constraints_schedules, key=grade_soft_constraints)
        bestSchedules = soft_sorted_schedules[0:10]

        scheduleGrades = []
        X = []

        for i in range(len(bestSchedules) - 1):
            scheduleGui = ScheduleGUI(bestSchedules[i], i)
            scheduleGrades.append((scheduleGui.grade.get()))
            X.append(getScheduleVec(bestSchedules[i]))

        Y = scheduleGrades

        regressor = LinearRegression()
        regressor.fit(X, Y)

        newUserScore = regressor.predict([getScheduleVec(soft_sorted_schedules[12])])

        schedule_scores = [(getScheduleVec(schedule), regressor.predict([getScheduleVec(schedule)])) for schedule in soft_sorted_schedules]

        best_schedule_score = []

        for schedule_scores_tup in schedule_scores:
            if schedule_scores_tup[1] <= 100 and schedule_scores_tup[1] >= 0:
                best_schedule_score.append([schedule_scores_tup[0], schedule_scores_tup[1]])

        best_schedule_score.sort(key=lambda x: x[1])
        best_schedule_score = best_schedule_score[-1]

        print("best schedule and score: ", best_schedule_score)


if __name__ == '__main__':
    main()
