from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance
from floodsystem.station import *

def run():
    stations = build_station_list()
    stations_sorted = stations_by_distance(stations, (52.2053, 0.1218))

    station_town_distance = []
    for i in stations_sorted:
        station_town_distance += [(i[0].name, i[0].town, i[1])]
    
    furthest_stations = station_town_distance[-10:]
    closest_stations = station_town_distance[:10]
    
    print("10 Stations Furthest From Cambridge:",furthest_stations)
    print("10 Stations Closest to Cambridge:",closest_stations)


run()
        