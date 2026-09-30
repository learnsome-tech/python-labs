# weather/__init__.py, the plain version
'''The weather package.'''

# the re-exporting version
from weather.report import summary

# which lets a caller write
from weather import summary
