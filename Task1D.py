from floodsystem.geo import stations_next_to_river
from floodsystem.geo import rivers_with_station
from floodsystem.stationdata import build_station_list

def run1():
    # Create list stations using real data
    stations = build_station_list()
    # Sort the list alphabetically
    sorted_rivers_with_station = sorted(rivers_with_station(stations))
    print("Number of Rivers with at Least 1 River Station:", len(sorted_rivers_with_station))
    print("The first 10 are:")
    # Print the first 10 stations
    print(sorted_rivers_with_station[:10])

def run2():
    # Create list stations using real data
    stations = build_station_list()
    # Create dictionary from real data with the river as the key and each station by next to that corresponding to it. 
    river_station_dictionary = stations_next_to_river(stations)
    # From the dictionary, extract a list of stations that are next to a particular river. (Done of Rivers Aire, Cam and Thames)
    River_Aire = river_station_dictionary["River Aire"]
    River_Cam = river_station_dictionary["River Cam"]
    River_Thames = river_station_dictionary["River Thames"]
    print("Stations on River Aire in Alphabetical Order:",sorted(River_Aire))
    print("Stations on River Cam in Alphabetical Order:",sorted(River_Cam))
    print("Stations on River Thames in Alphabetical Order:",sorted(River_Thames))

if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run1()
    run2()
    