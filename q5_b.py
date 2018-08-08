import q5_a

def number_of_winners(qualifying_time, race_results):
    """ (str, file open for reading) -> int

    A valid time is a str with format 'h:m:s', with 0 <= int(h) <= 23,
    0 <= int(m) <= 59 and 0 <= int(s) <= 59.

    Precondition: qualifying_time is a valid time,
                  Each line in race_results contains a single valid time.

    Return the number of lines in race_results that contain a time that is
    below qualifying_time.
    """
    x = q5_a.convert_time_to_seconds(qualifying_time)
    #累加
    winners = 0
    for line in race_results:
        y = q5_a.convert_time_to_seconds(line.strip())
        if y < x:
            winners = winners + 1
    return winners
    
if __name__ == '__main__':
    twm = open('twm_times.txt', 'r')
    print('Number of prize winners:', number_of_winners('3:20:14', twm))
    twm.close()