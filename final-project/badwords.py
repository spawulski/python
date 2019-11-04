"""
Badwords docs.

This is a pretty ugly array of words, and I wanted to keep it out of the
code for scrape_weather.py module.
"""

a = 'Environment and Climate Change Canada'

b = '- Meteorological Service of Canada'

n = a + " " + b

bad_words = ['scheme', 'W3CDTF', 'Google Tag Manager',
             """Environment and Climate Change Canada -
              Meteorological Service of Canada""", 'degrees', 'minute',
             'second', 'North', 'West', 'East', 'South',
             'World Meteorological Organization',
             'Transport Canada', 'Comma Separated Values',
             'Extensible Markup Language', 'metre', 'Maximum Temperature',
             'degrees Celsius', 'Daily Maximum Temperature Chart',
             'Minimum Temperature', 'Daily Minimum Temperature Chart',
             'Mean Temperature', 'Daily Mean Temperature Chart',
             'Heating Degree Days', 'Daily Heating Degree Days Chart',
             'millimetres', 'Daily Total Rain Chart', 'centimetres',
             'Daily Total Snow Chart', 'Total Precipitation',
             'Daily Total Precipitation Chart', 'Cooling Degree Days',
             'Daily Cooling Degree Days Chart', 'Snow on Ground',
             'Daily Snow on Ground Chart', 'Direction of Maximum Gust',
             'tens of degrees', 'Speed of Maximum Gust',
             'kilometres per hour', 'Daily Speed of Maximum Gust Chart',
             n, 'Average', 'Extreme'
             ]
