# inside weather/report.py
from .readings import highest         # relative
from weather.readings import highest  # absolute

$ python3 weather/report.py
ImportError: attempted relative import with no known parent package

$ python3 weather/report.py   # the absolute version
ModuleNotFoundError: No module named 'weather'
