from plyer import notification
import time

if __name__ == '__main__':
    while True:
        notification.notify(
            title = "Take Rest", 
            message="It will help you improve your performance.", 
            app_icon="H:/Study Material/Projects/Python Projects/Desktop Notifier/rest.ico", 
            timeout=5)
        time.sleep(60*60) #60secX60sec

#run the program : pythonw desktopnotifier.py, and you can stop it after ending task in Task Manager
