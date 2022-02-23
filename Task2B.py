from floodsystem.station import *
from floodsystem.stationdata import *
from floodsystem.flood import stations_level_over_threshold



stations = build_station_list()
update_water_levels(stations)
tol = 0.8
list = stations_level_over_threshold(stations,tol)
print(list)


