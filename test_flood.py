from floodsystem.flood import *
from floodsystem.station import *
from floodsystem.stationdata import *

def test_stations_level_over_threshold():
    # Create lists relative water level and inconsistent typical range lists using real data
    # and check that there are no common stations in each.
    stations = build_station_list
    update_water_levels(stations)
    rel_level_list = stations_level_over_threshold(stations, 0)
    inconsistent_data_list = inconsistent_typical_range_stations(stations)
    for i in rel_level_list:
        for j in inconsistent_data_list:
            assert i[0] != j.name