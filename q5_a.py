def convert_time_to_seconds(time_as_str: str) -> int:
    """ 
    Precondition: time_as_str is a str in the format 'h:m:s', with
    0 <= int(h) <= 23 and 0 <= int(m) <= 59 and 0 <= int(s) <= 59

    Return the number of seconds in time_as_str.

    >>> convert_time_to_seconds('1:10:25')
    4225
    """
    time = time_as_str.split(':')
    h = int(time[0])
    m = int(time[1])
    s = int(time[2])
    seconds = h * 3600 + m * 60 + s 
    return seconds

if __name__ == '__main__':
    x = convert_time_to_seconds('1:10:25')
    print(x)
    
    