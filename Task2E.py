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
    for i in sorted_stations:
        name = i[0]
        delta_t = 10
        dates, levels = fetch_measure_levels(name.measure_id, delta_t = datetime.timedelta(dates = delta_t))
        plot_water_levels(stations, dates, levels)

if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()