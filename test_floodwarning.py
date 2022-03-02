from floodsystem.floodwarning import floodwarning
from floodsystem.stationdata import *
import random

def test_floodwarning():
    # Create stations list from real data and update it.
    stations = build_station_list()
    update_water_levels(stations)
    
    # Select a random sample of ten stations.
    sample_stations = random.sample(stations,10)

    # Run the floodwarning function  to split the list into risk catogeries.
    severe_list, high_list, moderate_list, low_list = floodwarning(sample_stations)

    # Verify that stations within each list are ordered correctly
    if bool(severe_list) == True and len(severe_list) >= 2:
        assert severe_list[1][1] >= severe_list[0][1]
    
    if bool(high_list) == True and len(severe_list) >= 2:
        assert high_list[1][1] >= high_list[0][1]
    
    if bool(moderate_list) and len(moderate_list) >= 2:
        assert moderate_list[1][1] >= moderate_list[0][1]
    
    if bool(low_list) and len(low_list) >= 2:
        assert low_list[1][1] >= low_list[0][1]
    
    # Assert that the ordering of the lists is correct (i.e. first entry of moderate is higher than the last entry of low)
    if bool(severe_list) == True and bool(high_list) == True:
        assert severe_list[0][1] >= high_list[-1][1]

    if bool(high_list) == True and bool(moderate_list) == True:
        assert high_list[0][1] >= moderate_list[-1][1]
    
    if bool(moderate_list) == True and bool(low_list) == True:
        assert moderate_list[0][1] >= low_list[-1][1]

    
    
    