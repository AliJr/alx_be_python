from datetime import datetime, timedelta



# function to display current day and time in YYYY-MM-DD HH:MM:SS 
def display_current_datetime():
    current_date = datetime.now()
    print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))
    return current_date

def calculate_future_date(days_to_add,current_date):
    future_date = current_date + timedelta(days=days_to_add)
    print(f"Future Date: {future_date.strftime("%Y-%m-%d")}")
    
    return future_date

current_date = display_current_datetime()
calculate_future_date(int(input("Enter the number of days to add to the current date: ")),current_date)