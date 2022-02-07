# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

def distance_conversion(coordinate_1, coordinate_2):
    latitude_1, longitude_1 = coordinate_1
    latitude_2, longitude_2 = coordinate_2
    latitude_1 *= pi / 180
    latitude_2 *= pi / 180
    longitude_1 *= pi / 180
    longitude_2 *= pi / 180
    return 6378.7 * acos(sin(latitude_1) * sin(latitude_2) + cos(latitude_1)*cos(latitude_2)*cos(longitude_2-longitude_1))

def sorted_by_key(x, i, reverse=False):
    """For a list of lists/tuples, return list sorted by the ith
    component of the list/tuple, E.g.

    Sort on first entry of tuple:

      > sorted_by_key([(1, 2), (5, 1]), 0)
      >>> [(1, 2), (5, 1)]

    Sort on second entry of tuple:

      > sorted_by_key([(1, 2), (5, 1]), 1)
      >>> [(5, 1), (1, 2)]

    """

    # Sort by distance
    def key(element):
        return element[i]

    return sorted(x, key=key, reverse=reverse)

def stations_by_distance(stations, p):
    """This function creates a list of stations with the entries station name and distance
    using the haversine formula and coordinates defined in station.py and populated by 
    stationdata.py. It then sorts the list by distance using the sorted_by_key function in """
    
    list_of_stations = []
    
    for n in stations:
        distance = distance_conversion(n.coord , p)
        tuple_station = (n, distance)
        list_of_stations.append(tuple_station)
    
    return sorted(list_of_stations, key=lambda x: x[1])

from math import pi, sin, cos, acos

from sklearn.decomposition import DictionaryLearning

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

def rivers_with_station(stations):
    river_set = []
    for n in stations:
        river_set.append(n.river)
    
    return set(river_set)

