#!/usr/bin/env python3
# Student ID: [120669221]
# Name: Prince Dungrani

def function1():
    global schoolName  # Modify the global variable 'schoolName'
    schoolName = 'SICT'
    print('print() in function1 on schoolName:', schoolName)

def function2():
    global schoolName  # Modify the global variable 'schoolName'
    schoolName = 'SSDO'
    print('print() in function2 on schoolName:', schoolName)

# Global variable
schoolName = 'Seneca'
print('print() in main on schoolName:', schoolName)
function1()
print('print() in main on schoolName:', schoolName)
function2()
print('print() in main on schoolName:', schoolName)
