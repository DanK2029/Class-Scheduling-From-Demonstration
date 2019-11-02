import json


def convertToTimeline(classes):
    timeline = {}

    for c in classes:
        startTime = c["time"][0]
        if startTime in timeline:
            timeline[startTime].append(c)
        else:
            timeline[startTime] = [c]

    return timeline


with open('classes.json', 'r') as class_data_file:
    classes_json = json.load(class_data_file)
    class_timeline = convertToTimeline(classes_json)
    print(class_timeline)