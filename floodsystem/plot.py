import matplotlib.pyplot as plt
import matplotlib.dates
from datetime import datetime, timedelta
#from .analysis import *

def plot_water_levels(station, dates, levels):
    plt.plot(dates, levels)
    high_level = station.typical_range[0]*len(levels)
    low_level = station.typical_range[1]*len(levels)
    plt.plot(dates, high_level)
    plt.plot(dates, low_level)
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.title(station.name)
    plt.tight_layout()
    plt.show()