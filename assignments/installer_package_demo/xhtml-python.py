from html.parser import HTMLParser
import urllib.request

class MyHTMLParser(HTMLParser):

    def handle_data(self, data):
        if "Address" in data:
            split = data.split(" ")
            print(split[len(split)-1])


myparser = MyHTMLParser()
with urllib.request.urlopen("http://checkip.dyndns.org/") as response:
    html = str(response.read())


myparser.feed(html)

