from softConstraints import *


def getStartTime(bestSchedule):
    startTime = float("inf")
    for c in bestSchedule:
        startTime = min(c["time"][0], startTime)
    return startTime


def getEndTime(bestSchedule):
    endTime = 0
    for c in bestSchedule:
        endTime = min(c["time"][1], endTime)
    return endTime


def getTotalHours(bestSchedule):
    totalHours = 0
    for c in bestSchedule:
        totalHours += c['hours']
    return totalHours


def getAvgGPA(bestSchedule):
    avgGPA = 0
    for c in bestSchedule:
        avgGPA += c["difficulty"]
    return avgGPA / len(bestSchedule)


def getScheduleVec(bestSchedule):
    return [getStartTime(bestSchedule), getEndTime(bestSchedule), getTotalHours(bestSchedule), getAvgGPA(bestSchedule)]
