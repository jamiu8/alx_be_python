from datetime import datetime, timedelta, date

def display_current_datetime():
    current_date = datetime.now()
    print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))

days_to_add = int(input("Enter the number of days to add to the current date:" ))

def calculate_future_date():
    today = datetime.now()
    future_date = today + timedelta(days=days_to_add)
    print("Future date and time:", future_date.strftime("%Y-%m-%d"))

display_current_datetime()
calculate_future_date()
