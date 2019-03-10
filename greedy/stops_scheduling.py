"""
given:
  - a line segment [0, l]
  - n Potential rest stops
output:
  - Minimize the number of stops
  - l(s_{i+1}) - l(s_{i}) \leq 50
"""

__about__ = """
The Macalester track team has decided to host a marathon that runs down Grand Avenue for the faculty, staff and students
to participate in. Given your algorithm’s professor’s propensity to eat burritos in class, you are a little worried that
some of the faculty won’t make it unless you have numerous rest (and food) stops along the way. You’ve talked to the 
businesses along Grand Avenue and compiled a list of n potential rest stops along the street, with the geographic 
location of each such stop (some businesses did not like the idea of sweaty professors resting outside of them). 
Assume that Grand Avenue is a line segment [0, l] of length l meters. For simplicity, assume a rest stop has zero width; 
each location is just a point, rather than an interval on the line.)

According to your observations of how often your professors need to eat, you consider a section of the course properly 
covered if there is a rest stop within 50 meters of it (inclusive). So a single rest stop can cover 100 meters 
(if placed directly in the center of that 100 meters). Since the track team is rather small, and you need to man all 
the rest stops, you want to find a way to cover the entire course by opening as few rest stops as possible. Give an 
algorithm that places as few rest stops as possible, while covering the entire length of the course, or (correctly) 
reports that covering the entire length of the street is not possible given the available rest stops 
provided by the businesses.
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


