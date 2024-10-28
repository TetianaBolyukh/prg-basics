###
# Define a function time_string(hours, minutes, time_format) that, 
# given the number of hours (0..23) and the number of minutes (0..59), 
# returns a string specifying the time in the given format 
# ('24' for 24-hour time and '12' for 12-hour time)
#
def time_string(hours, minutes, time_format):
    if time_format == 24:
        return f'{hours:02}:{minutes:02}'
    elif time_format == '12':
        if hours >= 12:
            period = 'pm'
        else:
            hours = hours - 12
            period = 'am'
        return f'{hours}:{minutes}{period}'
    time_string(15, 38, 24)