from numpy import integer
from sympy import N
from floodsystem.stationdata import *
from floodsystem.geo import *


def test_distance_conversion():
    assert round(distance_conversion((0.1,0.2),(0.5,0.6)),1) == 63

def test_stations_by_distance():
    stations = build_station_list()
    distance_list = stations_by_distance(stations, (52.2053, 0.1218))
    assert sorted(distance_list, key=lambda x: x[1])==distance_list
    for station in distance_list:
        assert station[1]==distance_conversion(station[0].coord, (52.2053, 0.1218))
    
def test_stations_within_radius():
    stations = build_station_list()
    radius_list = stations_within_radius(stations, (52.2053, 0.1218), 10)
    for station in radius_list:
        assert distance_conversion(station.coord, (52.2053, 0.1218)) <= 10

def test_stations_next_to_river():
    stations = build_station_list()
    river_dict = stations_next_to_river(stations)
    #print(river_dict.keys())
    for i in river_dict.keys():
        for j in river_dict[i]:
            print(j)


test_distance_conversion()
test_stations_by_distance()
test_stations_next_to_river()


test_stations_within_radius()

def test_rivers_with_station():
    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    typical_range = (1.0)
    town = "MyTown"

    RiverA = "RiverA"
    RiverB = "RiverB"

    Station1 = MonitoringStation(s_id, m_id, label, coord, typical_range, RiverA, town)
    Station2 = MonitoringStation(s_id, m_id, label, coord, typical_range, RiverB, town)
    Station3 = MonitoringStation(s_id, m_id, label, coord, typical_range, RiverA, town)

    stations_examples = [Station1, Station2, Station3]

    assert isinstance(rivers_with_station(stations_examples), set) == True

def test_rivers_by_station_number():
    stations = build_station_list()
    n = 9
    output = stations_next_to_river(stations)
    assert type(output) == type(dict())
    output = stations_next_to_river(stations)
    river_numbers = []
    for river_name, numbers in output.items():
        tuple = (river_name, len(numbers))
        assert type(tuple) == type(tuple())
        assert len(tuple) == 2
        assert len(river_numbers) == len(output)
        river_numbers.append(tuple)
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
        if river[1] == river_N_numbers[N-1][1] :
            river_N_numbers.append(river)
    return river_N_numbers

