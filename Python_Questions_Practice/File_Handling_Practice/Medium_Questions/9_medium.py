# Write a function that logs user activity (timestamped) into a log file each time it is called.
from datetime import datetime

def log_user_activity(message):
    # Get current timestamp
    timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")

     # Create the full log entry
    log_entry = f"{timestamp} {message}\n"

    # Append the log to the file
    with open("Text files/activity.log", "a") as file:
        file.write(log_entry)

log_user_activity(input("Enter your message: "))