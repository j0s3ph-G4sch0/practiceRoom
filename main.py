import sys
import time
import datetime
import pygame
import schedule
from pygame import mixer
from datetime import datetime
from datetime import date
from datetime import timedelta


def mainScript():
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
        eventStartTime = printTime(startTime[0])

        #eventStartTime = str(eventStartTime)
        #eventStartTime.lstrip('0')

        #converting strings to integers
        currentHour = int(currentHour)
        currentMinute = int(currentMinute)

        #slicing up the variable
        minutePlace = minSlice(eventStartTime)

        #turning this variable into an integer for the if statement
        minutePlace = int(minutePlace)

        #removing characters
        hourPlace = hourSlice(eventStartTime)

        hourPlace = int(hourPlace)

        #removing 10 minutes from the event start time
        if minutePlace >= 10:
            minutePlace = minutePlace - 10
        else:
            minutePlace = minutePlace + 50
            hourPlace = hourPlace - 1
            
        minutePlace = str(minutePlace)
        
        if len(minutePlace) == 1:
            minutePlace = "0" + minutePlace

        #turning the variable back into a string so that the characters will merge together, and not add
        minutePlace = str(minutePlace)

        hourPlace = str(hourPlace)

        #adding the variables
        timeComparingVar = hourPlace + minutePlace

        #turning the comparing variable into an integer so that it can be properly compared
        timeComparingVar = int(timeComparingVar)

        #getting the current time in an integer format
        currentMinuteHour = int((currentHour * 100) + currentMinute)

        #converting and printing the combination of hours and minutes
        currentMinuteHour = int(currentMinuteHour)

        eventStartTime = int(eventStartTime)
        
        checkEqual = (currentMinuteHour == eventStartTime)
        while checkEqual != True:
            
            print(currentMinuteHour)
            print(timeComparingVar)
            
            #getting the updated time of the computer
            dateNow = datetime.now()
            currentMinute = dateNow.strftime("%M")
            currentHour = dateNow.strftime("%H")

            #redoing the comparison variables
            currentMinuteHour = (dateNow.strftime("%H") + currentMinute)
            currentMinuteHour = int(currentMinuteHour)

            #checking if the times are the same
            checkEqual = (currentMinuteHour == timeComparingVar)
            
            #waiting 15 seconds, can be changed as necessary
            time.sleep(15)
            

        #can be changed to the sound when needed, but this is what will happen when the start time and scheduled time are the same
        print("yay ;D")
        mixer.init()
        mixer.stop()
        mixer.music.load("/home/pi/practiceRoom/10MinWarning.mp3")
        mixer.music.play()
        print(datetime.now())
        
        
        time.sleep(300)
        
        
        print("yay ;D")
        mixer.init()
        mixer.stop
        mixer.music.load("/home/pi/practiceRoom/fiveMinWarning.mp3")
        mixer.music.play()
        print(datetime.now())

        #deleting the variable off of the array    
        del startTime[0]

        repeatVar = len(startTime)


schedule.every().day.at("20:10").do(mainScript)

while True:
    schedule.run_pending()
    time.sleep(1)
    
#         #Current date and time
#         dateNow = datetime.now()
#         currentMinute = dateNow.strftime("%M")
#         currentHour = dateNow.strftime("%H")
# 
# 
#         #Prints the results of the date
#         print("The start of the event is: " + printMonth(startTime[0]) +"/" + printDay(startTime[0]) + "/" + printYear(startTime[0]) + " at " + preventStartTime(startTime[0]))
# 
#         #closing document
#         doc.closed
# 
#         #getting the start time of the event
#         eventStartTime = preventStartTime(startTime[0])
# 
#         #converting strings to integers
#         currentHour = int(currentHour)
#         currentMinute = int(currentMinute)
# 
#         #slicing up the variable
#         minutePlace = minSlice(eventStartTime)
# 
#         #turning this variable into an integer for the if statement
#         minutePlace = int(minutePlace)
#         
#         hourPlace = int(hourPlace)
# 
#         #removing 5 minutes from the event start time
#         if 5 <= minutePlace <= 59:
#             if minutePlace > 0:
#                 minutePlace = minutePlace - 5
#             else:
#                 minutePlace = minutePlace + 55
#                 hourPlace = hourPlace - 1
#         else:
#             minutePlace = minutePlace + 55
#             hourPlace = hourPlace - 1
# 
#         #removing characters
#         hourPlace = hourSlice(eventStartTime)
#         
#         minutePlace = str(minutePlace)
#         
#         if len(minutePlace) == 1:
#             minutePlace = "0" + minutePlace
#         
#         #turning the variable back into a string so that the characters will merge together, and not add
#         minutePlace = str(minutePlace)
# 
#         #adding the variables
#         timeComparingVar = hourPlace + minutePlace
# 
#         #turning the comparing variable into an integer so that it can be properly compared
#         timeComparingVar = int(timeComparingVar)
# 
#         #getting the current time in an integer format
#         currentMinuteHour = int((currentHour * 100) + currentMinute)
# 
#         #converting and printing the combination of hours and minutes
#         currentMinuteHour = int(currentMinuteHour)
# 
#         
#         checkEqual = (currentMinuteHour == eventStartTime)
#         while checkEqual != True:
#         
#             print(currentMinuteHour)
#             print(timeComparingVar)
#             
#             #getting the updated time of the computer
#             dateNow = datetime.now()
#             currentMinute = dateNow.strftime("%M")
#             currentHour = dateNow.strftime("%H")
# 
#             #redoing the comparison variables
#             currentMinuteHour = (dateNow.strftime("%H") + currentMinute)
#             currentMinuteHour = int(currentMinuteHour)
# 
#             #checking if the times are the same
#             checkEqual = (currentMinuteHour == timeComparingVar)
#             
#             #waiting 15 seconds, can be changed as necessary
#             time.sleep(15)
#         
#         
# 
#         #can be changed to the sound when needed, but this is what will happen when the start time and scheduled time are the same
#         print("yay ;D")
#         mixer.init()
#         mixer.stop
#         mixer.music.load("/home/pi/practiceRoom/fiveMinWarning.mp3")
#         mixer.music.play()
#         print(datetime.now())
# 
#         #deleting the variable off of the array    
#         del startTime[0]
# 
#         repeatVar = len(startTime)

