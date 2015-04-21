import datetime
import pytz

fmt = "%H:%M, %m-%d-%Y %Z%z"

Timezones = [pytz.timezone('US/Pacific'),
             pytz.timezone('US/Eastern'),
             pytz.timezone('Europe/Paris'),
             pytz.timezone('Australia/Melbourne'),
             pytz.timezone('Asia/Singapore'),
             pytz.timezone('UTC')]
while True:
    time_input = input("Enter the time you want to convert(MM/DD/YYYY HH:MM): ")
    try:
        local_time = datetime.datetime.strptime(time_input, '%m/%d/%Y %H:%M')
    except:
        print("Please enter a valid input!!!")
    else:
        local_time = pytz.timezone('Asia/Calcutta').localize(local_time)
        utc_time = local_time.astimezone(pytz.utc)
        conv_times = []
        print("Time across different Timezones: ")
        for i, timezone in enumerate(Timezones, start=1):
            conv_times.append(utc_time.astimezone(timezone))
            print("{}) {}: {}".format(i, timezone, datetime.datetime.strftime(conv_times[i-1],fmt)))
        break
    
