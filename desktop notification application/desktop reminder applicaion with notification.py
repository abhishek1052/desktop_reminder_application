import time
from plyer import notification as no

if __name__ == "__main__":
    while(True):
        no.notify(

            title="Please drink Water",
            message="Drinking 2.3 Liter of water is essential for your health",
            timeout=5
        )
        time.sleep(6)
