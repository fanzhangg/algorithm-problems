from unittest import TestCase

from hot_potato import *


class TestGetLast(TestCase):
    def test_get_last(self):
        names = ['Bill', 'David', 'Susan', 'Jane', 'Kent', 'Brad']
        last_name = get_last(names, 7)
        self.assertEqual('Susan', last_name)

    def test_num_qt_len_names(self):
        pass


class TestVisualizer(TestCase):
    def test_print_circle(self):
        names = ['Bill', 'David', 'Susan', 'Jane', 'Kent', 'Brad', "Piggy", "Frank", "Jack", "Victor", "Lollipop",
                 "John", "Alexandra", "Spark", "Toto", "Godard", "Paul", "Pig", "Dog", "Grey"]
        visual = Visualizer()
        circle_str = visual.circle_q_to_str(names, "John")
        print(circle_str)

    def test_print_animation(self):
        names = ['Bill', 'David', 'Susan', 'Jane', 'Kent', 'Brad']
        v = Visualizer()
        v.print_animation(names, 7)
