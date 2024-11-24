#!/usr/bin/env python3
# Student ID: [120669221]
# name: Prince Dungrani
class Time:
    """Simple object type for time of the day.
    data attributes: hour, minute, second
    """
    def __init__(self,hour=12,minute=0,second=0):
        """constructor for time object""" 
        self.hour = hour
        self.minute = minute
        self.second = second

def format_time(t):
    """Return time object (t) as a formatted string"""
    return f'{t.hour:02d}:{t.minute:02d}:{t.second:02d}'

def sum_times(t1, t2):
    """Adds 2 objts and returns desired sum."""
    sum = Time(0, 0, 0)
    sum.hour = t1.hour + t2.hour
    sum.minute = t1.minute + t2.minute
    sum.second = t1.second + t2.second

    # seconds to minutes
    if sum.second >= 60:
        sum.minute += sum.second // 60
        sum.second = sum.second % 60

    # if total minutes exceeds 60, converts to hours
    if sum.minute >= 60:
        sum.hour += sum.minute // 60
        sum.minute = sum.minute % 60

    return sum


def change_time(time, seconds):
    """Modify the time object by adding/subtracting seconds."""
    time.second += seconds

    # sets seconds within 0-59 range
    while time.second < 0:
        time.second += 60
        time.minute -= 1
    while time.second >= 60:
        time.second -= 60
        time.minute += 1

    # sets minutes within 0-59 range
    while time.minute < 0:
        time.minute += 60
        time.hour -= 1
    while time.minute >= 60:
        time.minute -= 60
        time.hour += 1

    # sets hours to fit within 0-23 range
    while time.hour < 0:
        time.hour += 24
    while time.hour >= 24:
        time.hour -= 24

    return None



def valid_time(t):
    """check for the validity of the time object attributes:
        24 > hour > 0, 60 > minute > 0, 60 > second > 0 """
    if t.hour < 0 or t.minute < 0 or t.second < 0:
        return False
    if t.minute >= 60 or t.second >= 60 or t.hour >= 24:
        return False
    return True
