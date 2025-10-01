import datetime

def display_current_datetime():
    current_date = datetime.datetime.now()
    return current_date.strftime("%Y-%m-%d %H:%M:%S")

def calculate_future_date(number_of_days):
    current_date = datetime.datetime.now()
    future_date = current_date + datetime.timedelta(days=number_of_days)
    return future_date.strftime("%Y-%m-%d")

def main():
    print("Current date and time:", display_current_datetime())
    days = int(input("Enter number of days to add: "))
    print("Future date is:", calculate_future_date(days))

if __name__ == "__main__":
    main()
