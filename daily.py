import schedule
import time
import os
import /home/pi/practiceRoom/main.py

def job2():
    os.system("/home/pi/practiceRoom/main.py")
    return
    
schedule.every().day.at("10:55").do(job2())

while True:
    schedule.run_pending()
    time.sleep(30)

