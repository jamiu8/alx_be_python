from datetime import datetime, timedelta, date

def display_current_datetime():
    current_date = datetime.now()
    print(current_date)

days_to_add = float(input("days to add: "))

def calculate_future_date():
    today = date.today()
    future_date = str(today + timedelta(days= days_to_add))
    parsed = datetime.strptime(future_date, '%Y-%m-%d')
    print(parsed)

display_current_datetime()
calculate_future_date()