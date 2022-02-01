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


def stations_next_to_river(stations):
    output = dict()
    for station in stations:
        if station.river in output:
            output[station.river].append(station.name)
        else:
            output[station.river] = [station.name]
    return output


def rivers_by_station_number(stations, N):
    output = dict()
    for station in stations:
        if station.river in output:
            output[station.river].append(station.name)
        else:
            output[station.river] = [station.name]
    rivers = []
    for station in stations:
        if station.river in rivers:
            pass
        else:
            rivers.append(station.river)
    river_numbers = []
    for river_name, numbers in output.items():
        tuple = (river_name, len(numbers))
        river_numbers.append(tuple)
    river_numbers = sorted(river_numbers, key = lambda x: x[1], reverse = True)
    river_N_numbers = river_numbers[:N]
    river_numbers = river_numbers[N:]
    for river in river_numbers:
        if river[1] == river_N_numbers[N-1][1] :
            river_N_numbers.append(river)
    return river_N_numbers

