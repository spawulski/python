from html.parser import HTMLParser
import urllib.request


class MyHTMLParser(HTMLParser):

    flag = False
    colour_code = ''
    colors = {}

    def handle_starttag(self, tag, attrs):
        for attr in attrs:
            if "style" in attr:
                split = attr[1].split(":")
                self.colour_code = split[1][:-1]
                self.flag = True

    def handle_data(self, data):
        if self.flag:
            if data not in self.colors.keys():
                self.colors[data] = self.colour_code
                self.flag = False


url = "https://www.colorhexa.com/color-names"

myparser = MyHTMLParser()
with urllib.request.urlopen(url) as response:
    html = str(response.read())

myparser.feed(html)

for k, v in myparser.colors.items():
    print(k, v)

