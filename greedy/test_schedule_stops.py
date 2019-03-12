from unittest import TestCase
from stops_scheduling import *
import unittest


class TestScheduleStops(TestCase):
    def test_schedule_stops(self):
        stops = [Stop(2, 50), Stop(1, 20),  Stop(3, 90), Stop(6, 150),  Stop(4, 110), Stop(5, 140), Stop(7, 170)]
        schedule = schedule_stops(stops, 200)
        self.assertEqual([s.index for s in schedule], [2, 6])

    def test_first_stops_start_distance_gt_50(self):
        stops = [Stop(1, 100), Stop(2, 120)]
        schedule = schedule_stops(stops, 130)
        self.assertEqual([], schedule)

    def test_last_stop_end_distance_gt_50(self):
        stops = [Stop(1, 20), Stop(2, 40)]
        schedule = schedule_stops(stops, 100)
        self.assertEqual([], schedule)

    def test_adjacent_stops_gt_100(self):
        stops = [Stop(1, 20), Stop(2, 200)]
        schedule = schedule_stops(stops, 200)
        self.assertEqual([], schedule)


if __name__ == "__main__":
    unittest.main()
