from floodsystem.stationdata import *
from floodsystem.flood import *


def run():
    # Build list of stations
    stations = build_station_list()

    # Update stations with latest level data
    update_water_levels(stations)

    # Produce list of 10 stations with largest relative water level
    Largest_Ten = stations_highest_rel_level(stations, 10)
    Largest_Ten_name_and_level = []
    for n in range(len(Largest_Ten)):
        name = Largest_Ten[n][0].name
        level = Largest_Ten[n][1]
        Largest_Ten_name_and_level.append((name, level))
    print(Largest_Ten_name_and_level)


if __name__ == "__main__":
    print("\n*** Task 2C: CUED Part IA Flood Warning System ***")
    run()

run()