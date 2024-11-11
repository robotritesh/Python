import time

def countdown(seconds):
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        print(f"{mins:02d}:{secs:02d}", end='\r')
        time.sleep(1)
        seconds -= 1
    print("Time's up!")

countdown(5)  # Countdown from 5 seconds
