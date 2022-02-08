from floodsystem.stationdata import build_station_list
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
    #print(river_dict.keys()
    for i in river_dict.keys():
        for j in river_dict[i]:
            for station in stations:
                if station.name == j:
                    temp = station
                    break
            print(j)
            print(temp.river, i)
            if temp.river == i:
                print("1")
            else:
                print("0")
            


test_distance_conversion()
test_stations_by_distance()
test_stations_next_to_river()
test_stations_within_radius()