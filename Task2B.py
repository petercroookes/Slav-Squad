from floodsystem.station import *
from floodsystem.stationdata import *
from floodsystem.flood import stations_level_over_threshold


def run():
    stations = build_station_list()
    update_water_levels(stations)
    tol = 0.8
    list = stations_level_over_threshold(stations,tol)
    name_and_level = [list[0].name, list[1]]
    print(name_and_level)

if __name__ == "__main__":
    print("\n*** Task 2B: CUED Part IA Flood Warning System ***")
    run()

run()