# Import Packages
from datetime import datetime, timedelta
from io import StringIO
from urllib.request import urlopen

from metpy.io import metar
from metpy.plots.declarative import *
from metpy.units import units

# Set Date
date = datetime(2020, 12, 20, 12)

# Get Data
data = StringIO(urlopen('http://bergeron.valpo.edu/current_surface_data/'
                        f'{date:%Y%m%d%H}_sao.wmo').read().decode('utf-8', 'backslashreplace'))
df = metar.parse_metar_file(data, year=date.year, month=date.month)

# Plot Data
obs = PlotObs()
obs.data = df
obs.time = date
obs.time_window = timedelta(minutes=15)
obs.level = None
obs.fields = ['air_temperature']

# Panel for plot with Map features
panel = MapPanel()
panel.layout = (1, 1, 1)
panel.projection = 'lcc'
panel.area = 'in'
panel.layers = ['states']
panel.plots = [obs]

# Bringing it all together
pc = PanelContainer()
pc.size = (10, 10)
pc.panels = [panel]

# Show image
pc.show()
