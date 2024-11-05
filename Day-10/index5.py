from datetime import datetime, timedelta

# Current date and time
now = datetime.now()
print("Current Date & Time:", now)

# Date calculations
tomorrow = now + timedelta(days=1)
print("Tomorrow's Date:", tomorrow.date())

# Format datetime
formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted Date & Time:", formatted_date)
