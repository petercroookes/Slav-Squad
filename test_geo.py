from numpy import integer
# from sympy import N
from floodsystem.stationdata import *
from floodsystem.geo import *


def test_distance_conversion():
    # Check that the function correctly calculates the distance between these two coordinates.
    assert round(distance_conversion((0.1,0.2),(0.5,0.6)),1) == 63

def test_stations_by_distance():
    # Create a list of stations using real data.
    stations = build_station_list()
    # Run the function on real data, which creates a list of stations and their distance from a particular coordinate.
    distance_list = stations_by_distance(stations, (52.2053, 0.1218))
    # Check that the function creates a list that is sorted alphabetically.
    assert sorted(distance_list, key=lambda x: x[1])==distance_list
    # Check that the distance of each station in this list is correct.
    for station in distance_list:
        assert station[1]==distance_conversion(station[0].coord, (52.2053, 0.1218))
    
def test_stations_within_radius():
    # Create a list of stations using real data.
    stations = build_station_list()
    # Run the function on real data, which shoud produce a list of stations within a given radius frm a given point.
    radius_list = stations_within_radius(stations, (52.2053, 0.1218), 10)
    # For each station in this list, check that their distance from the given point is less than or equal to the given radius.
    for station in radius_list:
        assert distance_conversion(station.coord, (52.2053, 0.1218)) <= 10

def test_stations_next_to_river():
    # Create a list of stations using real data.
    stations = build_station_list()
    river_dict = stations_next_to_river(stations)
    # Checks that the function produces a dictionary.
    assert isinstance(river_dict, dict) == True

def test_rivers_with_station():
    # Create a station with test characteristics.
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    typical_range = (1.0)
    town = "MyTown"

    # Create test river values.
    RiverA = "RiverA"
    RiverB = "RiverB"

    # Create test station classes.
    Station1 = MonitoringStation(s_id, m_id, label, coord, typical_range, RiverA, town)
    Station2 = MonitoringStation(s_id, m_id, label, coord, typical_range, RiverB, town)
    Station3 = MonitoringStation(s_id, m_id, label, coord, typical_range, RiverA, town)

    # Create list from test stations.
    stations_examples = [Station1, Station2, Station3]

    # Check that the function does not produce a list including the same river multiple tiems (i.e. it is a set)
    assert isinstance(rivers_with_station(stations_examples), set) == True

def test_rivers_by_station_number():
    # Create a list of stations using real data. 
    stations = build_station_list()

    N = 9
    output = stations_next_to_river(stations)
    assert type(output) == type(dict())
    output = stations_next_to_river(stations)
    river_numbers = []
    for river_name, numbers in output.items():
        river_tuple = (river_name, len(numbers))
        assert type(river_tuple) == type(tuple())
        assert len(river_tuple) == 2
        river_numbers.append(river_tuple)
    assert len(river_numbers) == len(output)
    river_numbers = sorted(river_numbers, key = lambda x: x[1], reverse = True)
    assert river_numbers[0][1] > river_numbers[-1][1]
    river_N_numbers = river_numbers[:N]
    assert len(river_N_numbers) == N
    river_numbers = river_numbers[N:]
    assert type(river_numbers[0]) == type(tuple())
    assert type(river_N_numbers[-1]) == type(tuple())
    assert type(river_numbers[0][1]) == type(int())
    assert type(river_N_numbers[-1][1]) == type(int())
    for river in river_numbers:
        if river[1] == river_N_numbers[N-1][1]:
            river_N_numbers.append(river)
    return river_N_numbers
test_rivers_by_station_number()
