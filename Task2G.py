from distutils.command.build import build
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.station import *
from floodsystem.floodwarning import floodwarning
from floodsystem.flood import stations_highest_rel_level

def run():
    stations = build_station_list()
    update_water_levels(stations)
    severe, high, moderate, low = sorted(floodwarning(stations), key = lambda x: x[1], reverse = True)
    severe_list = []
    moderate_list = []
    high_list = []
    low_list = []
    for i in range(len(severe)):
        severe_list.append(severe[i][0])
    for i in range(len(high)):
        high_list.append(high[i][0])
    for i in range(len(moderate)):
        moderate_list.append(moderate[i][0])
    for i in range(len(low)):
        low_list.append(low[i][0])
    
    print('severe', severe_list)
    print('')
    print('high', high_list)
    print('')
    print('moderate', moderate_list)
    print('')
    print('low', low_list)


if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()