# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

def distance_conversion(coordinate_1, coordinate_2):
    # Divides coordinate into latitude and longitude
    # Converts from degrees to radians
    latitude_1, longitude_1 = coordinate_1
    latitude_2, longitude_2 = coordinate_2

    # Converts from degrees to radians
    latitude_1 *= pi / 180
    latitude_2 *= pi / 180
    longitude_1 *= pi / 180
    longitude_2 *= pi / 180

    # Returns haversine formula computation of coordinates
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
    
    # Create empty list of stations
    list_of_stations = []
    
    # For each river:
    for n in stations:
        # Computes distance between coordinates and given coordinate river.
        distance = distance_conversion(n.coord , p)

        # Creates a tuple for each station and its corresponding distance, and append it to the list.
        tuple_station = (n, distance)
        list_of_stations.append(tuple_station)

    # Return sorted list of stations by distance in ascending order
    return sorted(list_of_stations, key=lambda x: x[1])

from math import pi, sin, cos, acos

# from sklearn.decomposition import DictionaryLearning





def stations_within_radius(stations, centre, r):
    # Creat empty list
    output = []

    # For each station, compute radius using station coordinatines and a given centre, and if the station is within
    # a specified radius, add the station to the list.
    for station in stations:
        radius = distance_conversion(station.coord, centre)
        if radius < r:
            output.append(station)

    return output


def stations_next_to_river(stations):
    # Create empty dictionary
    output = dict()

    # If the river is already in the dictionary, then add station name to that key. Else, if river
    # is not already in dictionary, add river to dictionary and assign station to river key.
    for station in stations:
        if station.river in output:
            output[station.river].append(station.name)
        else:
            output[station.river] = [station.name]
    return output


def rivers_by_station_number(stations, N):
    
    output = stations_next_to_river(stations)
    river_numbers = []
    # Create a list of tuples where each tuple contains a river name and the number of stations by that river.
    for river_name, numbers in output.items():
        tuple = (river_name, len(numbers))
        river_numbers.append(tuple)
    
    # This then sorts the rivers in descending order of number of stations
    river_numbers = sorted(river_numbers, key = lambda x: x[1], reverse = True)

    #This then moves the N rivers with the most stations to another list and removes them from the original list
    river_N_numbers = river_numbers[:N]
    river_numbers = river_numbers[N:]
    
    #This then checks to see if any of the rivers that weren't in the 1st N items have the same number of stations as the smallest in the N largest list, and if they do, it adds them to that list
    for river in river_numbers:
        if river[1] == river_N_numbers[N-1][1] :
            river_N_numbers.append(river)
    return river_N_numbers


def rivers_with_station(stations):

    # Create empty list
    river_set = []

    # For each station, add its river to the list (this will have duplicate entries)
    for n in stations:
        river_set.append(n.river)
    
    # Convert the list into a set, eliminating the duplicates
    return set(river_set)
