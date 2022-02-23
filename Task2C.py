from floodsystem.stationdata import *
from floodsystem.flood import *


def run():
    # Build list of stations
    stations = build_station_list()

    # Update stations with latest level data
    update_water_levels(stations)

    # Produce list of 10 stations with largest relative water level
    Largest_Ten = stations_highest_rel_level(stations, 10)

    # Print
    print(Largest_Ten)

if __name__ == "__main__":
    print("\n*** Task 2C: CUED Part IA Flood Warning System ***")
    run()

run()