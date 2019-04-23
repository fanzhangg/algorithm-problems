from unittest import TestCase
from weighted_interval_scheduling import Job, get_last_compatible_job, dynamic_wis as wis


class TestWeightedIntervalScheduling(TestCase):
    def test_get_last_compatible_job(self):
        jobs = [Job(1, 4, 5), Job(3, 5, 3), Job(0, 6, 4), Job(4, 7, 4), Job(3, 8, 5),
                Job(5, 9, 7), Job(6, 10, 5), Job(8, 11, 7)]
        for i in range(len(jobs)):
            last_job = get_last_compatible_job(jobs, i)
            print(last_job)

    def test_wis(self):
        jobs = [Job(1, 4, 5), Job(3, 5, 3), Job(0, 6, 4), Job(4, 7, 4), Job(3, 8, 5),
                Job(5, 9, 7), Job(6, 10, 5), Job(8, 11, 7)]
        print(wis(jobs))
        # expected: Job(1, 4, 5), Job(4, 7, 4), Job(8, 11, 7)]

    def test_solution(self):
        jobs = [Job(1, 4, 5), Job(3, 5, 3), Job(0, 6, 4), Job(4, 7, 4), Job(3, 8, 5),
                Job(5, 9, 7), Job(6, 10, 5), Job(8, 11, 7)]
        self.assertEqual((16, [8, 4, 1]), wis(jobs))
        # j   | 0  1  2  3  4  5  6  7  8
        # ------------------------------
        # P   | /  /  /  /  0  /  1  2  4
        # OPT | 0  5  5  5  9  9 12 12 16
        # job | /  5  3  4  4  5  7  5  7
