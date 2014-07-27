from HTMLParser import HTMLParser
class MyHTMLParser(HTMLParser):
    def __init__(self, dtag, dattrs):
        HTMLParser.__init__(self)
        self.link=[]
        self.dtag=dtag
        self.dattrs=dattrs
    def handle_starttag(self, tag, attrs):
        if tag==self.dtag:
            if len(attrs)==0:
                pass
            else:
                for (varible, value) in attrs:
                    if varible==self.dattrs:
                        self.link.append(value)

if __name__=='__main__':
    html_code = """
    <a href="www.google.com"> google.com</a>
    <A Href="www.pythonclub.org"> PythonClub </a>
    <A HREF = "www.sina.com.cn"> Sina </a>
    """
    hp = MyHTMLParser('a', 'href')
    hp.feed(html_code)
    hp.close()
    print hp.link
