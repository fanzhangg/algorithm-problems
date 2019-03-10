from unittest import TestCase
from interval_scheduling import *
from datetime import time


class TestScheduleInterval(TestCase):
    def test_schedule_interval(self):
        s2 = time(hour=9, minute=35)
        e2 = time(hour=11, minute=20)
        j2 = Job(s2, e2)

        s3 = time(hour=11)
        e3 = time(hour=12, minute=30)
        j3 = Job(s3, e3)

        s5 = time(hour=13, minute=20)
        e5 = time(hour=13, minute=50)
        j5 = Job(s5, e5)

        s4 = time(hour=12)
        e4 = time(hour=13, minute=30)
        j4 = Job(s4, e4)

        s1 = time(hour=9)
        e1 = time(hour=10)
        j1 = Job(s1, e1)

        jobs = [j1, j2, j3, j4, j5]

        for j in schedule_interval(jobs):
            print(j)
