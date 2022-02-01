# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""
#from .utils import sorted_by_key  # noqa*
from math import pi, sin, cos, acos
def distance_conversion(coordinate_1, coordinate_2):
    latitude_1, longitude_1 = coordinate_1
    latitude_2, longitude_2 = coordinate_2
    latitude_1 *= pi / 180
    latitude_2 *= pi / 180
    longitude_1 *= pi / 180
    longitude_2 *= pi / 180
    return 6378.7 * acos(sin(latitude_1) * sin(latitude_2) + cos(latitude_1)*cos(latitude_2)*cos(longitude_2-longitude_1))
def stations_within_radius(stations, centre, r):
    output = []
    for station in stations:
        radius = distance_conversion(station.coord, centre)
        if radius < r:
            output.append(station)
    return output