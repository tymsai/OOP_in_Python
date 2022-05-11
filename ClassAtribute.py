
#class attributes
class WeBrowser:
    connected=True
    def __init__(self, page):
        self.history=[page]
        self.current_page=page
        self.is_incognito=False

chrome=WeBrowser('google.co.in')
fox=WeBrowser('mi.com')

print(chrome.__dict__)
print(fox.__dict__)
print(chrome.connected)
print(fox.connected)
chrome.connected=False
print(chrome.__dict__)
print(fox.__dict__)
WeBrowser.connected=False
print(chrome.__dict__)
print(fox.__dict__)
