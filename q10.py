class Timestamp:
    """ Time and message for a timestamp. """

    def __init__(self, h, m, s, msg):
        """ (Timestamp, int, int, int, str) -> NoneType

        Precondition: 0 <= h <= 23 and 0 <= m <= 59 and 0 <= s <= 59

        Initialize the hour h, minute m, second s, and message msg associated
        with this Timestamp.

        >>> ts1 = Timestamp(14, 10, 42, 'Relax')
        >>> ts1.hour
        14
        >>> ts1.min
        10
        >>> ts1.sec
        42
        >>> ts1.msg
        'Relax'
        """
        self.hour = h
        self.min = m 
        self.sec = s 
        self.msg = msg 

    def time(self):
        """ (Timestamp) -> str

        Return a string representation of the time associated with this Timestamp.

        >>> ts1 = Timestamp(14, 9, 1, 'Relax')
        >>> ts1.time()
        '14:9:1'
        """
        x = str(self.hour) + ':' + str(self.min) + ':' + str(self.sec) 
        return x 

    def __eq__(self, other):
        """(Timestamp, Timestamp) -> bool
        Return whether this Timestamp has the same messages as other.

        >>> ts1 = Timestamp(12, 8, 3, 'Busy')
        >>> ts2 = Timestamp(12, 8, 4, 'Busy')
        >>> ts3 = Timestamp(12, 8, 3, 'Busy')
        >>> ts4 = Timestamp(12, 8, 3, 'Relax')
        >>> ts1 = ts2
        False
        >>> ts1 = ts3
        True 
        >>> ts1 = ts4
        False
        """
        return self.hour == other.hour and self.min == other.min and self.sec == other.sec and self.msg == other.msg 


class AlarmSchedule:
    """ Contains information about Timestamp objects in an alarm schedule. """

    def __init__(self):
        """ (AlarmSchedule) -> NoneType

        Initialize an AlarmSchedule with an empty list named schedule.

        >>> alarms = AlarmSchedule()
        >>> alarms.schedule
        []
        """
        self.schedule = []

    def add(self, tstamp):
        """ (AlarmSchedule, Timestamp) -> NoneType

        Modify schedule to add Timestamp tstamp, provided there is not an
        existing Timestamp with the same time.

        >>> alarms = AlarmSchedule()
        >>> alarms.add(Timestamp(14, 10, 42, 'Relax'))
        >>> alarms.add(Timestamp(14, 23, 39, 'Sigh'))
        >>> alarms.add(Timestamp(14, 10, 42, 'Burp'))
        >>> alarms.schedule[0].msg
        'Relax'
        >>> alarms.schedule[1].msg
        'Sigh'
        >>> len(alarms.schedule)
        2
        """
        for t in self.schedule:
            if t.time() == tstamp.time():
                tstamp_exist = True
                if not tstamp_exist:
                    self.schedule.append(tstamp)

if __name__ == '__main__':
    import doctest
    doctest.testmod