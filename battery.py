import time
from asyncio import sleep
import psutil
from pyttsx3 import speak

def battery():

    battery = psutil.sensors_battery()
    plugged = battery.power_plugged
    percent = int(battery.percent)
    demo = timeCalculator(battery.secsleft)
    if (plugged == True):
        if (percent == 100):
            speak("Unplugged the chrager, battry is full")
        elif percent >= 95:
            speak("After  few seconds  battery will be fully charged ")
    elif percent < 20:
        if percent > 10:
            speak("Battery is low ! Please plug the charger ")
            speak(f"battery work total{demo} ")
        elif percent <= 10:
            for i in range(100):
                print("Batter is low ! Please plug the charger")
                speak(f"battery work total{demo} ")
                sleep(3)

def timeCalculator(time):
        hour = time // 3600
        time %= 3600
        minutes = time // 60
        time %= 60
        seconds = time

        if hour <= 0 | minutes<=0:
            demo1 = (f"seconds{seconds}")
            return demo1
        elif hour <= 0:
            demo2 = (f"{minutes}minutes,{seconds}seconds")
            return demo2
        else:
            demo3 = (f"{hour}hours,{minutes}minutes,{seconds}seconds")
            return demo3

"""def batterycommand():
    battery = psutil.sensors_battery()
    demo = timeCalculator(battery.secsleft)
    speak(f"Battery charging {battery.percent}")
    speak(f"battery work total{demo} ")"""


def main():
    #Battery()
    while True:
        battery()
        m = 15*30
        time.sleep(m)
    #batterycommand()

if __name__ == "__main__":
    main()"""
