from .utils import sorted_by_key

def stations_level_over_threshold(stations, tol):
    """Returns a list of tuples, where each tuple holds (i) a station at which the latest relative water 
    level is over tol and (ii) the relative water level at the station. The returned list is then sorted by the 
    relative level in descending order."""
    
    # Create empty list
    stations_over_threshold = []
    
    # For each station, if the relative water level is not None and if the water level is above tol, 
    # append to the list a tuple of the station name and the corresponding relative water level. Sort this list
    # in descending order.
    for n in stations:
        rel_level = n.relative_water_level()
        
        if rel_level != None and rel_level > tol:
            station = (n.name, rel_level)
            stations_over_threshold.append(station)
    
    sorted_list = sorted_by_key(stations_over_threshold, 1, reverse=True)

    return sorted_list


def stations_highest_rel_level(stations, N):
    """Returns a list of N stations which have the highest water level relative to their typical range."""
    rel_level_list = stations_level_over_threshold(stations, 0)
    biggest_n = rel_level_list[:N]
    return biggest_n