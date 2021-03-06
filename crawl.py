import sys
from filters import filter_urls, filter_emails, filter_phones
import requests


class WebPage:

    def __init__(self, url):
        """
        Initializes a WebPage's state with the url, and populates:
        - the set of urls in the WebPages's source
        - the set of emails in the WebPages's source
        - the set of phone numbers in the WebPages's source
        Args:
            url (str): the url to search
        """
        pass

    def __hash__(self):
        """Return the hash of the URL"""
        return hash(self.url())

    def __eq__(self, page):
        """
        return True if and only if the url of this page equals the url
        of page.
        Args:
            page (WebPage): a WebPage object to compare
        """
        pass

    def populate(self):
        """
        fetch this WebPage object's webpage text and populate its content
        """
        pass

    def url(self):
        """return the url asssociated with the WebPage"""
        pass

    def phone_numbers(self):
        """return the phone numbers associated with the WebPage"""
        pass

    def emails(self):
        """return the email addresses associated with the WebPage"""
        pass

    def urls(self):
        """return the URLs associated with the WebPage"""
        pass


class WebCrawler:
    def __init__(self, base_url, max_links=50):
        """
        Initialize the data structures required to crawl the web.
        Args:
           base_url (str): the starting point of our crawl
           max_links (int): after traversing this many links, stop the crawl
        """

    def crawl(self):
        """
        starting from self._base_url and until stopping conditions are met,
        creates WebPage objects and recursively explores their links.
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

    crawl = WebCrawler(base_url, 15) # until you are confident use small max_links
    crawl.crawl()
    crawl.output_results(report_path)
