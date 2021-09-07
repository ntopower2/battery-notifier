from plyer import notification
from time import sleep
import psutil


def battery_check(lower=30, upper=80):
    battery = psutil.sensors_battery()
    title = "Battery Notification"
    if battery.percent < lower and not battery.power_plugged:
        notification.notify(title=title, 
        message=f'Battery lower than 40% (real: {battery.percent}%), please connect charger!', 
        timeout=15)
    elif battery.percent > upper and battery.power_plugged:
        notification.notify(title=title, 
        message=f'Battery more than 80% (real: {battery.percent}%), please disconnect charger!', 
        timeout=15)
    return True

if __name__ == "__main__":
    while True:
        battery_check()
        sleep(120)
