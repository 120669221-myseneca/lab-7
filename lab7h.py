#!/usr/bin/env python3
# Student ID: [120669221]
# anme: prince Dungrani

def function1():
    print('print() in function1 on schoolName:', schoolName)

def function2():
    print('print() in function2 on schoolName:', schoolName)

# Global variable
schoolName = 'Seneca College'
print('print() in main on schoolName:', schoolName)
function1()
print('print() in main on schoolName:', schoolName)
function2()
print('print() in main on schoolName:', schoolName)