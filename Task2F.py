from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.station import *
from floodsystem.flood import stations_highest_rel_level
from floodsystem.plot import plot_water_level_with_fit
from floodsystem.datafetcher import fetch_measure_levels
import datetime
import matplotlib.pyplot as plt

def run():
    stations = build_station_list()
    update_water_levels(stations)
    highest_5 = sorted(((station, station.relative_water_level()) for station in stations if station.relative_water_level() != None), key = lambda x: x[1], reverse = True)[:5]
    print(highest_5)
    for i in highest_5:
        station  = i[0]
        dt = 2
        dates, levels = fetch_measure_levels(station.measure_id, dt = datetime.timedelta(days = dt))
        try:
            low = [station.typical_range[0]*len(levels)]
            high = [station.typical_range[1]*len(levels)]
            plt.plot(dates, low)
            plt.plot(dates, high)
            plot_water_level_with_fit(station, dates, levels, 4)
        except:
            pass

if __name__ == "__main__":
    print("*** Task 2F: CUED Part IA Flood Warning System ***")
    run()