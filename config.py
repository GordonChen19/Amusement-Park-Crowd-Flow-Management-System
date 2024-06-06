from datetime import datetime

opening_time = "08:30" 
closing_time = "21:30"

def get_minute_difference(time1, time2):
    # Define the time format
    time_format = "%H:%M"
    
    # Convert the string times to datetime objects
    t1 = datetime.strptime(time1, time_format)
    t2 = datetime.strptime(time2, time_format)
    
    # Calculate the difference
    delta = t1 - t2 if t1 > t2 else t2 - t1
    
    minutes = delta.total_seconds() // 60
    return int(minutes) 

operating_hours = int(get_minute_difference(opening_time, closing_time)/60)
operating_minutes = operating_hours * 60


##########################

# Kairos Parameters

fast_pass_intervals = 10
max_fast_passes_per_slot = 8

##########################
