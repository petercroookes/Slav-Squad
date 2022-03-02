from .datafetcher import *
from .analysis import polyfit
import datetime
from .utils import sorted_by_key

def floodwarning(stations):
    ordered = []
    for station in stations:
        if station.relative_water_level() != None:
            if station.relative_water_level() > 1:
                dates, levels = fetch_measure_levels(station.measure_id, dt = datetime.timedelta(days = 1))
                if len(levels) > 0:    
                    level_change = levels[len(levels)-1] - levels[0]
                    tuple = (station.name, level_change)
                    ordered.append(tuple)
    ordered = sorted_by_key(ordered, 1)
    low_list = ordered[:int(len(ordered)*0.3):]
    high_list = ordered[int(len(ordered)*0.6):int(len(ordered)*0.9)]
    moderate_list = ordered[int(len(ordered)*0.3):int(len(ordered)*0.6)]
    severe_list = ordered[int(len(ordered)*0.9):]
    return severe_list, high_list, moderate_list, low_list