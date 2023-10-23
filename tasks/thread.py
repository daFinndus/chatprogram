from threading import Thread

import time


# Class to display how threads work
class MyThread(Thread):
    def __init__(self, thread_id, name, delay_time):
        Thread.__init__(self)
        self.thread_id = thread_id
        self.name = name
        self.delay_time = delay_time

    # Function run the another function
    def run(self):
        print(f"Starting thread '{self.name}'.")
        self.print_time(5)
        print(f"Stopping thread '{self.name}'.")

    # Function to print the threadname and time with a certain delay
    def print_time(self, counter):
        while counter:
            time.sleep(self.delay_time)
            print(f"'{self.name}': {time.ctime(time.time())}")
            counter -= 1
