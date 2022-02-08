from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_by_station_number

def run():
    # Create a list of stations using real data.
    stations = build_station_list()
    # Show the 9(+) rivers with the most stations.
    print(rivers_by_station_number(stations, 9))


if __name__ == "__main__":
    print("*** Task 1E: CUED Part IA Flood Warning System ***")
    run()