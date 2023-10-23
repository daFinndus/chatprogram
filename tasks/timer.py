from threading import Timer
import time


# Class to execute certain task after certain time with the timer module
class MyTask:
    def __init__(self, timer_period, name, function):
        self.timer_period = timer_period
        self.name = name
        self.function = function
        self.timer = Timer(self.timer_period, self.handle_function)  # Handle function after certain time

    # Function to handle a certain function and then restart the timer
    def handle_function(self):
        self.function()  # Execute function
        self.timer = Timer(self.timer_period, self.handle_function)  # Reset the timer to handle the function again
        self.timer.start()  # Start the timer


# This class is used to check which thread works at which time
class DatePicker:
    def __init__(self, name):
        self.thread_name = name

    # Function to print the threadname and time
    def print_time(self):
        print(f"'{self.thread_name}': {time.ctime(time.time())}")
