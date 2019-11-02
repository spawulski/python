from html.parser import HTMLParser
from html.entities import name2codepoint
import urllib.request


class MyHTMLParser(HTMLParser):
    attr_flag = False
    data_counter = 0
    bad_words = ['scheme', 'W3CDTF', 'Google Tag Manager',
                 """Environment and Climate Change Canada -
                  Meteorological Service of Canada""", 'degrees', 'minute',
                 'second', 'North', 'West', 'East', 'South',
                 'World Meteorological Organization',
                 'Transport Canada', 'Comma Separated Values',
                 'Extensible Markup Language', 'metre']


                 #FINISH THE BAD WORDS ARRAY YOU LAZY BASTARD.



    def handle_starttag(self, tag, attrs):
        #print("Start tag:", tag)
        for attr in attrs:
            if "title" in attr:
                if attr[1] not in self.bad_words:
                    self.attr_flag = True
                    #date_array = attr[1].split(" ")
                    #date_array[1] = date_array[1][:-1]
                    print("     attr:", attr)



    def float_checker(self, s):
        try:
            float(s)
            return True
        except Exception as e:
            #print("Exception: ", e)
            return False


    #def handle_endtag(self, tag):
    #    print("End tag :", tag)

    def handle_data(self, data):
        if self.attr_flag:
            if self.float_checker(data.strip()):
                if self.data_counter < 4:
                    print("Data  :", data)
                    #print(self.data_counter)
                    self.data_counter += 1
                else:
                    self.attr_flag = False
                    self.data_counter = 0

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


myparser = MyHTMLParser()

with urllib.request.urlopen('https://climate.weather.gc.ca/climate_data/daily_data_e.html?StationID=27174&timeframe=2&StartYear=1840&EndYear=2018&Day=1&Year=2018&Month=5') as response:
    html = str(response.read())

myparser.feed(html)
