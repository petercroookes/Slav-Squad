# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module provides a model for a monitoring station, and tools
for manipulating/modifying station data

"""

class MonitoringStation:
    """This class represents a river level monitoring station"""

    def __init__(self, station_id, measure_id, label, coord, typical_range,
                 river, town):

        self.station_id = station_id
        self.measure_id = measure_id

        # Handle case of erroneous data where data system returns
        # '[label, label]' rather than 'label'
        self.name = label
        if isinstance(label, list):
            self.name = label[0]

        self.coord = coord
        self.typical_range = typical_range
        self.river = river
        self.town = town

        self.latest_level = None

    def __repr__(self):
        d = "Station name:     {}\n".format(self.name)
        d += "   id:            {}\n".format(self.station_id)
        d += "   measure id:    {}\n".format(self.measure_id)
        d += "   coordinate:    {}\n".format(self.coord)
        d += "   town:          {}\n".format(self.town)
        d += "   river:         {}\n".format(self.river)
        d += "   typical range: {}".format(self.typical_range)
        return d

    # Check that the typical range values for a river are valid (lower value must be less than higher value)   
    def typical_range_consistent(self):
        if self.typical_range == None:
            return False
        elif self.typical_range[0] <= self.typical_range[1]:
            return True
        else:
            return False
    
     
    def relative_water_level(self):
        """This function returns the relative water level, given by the ratio of the latest water level 
        minus the typical minimum to the typical range i.e. a ratio of 1.0 corresponds to a level at the 
        typical high and a ratio of 0.0 corresponds to a level at the typical low """
        # If the typical range is consistent, it calculates the ratio, and if this causes an error e.g. 
        # a NoneType error, it creates an exception and returns None. Otherwise, it returns the ratio, and
        # and if the range is not consistent, it returns None.      
        if self.typical_range_consistent() == True:
            try:
                ratio = (self.latest_level - self.typical_range[0])/(self.typical_range[1]-self.typical_range[0])
            except TypeError:
                return None
        # Filter out anomalous values.
            if ratio < 100:
                return ratio
        else:
            return None


# Create a list for stations that do not have conistent typical ranges.
def inconsistent_typical_range_stations(stations):
    inconsistent_data_list = []
    for station in stations:
        if station.typical_range_consistent() == False:
            inconsistent_data_list.append(station)
    return inconsistent_data_list



