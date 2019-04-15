import csv
from typing import List, Tuple
from get_closest_pair import get_closest_pair
import copy
import re

"""
@author: Fan Zhang
@date: April 14, 2019
@ref: https://docs.python.org/3/library/csv.html
"""


def get_location_coords(f_name: str)->List[Tuple[float, float]]:
    """
    Read the 4-5 columns of the csv file except the first row
    :param f_name: file name
    :return: a list of location coordinates: (Latitude, Longitude)
    """
    result_l = []
    with open(f_name, newline="") as file:
        reader = csv.reader(file)
        line_num = 0
        for row in reader:
            if line_num == 0:
                pass
            else:
                location_coord = (float(row[3]), float(row[4]))
                result_l.append(location_coord)
            line_num += 1
    return result_l


def get_chigago_location_coords(f_name: str)->List[Tuple[float, float]]:
    """
    Exclude radio station names i.e. "WONX-AM (Evanston)"
    :param f_name: file name
    :return: a list of location coordinates: (Latitude, Longitude)
    """
    result_l = []
    with open(f_name, newline="") as file:
        reader = csv.reader(file)
        line_num = 0
        for row in reader:
            name = row[1]
            if not re.search("[A-Z]+-[A-Z]+ ()", name):
                if line_num == 0:
                    pass
                else:
                    location_coord = (float(row[3]), float(row[4]))
                    result_l.append(location_coord)
            line_num += 1
    return result_l


def get_closest_location_pair_coord(location_l: list)-> Tuple:
    # sorted by latitude
    locations_x = copy.deepcopy(location_l)
    locations_x.sort(key=lambda location: location[0])
    # sorted by longitude
    locations_y = copy.deepcopy(location_l)
    locations_y.sort(key=lambda location: location[1])
    return get_closest_pair(locations_x, locations_y)


def get_location_pair_names(fname: str)->tuple:
    location_l = get_location_coords(fname)
    pair_coords = get_closest_location_pair_coord(location_l)
    coord1, coord2 = pair_coords[1]
    name1 = get_location_name(fname, coord1)
    name2 = get_location_name(fname, coord2)
    return name1, name2


def get_chigago_location_pair_names(fname: str)->tuple:
    location_l = get_chigago_location_coords(fname)
    pair_coords = get_closest_location_pair_coord(location_l)
    coord1, coord2 = pair_coords[1]
    name1 = get_location_name(fname, coord1)
    name2 = get_location_name(fname, coord2)
    return name1, name2


def get_location_name(fname: str, location_coord: tuple)->str:
    x = str(location_coord[0])
    y = str(location_coord[1])
    with open(fname) as file:
        reader = csv.reader(file)
        for row in reader:
            if (x, y) == (row[3], row[4]):
                return row[1]


if __name__ == "__main__":
    location_l = get_location_coords("minnesotaLocations.csv")
    pair_coords = get_closest_location_pair_coord(location_l)
    print(pair_coords)
    coord1, coord2 = pair_coords[1]
    name1 = get_location_name("minnesotaLocations.csv", coord1)
    name2 = get_location_name("minnesotaLocations.csv", coord2)
    print(name1, name2)

    names = get_location_pair_names("minnesotaLocations.csv")
    print(names)

