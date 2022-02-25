import matplotlib.dates
import numpy as np

def polyfit(dates, levels, p):
    x = matplotlib.dates.date2num(dates)
    y = levels
    p_coefficient = np.polyfit(x-x[0], y, p)
    poly = np.polyld(p_coefficient)
    return poly, x[0]