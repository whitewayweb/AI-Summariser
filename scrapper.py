import requests
import re

from bs4 import BeautifulSoup

class Scrapper:
    """
    Scrapper class performs the scrapping operation to fetch the content of any web page.
    It return the content in string format.

    Attributes:
        minWordPara: An integer value indicating minimum number of words required in a paragraph.
        url: A website URL to be scrapped.
    """
    def __init__(self, url):
        """
        Initializes the instance of class Scrapper.

        """

        self.minWordPara = 50
        self.url = url
        self.logger = get_logger()
   
    def is_valid_url(self, url):
        """
        Checks if URL is valid or invalid using regex.

        Args:
            url: A webpage url in string formart

        Returns:
            True if URL is valid otherwise False

        """

        response = requests.get(url, timeout=30)
        if response.status_code == 200:
            self.logger.info("Valid URL")
            return True
        else:        
            self.logger.error("Invalid URL")
            raise HTTPException(status_code=404, detail="URL Not Found or Incorrect")
        
    def extract_article(self):
        """
        Scraps the website URL using Beautifulsoup library to extract the plain text using html5lib parser.
        Removed the unwanted paragrpahs using Regex: (r'\w+', para)

        Returns:
            Returns Scrapped web page as a plain text.

        """
        logger = get_logger()
        self.is_valid_url(self.url)
        
        try:
            r = requests.get(self.url)
            document = []

            # Beautifulsoup object used to extract data from HTML using html5lib parser
            soup = BeautifulSoup(r.content, 'html5lib') 
            for p in soup.find_all('p'):
                para = p.get_text()

                # Regex to count the number of words in a paragraph
                count_words = len(re.findall(r'\w+', para))
                if(count_words > self.minWordPara):
                    document.append(p.get_text())

            article=(' '.join(document))

            logger.info("Article scrapped successfully!")
            return article
        
        except:
            logger.critical("Error occured while scrapping")
            raise HTTPException(status_code=500, detail="Error occured while scrapping")
    
