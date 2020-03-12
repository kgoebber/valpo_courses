# # Upperair Observation Plotting

from datetime import datetime

import cartopy.crs as ccrs
from metpy.io import add_station_lat_lon
from metpy.plots import declarative
from metpy.units import units
from siphon.simplewebservice.iastate import IAStateUpperAir
import pandas as pd


# ## Read Data
# Set date for desired UPA data
date = datetime(2020, 2, 29, 12)

# Request data using Siphon request for data from Iowa State Archive
df = IAStateUpperAir.request_all_data(date)

df = add_station_lat_lon(df, 'station')

df['dewpoint_depression'] = df['temperature'] - df['dewpoint']


# ## Plot Upperair Map

# Set a format specifier for the geoptential height
# This formatter takes a value 9300 -> 930
height_format = lambda v: format(v, '.0f')[1:]

# Plot desired data
obs = declarative.PlotObs()
obs.data = df
obs.time = date
obs.level = 850 * units.hPa
obs.fields = ['temperature', 'dewpoint_depression', 'height']
obs.locations = ['NW', 'SW', 'NE']
obs.formats = [None, None, height_format]
obs.vector_field = ['u_wind', 'v_wind']

# Panel for plot with Map features
panel = declarative.MapPanel()
panel.layout = (1, 1, 1)
panel.projection = 'lcc'
panel.area = [-120, -74, 24, 50]
panel.layers = ['states', 'coastline']
panel.title = (f'{obs.level.m}-hPa Observations                                '
               f'                                                                                            Valid: {date}')
panel.plots = [obs]

# Bringing it all together
pc = declarative.PanelContainer()
pc.size = (20, 16)
pc.panels = [panel]

#pc.show()
pc.save(f'{obs.level.m}hPa_observations_{date:%Y%m%d%H}.png', dpi=150, bbox_inches='tight')

