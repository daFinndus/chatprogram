import time
from threading import Thread

from event import MyEvent
from led import LED
from timer import MyTask, DatePicker


# Function to display how event's work
def work_with_events():
    my_five_events = MyEvent("set")
    input_value = input("Set input for event: ").lower()
    time.sleep(1)

    if input_value == my_five_events.key:
        my_five_events.set_event()
    my_five_events.join_threads()
    print("All threads are done.")


# Function to thread a LED blinking and time printing
def print_time_and_blink():
    LED_instance = LED(37)  # Setup connection between LED and Pi

    led_thread_0 = Thread(target=LED_instance.start_blink_light, args=())

    date_picker_1 = DatePicker("Thread_1_FAST")
    date_picker_2 = DatePicker("Thread_2_SLOW")

    timer_period_1 = 1
    timer_period_2 = 3

    my_task_1 = MyTask(timer_period_1, date_picker_1.thread_name, date_picker_1.print_time)
    my_task_2 = MyTask(timer_period_2, date_picker_2.thread_name, date_picker_2.print_time)

    led_thread_0.start()

    my_task_1.timer.start()
    my_task_2.timer.start()

    time.sleep(30)

    my_task_1.timer.cancel()
    my_task_2.timer.cancel()

    LED_instance.stop_blink_light()

    led_thread_0.join()


if __name__ == "__main__":
    pass
