# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""
<<<<<<< HEAD
from utils import sorted_by_key
from haversine import haversine, Unit


def stations_by_distance(stations, p):
    """This function creates a list of stations with the entries station name and distance
    using the haversine formula and coordinates defined in station.py and populated by 
    stationdata.py. It then sorts the list by distance using the sorted_by_key function in """
    
    list_of_stations = []
    
    for n in stations:
        distance = haversine(n.coord , p)
        tuple_station = (n.name, distance)
        list_of_stations.append(tuple_station)
    stations_sorted = sorted_by_key(list_of_stations, 0)
    return stations_sorted

def stations_within_radius(stations, centre, r):
    
    station_list = []

    for n in stations:
        
        radius = haversine(n.coord, centre)

        if r > radius:
            station_list.append(station)
        else:
            pass
    
    return station_list
=======
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

>>>>>>> 46be1bc8500b443e3dda8a6f9f5167995795a68f
