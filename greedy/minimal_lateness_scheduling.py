"""
- Given:
  - A single resource
  - A set of $n$ requests
    - Deadline $d(i)$
    - Time duration $t(i)$

- Output: a schedule that satisfies all requests and minimizes max_i (l(i))

  - l(i): lateness of job i

"""
from datetime import time, timedelta, datetime, date


class Job:
    def __init__(self, deadline: time, duration: timedelta):
        self.deadline = datetime.combine(date.today(), deadline)
        self.duration = duration
        self.start = None
        self.end = None

    def __lt__(self, other) -> bool:
        return self.deadline < other.deadline

    def __le__(self, other) -> bool:
        return self.deadline <= other.deadline

    def __eq__(self, other) -> bool:
        return self.deadline == other.deadline

    def __ne__(self, other) -> bool:
        return self.deadline != other.deadline

    def __gt__(self, other) -> bool:
        return self.deadline > other.deadline

    def __ge__(self, other) -> bool:
        return self.deadline >= other.deadline

    def __str__(self):
        return ''.join((str(self.start.time()), "--", str(self.duration), "-->", str(self.end.time())))


def minimize_lateness(jobs: list)->list:
    """Select jobs with earlier deadline"""
    selected_jobs = []
    jobs.sort()
    start = datetime.combine(date.today(), time(hour=8))
    for job in jobs:
        job.start = start
        job.end = start + job.duration
        start = job.end
        selected_jobs.append(job)
    return selected_jobs
