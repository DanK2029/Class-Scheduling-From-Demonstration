from tkinter import Tk, Canvas, Frame, Entry, Button, IntVar
import math
from timeline import *
import random as rand


class ScheduleGUI:
    def __init__(self, schedule, index):
        root = Tk()
        root.title("Schedule GUI " + str(index+1))

        outerFrame = Frame(root)
        outerFrame.pack()
        self.grade = IntVar()

        height = 500
        width = 800
        dayText = ["TIME", "MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY"]
        numDays = len(dayText)
        textOffset = width / (2 * numDays)
        textHeight = 10

        scheduleCanvas = Canvas(outerFrame, width=width, height=height, bg="white", bd=0, highlightthickness=1, highlightbackground="black")
        scheduleCanvas.pack(side="left")

        # create border lines
        scheduleCanvas.create_line(0, 2*textHeight, width,  2*textHeight, fill="black")

        # create vertical days lines
        for i in range(numDays):
            x = width * ((i+1) / numDays)
            scheduleCanvas.create_line(x, 0, x, height, fill="black")
            scheduleCanvas.create_text(x-textOffset, textHeight, fill="black", text=dayText[i])

        minHour = 7
        maxHour = 18
        numHours = math.ceil((maxHour-minHour))
        for time in range(numHours):
            th = 2 * textHeight + (time / numHours * (height - 2 * textHeight))
            timeText = time + minHour

            if timeText < 12:
                timeText = str(timeText) + ":00am"
            elif timeText == 12:
                timeText = str(timeText) + ":00pm"
            else:
                timeText = str(timeText % 12) + ":00pm"

            scheduleCanvas.create_text(1 / (2 * numDays) * width, th + ((0.25 / numHours) * (height - 2*textHeight)),
                                       fill="black", text=timeText)
            scheduleCanvas.create_line(0, th, width, th, fill="black")

        weekdays = {
            "M": 1,
            "T": 2,
            "W": 3,
            "R": 4,
            "F": 5
        }

        colors = ["#FFDFD3", "#E0BBE4", "#bae1ff", "#baffc9", "#ffffba", "#ffdfba", "#ffb3ba"]

        minMin = minHour * 60
        maxMin = maxHour * 60
        colorSet = rand.sample(colors, len(schedule))
        for i, c in enumerate(schedule):
            startTime = c["time"][0]
            endTime = c["time"][1]
            startTime = ((startTime - minMin) / (maxMin - minMin)) * (height - 2 * textHeight)
            endTime = (endTime - minMin) / (maxMin - minMin) * (height - 2 * textHeight)

            for _, day in enumerate(c["days"]):
                x = weekdays[day]
                scheduleCanvas.create_rectangle(width * (x / numDays), startTime, width * ((x+1) / numDays), endTime, fill=colorSet[i])
                scheduleCanvas.create_text(width * ((x / numDays) + (0.5 / numDays)), (startTime+endTime)/2 - (endTime-startTime)/4, fill="black", text=c["name"])
                scheduleCanvas.create_text(width * ((x / numDays) + (0.5 / numDays)), ((startTime+endTime)/2) + (endTime-startTime)/4, fill="black", text="HRS:" + str(c["hours"]) + ", " + "GPA: " + str(c["difficulty"]))

        inputFrame = Frame(root)
        inputFrame.pack(side="bottom", fill="both")


        def grade_schedule():
            self.grade.set(gradeInput.get())
            root.destroy()

        gradeInput = Button(inputFrame, text="Grade Schedule", command=grade_schedule)
        gradeInput.pack(side="right")

        gradeInput = Entry(inputFrame)
        gradeInput.pack(side="right")

        root.mainloop()
