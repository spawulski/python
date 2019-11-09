"""
This is the documentation for scrape_weather module.

scrape_weather scrapes the daily weather from the internet
and passes a dict with the data.
"""
from html.parser import HTMLParser
from datetime import date
import urllib.request
import datetime
import badwords


class MyHTMLParser(HTMLParser):
    """Parse data from web pages."""

    attr_flag = False
    data_counter = 0
    weather = {}
    temp_weather = {}
    date = ''
    day = ''
    min = ''
    max = ''
    mean = ''

    def handle_starttag(self, tag, attrs):
        """
        Check attriutes.

        Eliminate bad attributes by checking against
        badwords. Save date to class variable.
        Set flag to true for handle_data().
        """
        f = '%B %d, %Y'
        t = '%Y-%m-%d'

        for attr in attrs:
            if "title" in attr:
                if attr[1] not in badwords.bad_words:
                    a = attr[1]
                    self.date = datetime.datetime.strptime(a, f).strftime(t)
                    self.attr_flag = True

    def float_checker(self, s):
        """Check value to see if float."""
        try:
            float(s)
            return True
        except Exception:
            return False

    def data_reset(self):
        """Reset variables used in weather dict creation."""
        self.day = ''
        self.max = ''
        self.min = ''
        self.mean = ''

    def handle_data(self, data):
        """Extract the actual weather data we want from the page."""
        # Check attribute flag
        if self.attr_flag:
            # If data is a float, at this point we know its the data we want
            if self.float_checker(data.strip()):
                # Here we add a counter, based on the counter value
                # we know what the data represents.
                # In this case its the day, max, min, or mean temp.
                if self.data_counter < 4:
                    if self.data_counter == 0:
                        self.day = data
                    if self.data_counter == 1:
                        self.max = data
                    if self.data_counter == 2:
                        self.min = data
                    if self.data_counter == 3:
                        self.mean = data

                    self.data_counter += 1
                # When the counter = 4, we have the data scraped for
                # the particular day. It can now be put into the 'daily_temps'
                # dict and pushed to the class dict that holds all the daily
                # weather
                # Also reset flags, counter, and daily weather variables.
                else:
                    daily_temps = {'Max': self.max,
                                   'Min': self.min,
                                   'Mean': self.mean}
                    self.weather.update({self.date: daily_temps})
                    self.temp_weather.update({self.date: daily_temps})
                    self.attr_flag = False
                    self.data_counter = 0
                    self.data_reset()


myparser = MyHTMLParser()

all_weather = {}


def scrape_page(url):
    """Scrape a url that is passed in for weather data."""
    monthly_weather = {}
    monthly_weather = myparser.temp_weather
    myparser.temp_weather.clear()
    with urllib.request.urlopen(url) as response:
        html = str(response.read())

    myparser.feed(html)
    return monthly_weather
    # print(myparser)

    # for k, v in myparser.weather.items():
    # print(k)
    #    monthly_weather.update({k: v})

    # return monthly_weather


def scrape_all_weather():
    """
    Scrape all the weather.

    start with today and moving backward until there is no more weather
    data to scrape, get all weather data.
    """
    a = 'https://climate.weather.gc.ca/'
    b = 'climate_data/daily_data_e.html?'
    c = 'StationID=27174&timeframe=2&'
    d = 'StartYear=1840&EndYear=2018&Day='
    full = a + b + c + d
    # Set variable to todays date.
    today = date.today()
    # Pull the year out of that.
    current_year = today.strftime("%Y")
    # Iterate through all of the years starting with current and working back.
    for year in range(int(current_year), 0, -1):
        print(str(year))
        # Iterate through the months backward, starting with December
        for month in range(12, 0, -1):
            print(str(month))
            # Build url to scrape using year and month
            url = full + '1' + '&Year=' + str(year) + '&Month=' + str(month)
            w = scrape_page(url)
            # Iterate through the monthly_weather dict that came from scrape
            for k, v in w.items():
                # Slice the year out of the key
                y = k[0:4]
                # Get year value to appear as 4 digits
                year_from_page = datetime.datetime.strptime(y, "%Y")
                year_from_page = year_from_page.strftime("%Y")

                # Checks to see if the year from the parsed page
                # Is the intended year to scraped
                # If not, then that means we have worked through
                # all of the weather data from the site.
                # Return the full dictionary with all weather data
                if int(year_from_page) != year:
                    print(url)
                    return myparser.weather
                myparser.weather.update({k: v})


def recent_weather(t):
    """Update weather db."""
    a = 'https://climate.weather.gc.ca/'
    b = 'climate_data/daily_data_e.html?'
    c = 'StationID=27174&timeframe=2&'
    d = 'StartYear=1840&EndYear=2018&Day='
    full = a + b + c + d
    # Set variable to todays date.
    today = date.today()
    # Pull the year out of that.
    current_year = int(today.strftime("%Y"))
    current_month = int(today.strftime("%m"))

    to_year = int(t[0:4])
    print(to_year)
    to_month = int(t[5:7])
    print(to_month)

    if current_year == to_year and current_month == to_month:
        a = full + '1' + '&Year=' + str(current_year) + '&Month='
        url = a + str(current_month)
        w = scrape_page(url)
        # Iterate through the monthly_weather dict that came from scrape
        for k, v in w.items():
            # Slice the year out of the key
            y = k[0:4]
            # Get year value to appear as 4 digits
            year_from_page = datetime.datetime.strptime(y, "%Y")
            year_from_page = year_from_page.strftime("%Y")
            print(url)
            myparser.weather.update({k: v})
            return myparser.weather
    else:
        while current_year >= to_year:
            print(current_year)
            while current_month >= to_month:
                print(current_month)
                a = full + '1' + '&Year=' + str(current_year)
                url = a + '&Month=' + str(current_month)
                w = scrape_page(url)
                # Iterate through the monthly_weather dict from scrape
                for k, v in w.items():
                    # Slice the year out of the key
                    y = k[0:4]
                    # Get year value to appear as 4 digits
                    year_from_page = datetime.datetime.strptime(y, "%Y")
                    year_from_page = year_from_page.strftime("%Y")
                    print(url)
                    myparser.weather.update({k: v})

                current_month -= 1
            current_year -= 1
        return myparser.weather


# recent_weather('2018-04-21')


# scrape_all_weather()

# print(all_weather)
