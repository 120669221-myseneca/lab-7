#!/usr/bin/env python3
# Student ID: [120669221]
# name: Prince Dungrani

def function1():
    # Local variable 'a' in function1
    a = 'object_function1'
    print('print() call in function1 on a:', a)

def function2():
    # Local variable 'a' in function2
    a = 'function2_object'
    print('print() call in function2 on a:', a)

# Global variable 'a' in main
a = 'object_in_main'
print('print() call in main on a:', a)
function1()
print('print() call in main on a:', a)
function2()
print('print() call in main on a:', a)
