from unittest import TestCase
from minimal_lateness_scheduling import *


class TestMinimizeLateness(TestCase):
    def test_minimize_lateness(self):
        j1 = Job(time(hour=18), duration=timedelta(hours=4))
        j2 = Job(time(hour=12), duration=timedelta(hours=8))
        jobs =[j1, j2]
        schedule = minimize_lateness(jobs)

        self.assertTrue(schedule[0].deadline <= schedule[1].deadline)


