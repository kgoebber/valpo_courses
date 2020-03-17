##############################################################################################
#                                                                                            #
# Script Name:    surface_map.py                                                             #
# Author:         Kevin Goebbert                                                             #
# Purpose:        This script plots a surface map for the CONUS.                             #
# Created:        2 March 2020                                                               #
# Modifications:  (None)                                                                     #
#                                                                                            #
##############################################################################################

# Import needed Python Modules
from datetime import datetime, timedelta

from metpy.plots import declarative
from metpy.units import units
import pandas as pd

###############################################
# MODIFY THIS CODE TO READ IN FROM AN ARGUMENT
sdate = "20160301"
shour = "12"
#
###############################################

# Construct datetime object from input date and hour
date = datetime(int(sdate[:4]), int(sdate[4:6]), int(sdate[6:8]), int(shour))

# Read relevant files and compute temperature/dewpoint in Fahrenheit
df = pd.read_csv(f'http://bergeron.valpo.edu/archive_surface_data/{date:%Y}/{date:%Y%m%d}_metar.csv', 
                 parse_dates=['date_time'])
df['tmpf'] = (df.air_temperature.values * units.degC).to('degF')
df['dwpf'] = (df.dew_point_temperature.values * units.degC).to('degF')

# Formatter for MSLP values to be properly encoded for plotting purposes
mslp_formatter = lambda v: format(v*10, '.0f')[-3:]

# Plot desired data
obs = declarative.PlotObs()
obs.data = df
obs.time = date
obs.time_window = timedelta(minutes=15)
obs.level = None
obs.fields = ['cloud_coverage', 'tmpf', 'dwpf',
              'air_pressure_at_sea_level', 'present_weather']
obs.locations = ['C', 'NW', 'SW', 'NE', 'W']
obs.formats = ['sky_cover', None, None, mslp_formatter, 'current_weather']
obs.reduce_points = 1
obs.vector_field = ['eastward_wind', 'northward_wind']

# Panel for plot with Map features
panel = declarative.MapPanel()
panel.layout = (1, 1, 1)
panel.projection = 'lcc'
panel.area = [-105, -70, 25, 50]
panel.layers = ['states', 'borders', 'coastline']
panel.title = f'Surface Plot at {obs.time} by KHG'
panel.plots = [obs]

# Bringing it all together
pc = declarative.PanelContainer()
pc.size = (24, 18)
pc.panels = [panel]

pc.save(f'{date:%Y%m%d_%H%M}_surface.png', dpi=150, bbox_inches='tight')
