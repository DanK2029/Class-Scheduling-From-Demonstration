from consts import *


empty_class = {
    "name": EMPTY_CLASS
}


def remove_empty_classes(schedule):
    new_schedule = []
    for cl in schedule:
        if not (cl[NAME] == EMPTY_CLASS):
            new_schedule.append(cl)

    # new_sch = filter(lambda c: not (c[NAME] == EMPTY_CLASS), schedule)
    return new_schedule


def convertToTimeline(classes):
    timeline = {}

    for c in classes:
        startTime = c[TIME][0]
        if startTime in timeline:
            timeline[startTime].append(c)
        else:
            timeline[startTime] = [empty_class, c]

    return timeline
