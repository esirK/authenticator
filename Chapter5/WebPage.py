from urllib.request import urlopen


class WebPage:
    def __init__(self, url):
        self.url = url
        self._content = None  # Used For Caching a web page

    @property
    def content(self):
        if not self._content:
            print("Retrieving a Web Page")
            self._content = urlopen(self.url).read()
        return self._content
