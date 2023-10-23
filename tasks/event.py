from threading import Thread, Event, current_thread


# Class to display how events work
class MyEvent:
    def __init__(self, key):
        self.key = key
        self.event = Event()
        self.threads = []

        self.amount = 5

        # Generate certain amount of threads and adding them to our threads list
        for thread in range(self.amount):
            thread = Thread(target=self.runner)
            self.threads.append(thread)
            thread.start()

    def runner(self):
        name = current_thread().name
        print(f"{name} is waiting for an event.")
        self.event.wait()
        print(f"{name} found an event: '{self.key}'.")

    def set_event(self):
        self.event.set()

    def join_threads(self):
        for thread in self.threads:
            thread.join()
