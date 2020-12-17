import sys
import time
import datetime
import pygame
from pygame import mixer
from datetime import datetime
from datetime import date
from datetime import timedelta

currentDate2 = datetime.now()
currentDate = currentDate2.strftime("%Y%m%d")

#starting the mixer for playing the audio files
mixer.init()

#opening the calendar file, "calendar.txt" should be the name of the file containing the events
with open("/home/pi/practiceRoom/calendar.txt", "r") as doc:
    
    #creating the arrays for the start and end time of the events
    startTime = []
    endTime = []

    #getting the start time and end time from the document
    for ln in doc:
        if ln.startswith(currentDate):
            #the number 30 is the removed character, removing all of the excess numbers which aren't needed
            startTime.append(ln)

print(len(startTime))
#print(startTime[0])

#the amount of times the loop is going to repeat
repeatVar = len(startTime)


#the big loop
while repeatVar > 0:

    #slicing string up
    def printYear(sliceYear):
        return sliceYear[:4]

    def printMonth(sliceMonth):
        return sliceMonth[4:6]

    def printDay(sliceDay):
        return sliceDay[6:8]

    def printTime(sliceTime):
        return sliceTime[9:13]

    def minSlice(sliceMin):
        return sliceMin[2:4]

    def hourSlice(sliceHour):
        return sliceHour[0:2]

    #Current date and time
    dateNow = datetime.now()
    currentMinute = dateNow.strftime("%M")
    currentHour = dateNow.strftime("%H")


    #Prints the results of the date
    print("The start of the event is: " + printMonth(startTime[0]) +"/" + printDay(startTime[0]) + "/" + printYear(startTime[0]) + " at " + printTime(startTime[0]))

    #getting the start time of the event
    intTime = printTime(startTime[0])

    #intTime = str(intTime)
    #intTime.lstrip('0')

    #converting strings to integers
    currentHour = int(currentHour)
    currentMinute = int(currentMinute)

    #slicing up the variable
    subtractionMinute = minSlice(intTime)

    #turning this variable into an integer for the if statement
    subtractionMinute = int(subtractionMinute)

    #removing characters
    hourPlace = hourSlice(intTime)

    hourPlace = int(hourPlace)

    #removing 10 minutes from the event start time
    if subtractionMinute >= 10:
        subtractionMinute = subtractionMinute - 10
    else:
        subtractionMinute = subtractionMinute + 50
        hourPlace = hourPlace - 1
        
    subtractionMinute = str(subtractionMinute)
    
    if len(subtractionMinute) == 1:
        subtractionMinute = "0" + subtractionMinute

    #turning the variable back into a string so that the characters will merge together, and not add
    subtractionMinute = str(subtractionMinute)

    hourPlace = str(hourPlace)

    #adding the variables
    comparisonVar = hourPlace + subtractionMinute

    #turning the comparing variable into an integer so that it can be properly compared
    comparisonVar = int(comparisonVar)

    #getting the current time in an integer format
    currentMinuteHour = int((currentHour * 100) + currentMinute)

    #converting and printing the combination of hours and minutes
    currentMinuteHour = int(currentMinuteHour)

    intTime = int(intTime)
    
    checkEqual = (currentMinuteHour == intTime)
    while checkEqual != True:
        
        print(currentMinuteHour)
        print(comparisonVar)
        
        #getting the updated time of the computer
        dateNow = datetime.now()
        currentMinute = dateNow.strftime("%M")
        currentHour = dateNow.strftime("%H")

        #redoing the comparison variables
        currentMinuteHour = (dateNow.strftime("%H") + currentMinute)
        currentMinuteHour = int(currentMinuteHour)

        #checking if the times are the same
        checkEqual = (currentMinuteHour == comparisonVar)
        
        #waiting 15 seconds, can be changed as necessary
        time.sleep(15)
        

    #can be changed to the sound when needed, but this is what will happen when the start time and scheduled time are the same
    print("yay ;D")
    mixer.init()
    mixer.stop()
    mixer.music.load("/home/pi/practiceRoom/10MinWarning.mp3")
    mixer.music.play()
    print(datetime.now())










    #Current date and time
    dateNow = datetime.now()
    currentMinute = dateNow.strftime("%M")
    currentHour = dateNow.strftime("%H")


    #Prints the results of the date
    print("The start of the event is: " + printMonth(startTime[0]) +"/" + printDay(startTime[0]) + "/" + printYear(startTime[0]) + " at " + printTime(startTime[0]))

    #closing document
    doc.closed

    #getting the end time of the event
    intTime = printTime(startTime[0])

    #converting strings to integers
    currentHour = int(currentHour)
    currentMinute = int(currentMinute)

    #slicing up the variable
    subtractionMinute = minSlice(intTime)

    #turning this variable into an integer for the if statement
    subtractionMinute = int(subtractionMinute)
    
    hourPlace = int(hourPlace)

    #removing 5 minutes from the event start time
    if 5 <= subtractionMinute <= 59:
        subtractionMinute = subtractionMinute - 5
    else:
        subtractionMinute = subtractionMinute + 55
        hourPlace = hourPlace - 1

    #removing characters
    hourPlace = hourSlice(intTime)
    
    subtractionMinute = str(subtractionMinute)
    
    if len(subtractionMinute) == 1:
        subtractionMinute = "0" + subtractionMinute
    
    #turning the variable back into a string so that the characters will merge together, and not add
    subtractionMinute = str(subtractionMinute)

    #adding the variables
    comparisonVar = hourPlace + subtractionMinute

    #turning the comparing variable into an integer so that it can be properly compared
    comparisonVar = int(comparisonVar)

    #getting the current time in an integer format
    currentMinuteHour = int((currentHour * 100) + currentMinute)

    #converting and printing the combination of hours and minutes
    currentMinuteHour = int(currentMinuteHour)

    
    checkEqual = (currentMinuteHour == intTime)
    while checkEqual != True:
    
        print(currentMinuteHour)
        print(comparisonVar)
        
        #getting the updated time of the computer
        dateNow = datetime.now()
        currentMinute = dateNow.strftime("%M")
        currentHour = dateNow.strftime("%H")

        #redoing the comparison variables
        currentMinuteHour = (dateNow.strftime("%H") + currentMinute)
        currentMinuteHour = int(currentMinuteHour)

        #checking if the times are the same
        checkEqual = (currentMinuteHour == comparisonVar)
        
        #waiting 15 seconds, can be changed as necessary
        time.sleep(15)
    
    

    #can be changed to the sound when needed, but this is what will happen when the start time and scheduled time are the same
    print("yay ;D")
    mixer.init()
    mixer.stop
    mixer.music.load("/home/pi/practiceRoom/fiveMinWarning.mp3")
    mixer.music.play()
    print(datetime.now())

    #deleting the variable off of the array    
    del startTime[0]

    repeatVar = len(startTime)









#Below is unused code, but I still want to keep
