from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.station import *
from floodsystem.flood import stations_highest_rel_level
from floodsystem.plot import plot_water_levels
from floodsystem.datafetcher import fetch_measure_levels
import datetime

def run():
    stations = build_station_list()
    update_water_levels(stations)
    sorted_stations = stations_highest_rel_level(stations, 5)
    sorted_stations = sorted(((station, station.relative_water_level()) for station in stations if station.relative_water_level() != None), key = lambda x: x[1], reverse = True)[:5]
    for i in sorted_stations:
        station_info = i[0]
        dt = 10
        dates, levels = fetch_measure_levels(station_info.measure_id, dt = datetime.timedelta(dt))
        plot_water_levels(station_info, dates, levels)

if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()