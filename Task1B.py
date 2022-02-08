from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance
from floodsystem.station import *

def run():
    """Requirements for Task 1B"""

    # Create list of stations
    stations = build_station_list()

    # Sort them by distance using stations_by_distance from geo,py
    stations_sorted = stations_by_distance(stations, (52.2053, 0.1218))
    
    # Create empty list
    station_town_distance = []

    # Populate list with the name, town and position list of each entry in stations_sorted
    for i in stations_sorted:
        station_town_distance.append([(i[0].name, i[0].town, i[1])])
    
    # 10 furthest stations are the last 10 in the list, and the 10 closest are the first 10. 
    furthest_stations = station_town_distance[-10:]
    closest_stations = station_town_distance[:10]
    
    print("10 Stations Furthest From Cambridge:",furthest_stations)
    print("10 Stations Closest to Cambridge:",closest_stations)

<<<<<<< HEAD
if __name__ == "__main__":
    print("*** Task 1A: CUED Part IA Flood Warning System ***")
    run()    
=======

if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()
        
>>>>>>> 1d02fc1dce08ac2f2166567b785d437d78abc5ae
