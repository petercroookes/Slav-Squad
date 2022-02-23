# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the station module"""

from floodsystem.station import *
from floodsystem.flood import *
from floodsystem.stationdata import *

def test_create_monitoring_station():
    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    assert s.station_id == s_id
    assert s.measure_id == m_id
    assert s.name == label
    assert s.coord == coord
    assert s.typical_range == trange
    assert s.river == river
    assert s.town == town

def test_typical_range_consistent():
    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    river = "River X"
    town = "My Town"

    # Create test values that are examples of correct and incorrect typical ranges.
    correct_typical_range1 = (0,2)
    correct_typical_range2 = (-5,5)
    correct_typical_range3 = (10,100)
    incorrect_typical_range1 = (10,1)
    incorrect_typical_range2 = (6.2,-15)
    incorrect_typical_range3 = None

    # Set up the class for each example with corresponding test value and river "data"
    correct1 = MonitoringStation(s_id, m_id, label, coord, correct_typical_range1, river, town)
    correct2 = MonitoringStation(s_id, m_id, label, coord, correct_typical_range2, river, town)
    correct3 = MonitoringStation(s_id, m_id, label, coord, correct_typical_range3, river, town)
    
    incorrect1 = MonitoringStation(s_id, m_id, label, coord, incorrect_typical_range1, river, town)
    incorrect2 = MonitoringStation(s_id, m_id, label, coord, incorrect_typical_range2, river, town)
    incorrect3 = MonitoringStation(s_id, m_id, label, coord, incorrect_typical_range3, river, town)

    # Assert that the function returns true for the correct values and false for the incorrect values.
    assert correct1.typical_range_consistent() == True
    assert correct2.typical_range_consistent() == True
    assert correct3.typical_range_consistent() == True

    assert incorrect1.typical_range_consistent() == False
    assert incorrect2.typical_range_consistent() == False
    assert incorrect3.typical_range_consistent() == False


def test_inconsistent_typical_range_stations():
    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    river = "River X"
    town = "My Town"

    # Create test values that are examples of correct and incorrect typical ranges.
    correct_typical_range1 = (0,2)
    correct_typical_range2 = (-5,5)
    correct_typical_range3 = (10,100)
    incorrect_typical_range1 = (10,1)
    incorrect_typical_range2 = (6.2,-15)
    incorrect_typical_range3 = None

    # Set up the station class for each example with corresponding test value and river "data"
    correct1 = MonitoringStation(s_id, m_id, label, coord, correct_typical_range1, river, town)
    correct2 = MonitoringStation(s_id, m_id, label, coord, correct_typical_range2, river, town)
    correct3 = MonitoringStation(s_id, m_id, label, coord, correct_typical_range3, river, town)
    
    incorrect1 = MonitoringStation(s_id, m_id, label, coord, incorrect_typical_range1, river, town)
    incorrect2 = MonitoringStation(s_id, m_id, label, coord, incorrect_typical_range2, river, town)
    incorrect3 = MonitoringStation(s_id, m_id, label, coord, incorrect_typical_range3, river, town)

    # Create a list of station examples 
    station_examples = [correct1,correct2,correct3,incorrect1,incorrect2,incorrect3]

    # Check that the subsequent list produced by the function inconsistent_typical_range_stations contains
    # all of the incorrect examples and none of the correct examples.
    assert inconsistent_typical_range_stations(station_examples) == [incorrect1,incorrect2,incorrect3]

