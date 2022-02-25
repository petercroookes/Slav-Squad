import matplotlib.pyplot as plt
import matplotlib.dates
from datetime import datetime, timedelta
from analysis import *

def plot_water_levels(station, dates, levels):
    plt.plot(dates, levels)
    high_level = [station.typical_range[0]]*len(levels)
    low_level = [station.typical_range[1]]*len(levels)
    plt.plot(dates, high_level)
    plt.plot(dates, low_level)
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation = 45)
    plt.title(station.name)
    plt.tight_layout()
    plt.show()

def plot_water_level_with_fit(station, dates, levels, p):
    x = matplotlib.dates.date2num(dates)
    y = levels
    poly, d0 = polyfit(dates, levels, p)
    plt.plot(dates, '.')
    plt.plot(dates, poly(x-d0))
    plt.xlabel('date')
    plt.ylabel('water level')
    plt.xticks(rotation = 45)
    plt.title(station.name)
    plt.tight_layout()
    plt.show()
