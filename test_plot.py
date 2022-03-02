from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.station import *
from floodsystem.plot import plot_water_level_with_fit, plot_water_levels
from floodsystem.datafetcher import fetch_measure_levels
import datetime
import matplotlib.pyplot as plt
import random

def test_plot_water_levels():
    # Create station list using real data and update water levels.
    stations = build_station_list()
    update_water_levels(stations)

    # Select random station and obtain water levels over the last x days.
    station = random.choice(stations)
    dates, levels = fetch_measure_levels(station.measure_id, dt = datetime.timedelta(days = 13))

    # Plot the graph and visually inspect it. 
    plot_water_levels(station, dates, levels)
    plt.close

def test_plot_water_level_with_fit():
    # Create station list using real data and update water levels.
    stations = build_station_list()

    # Select random station and obtain water levels over the last x days.
    station = random.choice(stations)
    dates, levels = fetch_measure_levels(station.measure_id, dt = datetime.timedelta(days = 13))

    # Plot the graph and visually inspect it. 
    plot_water_level_with_fit(station, dates, levels, 20)
    plt.close

test_plot_water_level_with_fit()
test_plot_water_levels