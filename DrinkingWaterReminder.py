import ctypes
import schedule
import time
from datetime import datetime
from plyer import notification

notification_count = 0
max_notifications = 3


def send_drinking_water_notification():
    global notification_count
    """Send a drinking water reminder notification if the system is active."""
    idle_time = get_idle_duration()

    # Assuming 5 minutes as the threshold. If the system has been idle for less than 5 minutes, send a notification.
    if idle_time < 5 * 60 and notification_count < max_notifications:  # Convert minutes to seconds
        notification.notify(
            title="Drinking Water Reminder",
            message="Time to drink water!",
            timeout=10  # Notification stays for 10 seconds
        )
        notification_count += 1


def get_idle_duration():
    """Get system idle time in seconds for Windows."""
    class LASTINPUTINFO(ctypes.Structure):
        _fields_ = [("cbSize", ctypes.c_uint), ("dwTime", ctypes.c_uint)]

    lii = LASTINPUTINFO()
    lii.cbSize = ctypes.sizeof(LASTINPUTINFO)
    ctypes.windll.user32.GetLastInputInfo(ctypes.byref(lii))
    millis = ctypes.windll.kernel32.GetTickCount() - lii.dwTime
    return millis / 1000.0


# Capture the current time as the start time
start_time = datetime.now()

# Schedule the first notification immediately
send_drinking_water_notification()

# Schedule notifications every 1 minute (testing)
schedule.every(1).minutes.do(send_drinking_water_notification)

# Keep running the scheduled tasks
while True:
    schedule.run_pending()
    time.sleep(60)  # Check every minute
