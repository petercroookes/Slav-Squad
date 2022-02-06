# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""
from floodsystem.utils import sorted_by_key
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