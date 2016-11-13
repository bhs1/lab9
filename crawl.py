import sys
import socket
import urllib.request
import re

class WebLink:
    def __init__(self, url, depth):
        """
        Initializes a WebLink's state including data structures to store:
        - the set of urls in the WebLink's source
        - the set of emails in the WebLink's source
        - the set of phone numbers in the WebLink's source
        Args:
            url (str): the url to search
            depth (int): how many links have been traversed to reach this url
        """

    @staticmethod
    def filter_urls(text):
        """
        returns a list of urls found in the string 'text'
        """
        def extension_is_valid(url):
            """returns True if url is not a media file"""
            return True
        
    @staticmethod
    def filter_emails(text):
        """
        returns a list of emails found in the string 'text'
        """

    @staticmethod
    def filter_phones(text):
        """
        returns a list of uniformly formatted phone numbers extracted from
        the string 'text'
        """
        def format_phone(area, base, ext):
            """returns a uniformly formatted phone number as a string"""
            return "{}-{}-{}".format(area, base, ext)

    def crawl(self):
        """
        fetch this WebLink object's webpage text and populate its content
        """

class WebCrawler:
    def __init__(self, base_url, max_links=50, max_depth=5):
        """
        Initialize the data structures required to crawl the web.
        Args:
           base_url (str): the starting point of our crawl
           max_links (int): after traversing this many links, stop the crawl
           max_depth (int): only traverse this many links deep in any direction
        """

    def crawl(self):
        """
        starting from self._base_url and until stopping conditions are met,
        creates WebLink objects and recursively explores their links.
        """

    def all_emails(self):
        """
        returns the set of all email addresses harvested during a
        successful crawl
        """

    def all_phones(self):
        """
        returns the set of all phone numbers harvested during a
        successful crawl
        """

    def all_urls(self):
        """
        returns the set of all urls traversed during a crawl
        """

    def output_results(self, filename):
        """
        In an easy-to-read format, writes the report of a successful crawl
        to the file specified by 'filename'.
        This includes the starting url, the set of urls traversed,
        all emails encountered, and the set of phone numbers (recorded in
        a standardized format of NPA-NXX-XXXX).
        """

def usage():
    print("python3 crawl.py <base_url> <report_file>")
    print("\tbase_url: the initial url to crawl")
    print("\treport_file: file where all results are written")

if __name__ == '__main__':

    if len(sys.argv) < 3:
        usage()
        sys.exit(1)

    base_url = sys.argv[1]
    report_path = sys.argv[2]
    
    crawl = WebCrawler(base_url, 15, 2) # until you are confident, use
                                        # small max_links, max_depth
    crawl.crawl()
    crawl.output_results(report_path)
