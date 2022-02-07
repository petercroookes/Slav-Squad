from floodsystem.geo import stations_by_river
from floodsystem.geo import rivers_with_station
from floodsystem.stationdata import build_station_list

def run1():
    stations = build_station_list()
    sorted_rivers_with_station = sorted(rivers_with_station(stations))
    print("Number of Rivers with at Least 1 River Station:", len(sorted_rivers_with_station))
    print("The first 10 are:")
    print(sorted_rivers_with_station[:10])

def run2():
    stations = build_station_list()
    river_station_dictionary = stations_by_river(stations)
    River_Aire = river_station_dictionary["River Aire"]
    River_Cam = river_station_dictionary["River Cam"]
    River_Thames = river_station_dictionary["River Thames"]
    print("Stations on River Aire in Alphabetical Order:",sorted(River_Aire))
    print("Stations on River Cam in Alphabetical Order:",sorted(River_Cam))
    print("Stations on River Thames in Alphabetical Order:",sorted(River_Thames))

run1()
run2()
    