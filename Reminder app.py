from plyer import notification
import time

# get reminder message and time
message = input("Enter your reminder message: ")
reminder_time = input("Enter the time to send the reminder (format: HH:MM:SS): ")

# parse reminder time
hour, minute, seconds = reminder_time.split(":")
hour, minute, seconds = int(hour), int(minute), int(seconds)

# calculate time until reminder
now = time.localtime()
seconds_until_reminder = (hour - now.tm_hour) * 3600 + (minute - now.tm_min) * 60 - now.tm_sec
if seconds_until_reminder < 0:
    seconds_until_reminder += 24 * 3600

# wait until reminder time
time.sleep(seconds_until_reminder)

# send notification
notification.notify(
    title="Reminder",
    message=message,
    app_name="Reminder App",
    timeout=10
)
