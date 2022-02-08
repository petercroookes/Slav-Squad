from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_within_radius

def run():
    """Task Requirments for Task 1C"""
    # Create list of stations
    stations = build_station_list()

    # Create list of stations within 10 km radius of the town centre
    radius_list = stations_within_radius(stations, (52.2053, 0.1218), 10)

    # Sort the list, and then print the names of the stations in sorted order.
    sorted_list = sorted(radius_list, key = lambda x: x.name)
    print([station.name for station in sorted_list])

if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***")
    run()