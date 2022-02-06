from floodsystem.station import inconsistent_typical_range_stations
from floodsystem.stationdata import build_station_list
def run():
    stations = build_station_list()
    data_list_names = [station.name for station in inconsistent_typical_range_stations(stations)]
    data_list_names.sort()
    print(data_list_names)

if __name__ == "__main__":
    print("*** Task 1F: CUED Part IA Flood Warning System ***")
    run()