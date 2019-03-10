"""
given:
  - a line segment [0, l]
  - n Potential rest stops
output:
  - Minimize the number of stops
  - l(s_{i+1}) - l(s_{i}) \leq 50
"""


class Stop:
    def __init__(self, index: int, position: int):
        self.index = index
        self.position = position

    def __lt__(self, other):
        return self.position < other.position

    def __str__(self):
        return "".join(("stop", str(self.index), ": ", str(self.position)))


def schedule_stops(stops: list, l: int)->list:
    # sort the stops by increasing distance from the start
    #  sort() uses only < comparison between items
    stops.sort()
    last_selected_stop_pos = 0
    schedule = []
    pre_stop = Stop(0, 0)
    index = 0

    for stop in stops:
        if stop.position - pre_stop.position > 50:
            return []
        if stop.position - last_selected_stop_pos > 50:
            schedule.append(pre_stop)
            last_selected_stop_pos = pre_stop.position
        # if the stop is the end of the list, test if l - pos(s) <= 50
        if index == len(stops) - 1:
            if l - stop.position > 50:
                return []
            else:
                schedule.append(stop)
        pre_stop = stop
        index += 1
    return schedule


