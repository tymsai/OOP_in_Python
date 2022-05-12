#class attributes
class WeBrowser:
    def __init__(self, page):
        self.history=[page]
        self.current_page=page
        self.is_incognito=False
    def navigate(self, new_page):
        self.current_page=new_page
        if not self.is_incognito:
            self.history.append(new_page)
    def clear_history(self):
        self.history[:-1]=[]
    @classmethod 
    def with_incognito(cls, page):
        instance=cls(page)
        instance.is_incognito=true
        instance.history=[]
        return instance
chrome=WeBrowser('google.co.in')
fox=WeBrowser('mi.com')
chrome.navigate('dict.com')
chrome.navigate('ab.com')
chrome.clear_history()
print(chrome.__dict__)
print(fox.__dict__)
