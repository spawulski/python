from html.parser import HTMLParser
from html.entities import name2codepoint
import urllib.request
import datetime


class MyHTMLParser(HTMLParser):
    attr_flag = False
    data_counter = 0
    weather = {}
    date = ''
    day = ''
    min = ''
    max = ''
    mean = ''

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
                 'Environment and Climate Change Canada - Meteorological Service of Canada',
                 'Average', 'Extreme'
                 ]



    def handle_starttag(self, tag, attrs):
        #print("Start tag:", tag)
        for attr in attrs:
            if "title" in attr:
                if attr[1] not in self.bad_words:
                    #self.date = attr[1]
                    self.date = datetime.datetime.strptime(attr[1], '%B %d, %Y').strftime('%Y-%m-%d')
                    self.attr_flag = True
                    #date_array = attr[1].split(" ")
                    #date_array[1] = date_array[1][:-1]
                    #print("     attr:", attr)



    def float_checker(self, s):
        try:
            float(s)
            return True
        except Exception as e:
            #print("Exception: ", e)
            return False


    def data_reset(self):
        self.day = ''
        self.max = ''
        self.min = ''
        self.mean = ''


    #def handle_endtag(self, tag):
    #    print("End tag :", tag)

    def handle_data(self, data):
        if self.attr_flag:
            if self.float_checker(data.strip()):
                if self.data_counter < 4:
                    #print("Data  :", data)
                    if self.data_counter == 0:
                        self.day = data
                    if self.data_counter == 1:
                        self.max = data
                    if self.data_counter == 2:
                        self.min = data
                    if self.data_counter == 3:
                        self.mean = data

                    #print(self.data_counter)
                    self.data_counter += 1
                else:
                    daily_temps = {'Max': self.max, 'Min': self.min, 'Mean': self.mean}
                    self.weather.update({self.date: daily_temps})
                    self.attr_flag = False
                    self.data_counter = 0
                    self.data_reset()


    #def handle_comment(self, data):
    #    print("Comment  :", data)

    #def handle_entityref(self, name):
    #    c = chr(name2codepoint[name])
#        print("Named ent:", c)

#    def handle_charref(self, name):
#        if name.startswith('x'):
#            c = chr(int(name[1:], 16))
#        else:
#            c = chr(int(name))
#        print("Num ent  :", c)

#    def handle_decl(self, data):
#        print("Decl     :", data)


#url = "https://climate.weather.gc.ca/climate_data/daily_data_e.html?StationID=27174&timeframe=2&StartYear=1840&EndYear=2018&Day=1&Year=2018&Month=5"

years = ['1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003',
         '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011',
         '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019']

#months = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']


myparser = MyHTMLParser()

weather = {}
all_weather = {}

def scrape_page(url):
    with urllib.request.urlopen(url) as response:
        html = str(response.read())

    myparser.feed(html)

    for k, v in myparser.weather.items():
        weather.update({k: v})

    return weather

def scrape_all_weather():
    for year in range(2019, 2015, -1):
        print(str(year))
        for month in range(12, 0, -1):
            print(str(month))
            #for day in range(31, 0, -1):
            #    print(str(day))
            url = 'https://climate.weather.gc.ca/climate_data/daily_data_e.html?StationID=27174&timeframe=2&StartYear=1840&EndYear=2018&Day=' + '1' + '&Year=' + str(year) + '&Month=' + str(month)
            #url = 'https://climate.weather.gc.ca/climate_data/daily_data_e.html?StationID=27174&timeframe=2&StartYear=1840&EndYear=2018&Day=1&Year=' + str(year) + '&Month=' + str(month)
            w = scrape_page(url)
            for k, v in w.items():
                all_weather.update({k: v})

    return all_weather


#scrape_all_weather()

#print(all_weather)
