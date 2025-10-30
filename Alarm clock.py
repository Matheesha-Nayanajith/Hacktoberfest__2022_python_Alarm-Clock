from datetime import datetime
from playsound import playsound
import time

# Ask user for alarm time in HH:MM:SS AM/PM format
alarm_time = input("Enter the time of alarm to be set (HH:MM:SS AM/PM):\n")

# Validate input format
try:
    alarm_hour, alarm_minute, alarm_seconds = map(int, alarm_time[:-3].split(':'))
    alarm_period = alarm_time[-2:].upper()
except:
    print("Invalid time format. Please enter in HH:MM:SS AM/PM format.")
    exit()

print("Setting up alarm...")

while True:
    now = datetime.now()
    current_hour = int(now.strftime("%I"))
    current_minute = int(now.strftime("%M"))
    current_seconds = int(now.strftime("%S"))
    current_period = now.strftime("%p")

    if (alarm_period == current_period and
        alarm_hour == current_hour and
        alarm_minute == current_minute and
        alarm_seconds == current_seconds):
        print("Good morning! Wake up!")
        playsound('audio.mp3')
        break
    
    # Sleep 1 second to reduce CPU usage
    time.sleep(1)
