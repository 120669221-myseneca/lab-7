#!/usr/bin/env python3
# Student ID: [120669221]
# name : Prince Dungrani
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
    '''Areturns a new time objt'''
    total_seconds = time_to_sec(t1) + time_to_sec(t2)
    return sec_to_time(total_seconds)



def change_time(time, seconds):
    '''adding or subtracting seconds'''
    total_seconds = time_to_sec(time) + seconds
    while total_seconds < 0:
        total_seconds += 24 * 3600  
    total_seconds %= 24 * 3600  
    updated_time = sec_to_time(total_seconds)
    time.hour, time.minute, time.second = updated_time.hour, updated_time.minute, updated_time.second
    return None


def time_to_sec(time):
    '''from time objt to integer (seconds)'''
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds

def sec_to_time(seconds):
    '''output of time_to_sec function to hour minute second frame'''
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time


def valid_time(t):
    """check for the validity of the time object attributes:
        24 > hour > 0, 60 > minute > 0, 60 > second > 0 """
    if t.hour < 0 or t.minute < 0 or t.second < 0:
        return False
    if t.minute >= 60 or t.second >= 60 or t.hour >= 24:
        return False
    return True
