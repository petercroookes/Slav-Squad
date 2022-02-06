from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_within_radius
def run():
    stations = build_station_list()
    radius_list = stations_within_radius(stations, (52.2053, 0.1218), 10)
    sorted_list = sorted(radius_list, key = lambda x: x.name)
    print([station.name for station in sorted_list])

if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***")
    run()