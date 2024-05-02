class Timer:
    def __init__(self):
        #
        # Write code here
        #
        pass

    def __str__(self):
        #
        # Write code here
        #
        pass

    def next_second(self):
        #
        # Write code here
        #
        pass

    def prev_second(self):
        #
        # Write code here
        #
        pass

def set_time_to_string(seconds, minutes, hours):
    """Function to read in three integer values and convert to a string in the form 
    'hh:mm:ss'\nInputs:\n\tseconds (int)\n\tminutes (int)\n\t(hours)\nOutput:\n\ttime_string (str)
    """

    # Convert each of the integers to strings - add zeros onto front if needed
    seconds_string = time_denom_to_string(seconds)
    minutes_string = time_denom_to_string(minutes)
    hours_string = time_denom_to_string(hours)

    return f"{hours_string}:{minutes_string}:{seconds_string}"

def time_denom_to_string(time):
    """Function to read in a single integer as a time denomination and convert to string (with a leading zero if needed)
    \nInput:\n\ttime (int)
    \nOutput:\n\ttime_string (str)
    """

    if time < 10: return "0" + str(time)
    else: return str(time)
"""
timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)
"""

#Testing time to string and time denom funcitons

print(time_denom_to_string(30))
print(time_denom_to_string(5))

print(set_time_to_string(30, 30, 10))