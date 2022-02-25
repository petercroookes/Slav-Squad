from floodsystem.station import MonitoringStation
from floodsystem.flood import stations_level_over_threshold
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.analysis import polyfit
import datetime

stations = build_station_list()
update_water_levels(stations)

# initial guess for warning water level thresholds
severe = 5.0
high = 4.0
moderate = 2.5
low = 1.5

# generate list of stations above a threshold of 0.8m
tol = 0.8
risk_stations = []
stations_over_threshold = stations_level_over_threshold(stations, tol)
for i in stations_over_threshold:
    risk_stations.append(i[0].name)

print(risk_stations)

# generate list of tuples of polynomial coefficients, using value of dt and p from 2f intially
p_coeff = []
for i in stations_over_threshold:
    station = i[0]
    dt = 2
    dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
    p_coeff.append(polyfit(dates, levels, 4))

print(p_coeff)