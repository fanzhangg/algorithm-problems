"""
Simulate the behavior of the printing queue.
- Printing task is placed in a queue to be processed in a first-come first-served manner.
- If the printer cannot handle a certain amount of work, the student will be waiting too long.

Problem:
Input:
- n printing tasks, and each task has a certain length of pages.
- The printer can process 20 pages/min in draft quality, 5 pages/min in better quality.
Output: the best page rate

Solution:
- printing task
  - pages == a random number between 1 and 20
- printer
- printQueue

- Add to a waiting list after submitting printing tasks.
- After complete a task, check if exist a remaining tasks.
- Average amount of waiting time = average amount of time a task waits in the queue

Main Simulation:
- Create a queue of print tasks. When a print task arrives, give a timestamp
- For each second `current_sec`:
  - If a new print task get created:
    - Queue, time_stamp = current_second
  - If the printer is not busy and a task is waiting
    - Remove the next task from the print queue & assign it to the printer
    - Waiting time: current_sec - timestamp
    - Appending the waiting time for that task to a list for later processing
    - Get the required time based on the number of pages
  - The printer does 1 sec of printing, - 1 second from the time required for that task
  - If the task has been completed(time required = 0), the printer is not busy
- After the simulation, get the average waiting time
"""
import random

from my_queue import Queue


class Printer(object):
    def __init__(self, ppm: int):
        """
        :param ppm: page per minute
        """
        self.page_rate = ppm
        self.current_task = None
        self.time_remaining = 0

    def tick(self):
        """
        Decrement the internal timer and sets the printer to idle if the task is completed
        """
        if self.current_task:
            if self.time_remaining > 0:
                self.time_remaining -= 1
            else:
                self.current_task = None

    def is_busy(self) -> bool:
        if self.current_task:
            return True
        else:
            return False

    def start_next(self, new_task):
        self.current_task = new_task
        self.time_remaining = new_task.pages * 60 / self.page_rate


class RandomTask(object):
    def __init__(self, time: int):
        """
        A task with a random pages between 1 and 20
        :param time: represent the time that task was created & placed in the printer queue
        :return: average waiting time, the number of print tasks remaining in queue
        """
        self.time_stamp = time
        self.pages = random.randrange(1, 21)

    def get_wait_time(self, current_time) -> int:
        return current_time - self.time_stamp


def simulate(num_seconds, pages_per_minute):
    printer = Printer(pages_per_minute)
    print_queue = Queue()
    waiting_times = []

    for curr_sec in range(num_seconds):
        if is_create_new_print_task():
            task = RandomTask(curr_sec)
            print_queue.put(task)

        if (not printer.is_busy()) and (not print_queue.empty()):
            next_task = print_queue.get()
            waiting_times.append(next_task.get_wait_time(curr_sec))
            printer.start_next(next_task)
        printer.tick()
    avg_wait_time = sum(waiting_times) / len(waiting_times)
    return avg_wait_time, print_queue.size()


def is_create_new_print_task() -> bool:
    """
    :return: True if a new printing task has been created
    """
    # Print tasks arrive once every 180 seconds, create a new task when time == 180
    sec = random.randrange(1, 181)
    if sec == 180:
        return True
    else:
        return False


if __name__ == "__main__":
    wait_time_sum = 0
    count = 0
    for i in range(10):
        result = simulate(3600, 10)
        print(f"Average wait time: {result[0]}   Remaining task: {result[1]}")
        wait_time_sum += result[0]
        count += 1
    print(f"Total average wait time:{wait_time_sum / count}")
