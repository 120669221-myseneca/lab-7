#!/usr/bin/env python3
# Student ID: 120669221
# Name: Prince Dungrani

class Time:
    """Simple object type for time of the day.
       Data attributes: hour, minute, second
       Function attributes: __init__, __str__, __repr__,
                            time_to_sec, format_time,
                            change_time, sum_times
    """
    def __init__(self, hour=12, minute=0, second=0):
        """Constructor to initialize time object."""
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        """Returns a formatted string representation of the time (HH:MM:SS)."""
        return f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'

    def __repr__(self):
        """Returns a developer-friendly representation of the time (HH.MM.SS)."""
        return f'{self.hour:02d}.{self.minute:02d}.{self.second:02d}'

    def format_time(self):
        """Returns a formatted string representation of the time (HH:MM:SS)."""
        return f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'

    def sum_times(self, t2):
        """Adds two Time objects and returns the sum as a new Time object."""
        total_seconds = self.time_to_sec() + t2.time_to_sec()
        return sec_to_time(total_seconds)

    def change_time(self, seconds):
        """Adjusts the time object by a given number of seconds."""
        total_seconds = self.time_to_sec() + seconds
        nt = sec_to_time(total_seconds)
        self.hour, self.minute, self.second = nt.hour, nt.minute, nt.second

    def time_to_sec(self):
        """Converts the time object to the total number of seconds."""
        total_minutes = self.hour * 60 + self.minute
        return total_minutes * 60 + self.second

    def valid_time(self):
        """Checks if the time attributes represent a valid time."""
        if self.hour < 0 or self.minute < 0 or self.second < 0:
            return False
        if self.hour >= 24 or self.minute >= 60 or self.second >= 60:
            return False
        return True

def sec_to_time(seconds):
    """Converts a total number of seconds into a Time object."""
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time
