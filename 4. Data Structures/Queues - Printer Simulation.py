from pythonds3 import Queue
from random import randrange

class Printer:
    def __init__(self, ppm):
        self.page_rate = ppm
        self.current_task = None
        self.time_remaining = 0

    def tick(self):
        if self.current_task is not None:
            self.time_remaining -= 1
            if self.time_remaining <= 0:
                self.current_task = None

    def busy(self):
        return self.current_task is not None

    def start_next(self, new_task):
        self.current_task = new_task
        self.time_remaining = new_task.get_pages() * 60 / self.page_rate

class Task:
    def __init__(self, time):
        self.timestamp = time
        self.pages = randrange(1, average_prints())

    def get_stamp(self):
        return self.timestamp

    def get_pages(self):
        return self.pages

    def wait_time(self, current_time):
        return current_time - self.timestamp

def simulation(num_seconds, pages_per_minute):
    lab_printer = Printer(pages_per_minute)
    wait_times = []
    task_queue = Queue()
    for current_second in range(num_seconds):
        if set_new_task():
            new_task = Task(current_second)
            task_queue.enqueue(new_task)

        if (not lab_printer.busy()) and (not task_queue.is_empty()):
            next_task = task_queue.dequeue()
            wait_times.append(next_task.wait_time(current_second))
            lab_printer.start_next(next_task)

        lab_printer.tick()

    average_wait = sum(wait_times) / len(wait_times)

    print(f"Average Wait {average_wait:6.2f} secs" + f"{task_queue.size():3d} tasks remaining.")

def set_new_task():
    num = randrange(1, 181)
    return num == 180

def average_prints():
    return num_students * average_tasks

num_students = 5
average_tasks = 5
for i in range(10):
    simulation(3600, 5)

