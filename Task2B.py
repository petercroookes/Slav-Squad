from floodsystem.station import *
from floodsystem.stationdata import *
from floodsystem.flood import stations_level_over_threshold

stations = build_station_list()
update_water_levels(stations)
tol = 0.8

for n in stations_level_over_threshold(stations, tol):
    print(n[0].name, n[1])

