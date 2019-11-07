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
                    #print(a)
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
        """Reset variables used in dict creation."""
        self.day = ''
        self.max = ''
        self.min = ''
        self.mean = ''

    def handle_data(self, data):
        if self.attr_flag:
            if self.float_checker(data.strip()):
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
                else:
                    daily_temps = {'Max': self.max, 'Min': self.min, 'Mean': self.mean}
                    self.weather.update({self.date: daily_temps})
                    self.temp_weather.update({self.date: daily_temps})
                    self.attr_flag = False
                    self.data_counter = 0
                    self.data_reset()


myparser = MyHTMLParser()

all_weather = {}


def scrape_page(url):
    see_if_this_fix = {}
    see_if_this_fix = myparser.temp_weather
    myparser.temp_weather.clear()
    with urllib.request.urlopen(url) as response:
        html = str(response.read())

    myparser.feed(html)
    return see_if_this_fix
    #print(myparser)

    #for k, v in myparser.weather.items():
        #print(k)
    #    see_if_this_fix.update({k: v})

    #return see_if_this_fix


def scrape_all_weather():
    today = date.today()
    current_year = today.strftime("%Y")
    for year in range(int(current_year), 0, -1):
        print(str(year))
        for month in range(12, 0, -1):
            print(str(month))
            #for day in range(31, 0, -1):
            #    print(str(day))
            url = 'https://climate.weather.gc.ca/climate_data/daily_data_e.html?StationID=27174&timeframe=2&StartYear=1840&EndYear=2018&Day=' + '1' + '&Year=' + str(year) + '&Month=' + str(month)
            #url = 'https://climate.weather.gc.ca/climate_data/daily_data_e.html?StationID=27174&timeframe=2&StartYear=1840&EndYear=2018&Day=1&Year=' + str(year) + '&Month=' + str(month)
            w = scrape_page(url)
            for k, v in w.items():
                #print(k, v)
                thing = k[0:4]
                year_from_page = datetime.datetime.strptime(thing, "%Y")
                year_from_page = year_from_page.strftime("%Y")
                print("Date from webpage: " + str(year_from_page))
                print("year from loop:    " + str(year))
                if int(year_from_page) != year:
                    print(url)
                    return myparser.weather
                myparser.weather.update({k: v})



#scrape_all_weather()

##print(all_weather)
