from datetime import datetime, timedelta

from metpy.plots import declarative
from metpy.units import units
import pandas as pd


date = datetime(2010, 9, 7, 12)

df = pd.read_csv(f'http://bergeron.valpo.edu/archive_surface_data/{date:%Y}/{date:%Y%m%d}_metar.csv',
                 parse_dates=['date_time'], na_values=[-9999], low_memory=False)
df['tmpf'] = (df.air_temperature.values * units.degC).to('degF')
df['dwpf'] = (df.dew_point_temperature.values * units.degC).to('degF')

mslp_formatter = lambda v: format(v*10, '.0f')[2:]

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
obs.reduce_points = 0.75
obs.vector_field = ['eastward_wind', 'northward_wind']

# Panel for plot with Map features
panel = declarative.MapPanel()
panel.layout = (1, 1, 1)
panel.projection = 'lcc'
panel.area = [-105, -65, 25, 46]
panel.layers = ['states', 'borders', 'coastline']
panel.plots = [obs]

# Bringing it all together
pc = declarative.PanelContainer()
pc.size = (25, 25)
pc.panels = [panel]

pc.save(f'sfc_map_{date:%Y%m%d_%H}.png', dpi=150, bbox_inches='tight')

