from floodsystem.flood import *
from floodsystem.station import *
from floodsystem.stationdata import *

def test_stations_level_over_threshold():
    # Create a station with arbitrary properties.
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = "coord"
    river = "River X"
    town = "My Town"

    # Create a consistent typical range and then assign this to 3 different test stations, each with different latest
    # levels.
    consistent_typical_range1 = (5,7)
    test_station1 = MonitoringStation(s_id, m_id, label, coord, consistent_typical_range1, river, town)
    test_station1.latest_level = 5.5
    test_station2 = MonitoringStation(s_id, m_id, label, coord, consistent_typical_range1, river, town)
    test_station2.latest_level = 6.5
    test_station3 = MonitoringStation(s_id, m_id, label, coord, consistent_typical_range1, river, town)
    test_station3.latest_level = 7   
    
    # Create a list containing all of the test stations, and then run the function stations_level_over_threshold to
    # create a new list.
    test_station_list = [test_station1,test_station2,test_station3]
    test_stations_over_threshold = stations_level_over_threshold(test_station_list,0.5)
    
    # Assert that the length of the list is 2, as only two test stations have a relative water level above the threshold
    # and assert that it is ordered in descending order.
    assert len(test_stations_over_threshold) == 2
    assert test_stations_over_threshold[0][0] == test_station3.name
    assert test_stations_over_threshold[1][0] == test_station2.name

def test_stations_highest_rel_level():
    # Build a stations list using real data, and update all of their water levels.
    stations = build_station_list()
    update_water_levels(stations)

    # Run the function stations_highest_rel_level to make a list of the ten rivers the with 
    # greatest relative water levels.
    biggest_ten = stations_highest_rel_level(stations, 10)

    # Check that the length of the list is indeed ten as asked for.
    assert len(biggest_ten) == 10

    # Check that each entry in the list is a tuple and check that it is in descending order with 
    # respect to relative water level.
    for n in range(1,len(biggest_ten)):
        assert isinstance(biggest_ten[n],tuple)
        assert biggest_ten[n][1] <= biggest_ten[n-1][1]