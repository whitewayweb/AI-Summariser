import requests
import re
from datetime import datetime

from bs4 import BeautifulSoup
from summariser import Summarizerr

class Util():

    def __init__(self, url):
        self.url = url

    def scrap(self):
        r = requests.get(self.url, timeout=30)
        return BeautifulSoup(r.content, 'html5lib')

    def scrapAllMeta(self, soup):
        metas = soup.find_all('meta')
        return metas

    def getMeta(self, soup, meta_name):
        metas = self.scrapAllMeta(soup)
        try:
            for meta in metas:
                print(meta)
                if meta.get('name') == meta_name or meta.get('name') == 'og:'+meta_name:
                    return meta.get('content')
                elif meta.get('property') == 'og:'+meta_name:
                    return meta.get('content')
        except:
            return 'None'
            
        
    def getTitle(soup):
        return soup.title

    def getDescription(self, soup):
        return self.getMeta(soup, 'description')
    
    def formatDate(self, s):
        try:
            # formatting the date using strptime() function
            return datetime.strptime(s, '%Y/%m/%d').strftime('%Y-%m-%d')
        except:
            return 'None'

    def getDate(self, soup):
        metas = self.scrapAllMeta(soup)
        #print(metas)
        for meta in metas:
            metaName = meta.get('name')

            if metaName == 'pubdate':
                pd = meta.get('content')
                pubdate = pd[:4] + '-' + pd[4:6] + '-' + pd[6:]
                return pubdate
            elif metaName != None and re.search('date', metaName):
                return self.formatDate(meta.get('content'))
            else:
                return 'None'
            

    def getAuthor(self, soup):
        return self.getMeta(soup, 'author')
    
    def getPublisher(self, soup):
        return self.getMeta(soup, 'site_name')
    
    def getImage(self, soup):
        return self.getMeta(soup, 'image')
    

    def getSummary(self, soup):
        document = []
        for p in soup.find_all('p'):
            para = p.get_text()

            # Regex to count the number of words in a paragraph
            count_words = len(re.findall(r'\w+', para))
            if(count_words > 50):
                document.append(p.get_text())

        article=(' '.join(document)) # Article 
        
        summary = Summarizerr.articleSummary(article)

        return summary