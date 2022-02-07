from floodsystem.geo import stations_by_river
from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_next_to_river

stations = build_station_list()
print("stations next to river", len(stations_next_to_river(stations)))
print("stations by river", len(stations_by_river(stations)))