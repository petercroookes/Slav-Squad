from floodsystem.station import MonitoringStation

def stations_level_over_threshold(stations, tol):
    """Returns a list of tuples, where each tuple holds (i) a station at which the latest relative water 
    level is over tol and (ii) the relative water level at the station. The returned list should be sorted by the 
    relative level in descending order."""
    
    stations_over_threshold = []
    
    for n in stations:
        rel_level = n.relative_water_level()
        
        if rel_level != None:
            if rel_level > tol:
                station = (n.name, rel_level)
                stations_over_threshold.append(station)
    
    sorted_list = stations_over_threshold.sort(key=lambda x:x[1], reverse=True)

    return sorted_list

        
        
        
