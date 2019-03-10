"""
- Given: a set of n jobs to schedule for a resource {1, 2, 3, ..., n}.
  * job j: start time s(j), end time f(j)
- Output: max(subset of compatible jobs)
  * compatible job: jobs do not overlap
"""

from datetime import time


class Job:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __lt__(self, other)->bool:
        return self.end < other.end

    def __le__(self, other)->bool:
        return self.end <= other.end

    def __eq__(self, other)->bool:
        return self.end == other.end

    def __ne__(self, other)->bool:
        return self.end != other.end

    def __gt__(self, other)->bool:
        return self.end > other.end

    def __ge__(self, other)->bool:
        return self.end >= other.end

    def __str__(self):
        return ''.join((str(self.start), '--', str(self.end)))


def schedule_interval(jobs: list):
    compat_jobs = []
    jobs.sort()
    max_end_time = None
    for job in jobs:
        if max_end_time is None or job.start > max_end_time:
            compat_jobs.append(job)
            max_end_time = job.end
    return compat_jobs



