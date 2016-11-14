import re


def filter_urls(text, domain='williams.edu'):
    """
    returns a list of urls found in the string 'text' that are
    (1) not media files and (2) within the specified domain.
    Args:
        text (str): a string that represents the text of a webpage
        domain (str): a <sub-domain> + '.' + <top-level domain>
    """
    def extension_is_valid(url):
        EXTS = ["jpg", "jpeg", "svg", "png", "pdf",
                "gif", "bmp", "mp3", "dvi"]
        for e in EXTS:
            if url.casefold().endswith(e):
                return False
        return True

    domain, tld = domain.split(".")
    # '<a' + _not >_ + 'href=' + _quote_ + 'http://' + _nonquote_ + _quote_
    REGEX = '''<a[^>]+href\s*=\s*["'](http://.+{}\.{}[^"']+?)["']'''
    REGEX = re.compile(REGEX.format(domain, tld))

    urls = re.findall(REGEX, text)
    return [url for url in urls if extension_is_valid(url)]


def filter_emails(text):
    """
    returns a list of emails found in the string 'text'
    """
    LOCALPART = ['''[a-zA-z0-9]''']
    MIDDLEPART = ['''[a-zA-Z0-9]*\. ''']
    DOM = [a-zA-Z]{2,}
    ACCEPT = '''[!#$%&'*+-/=?^_`{|}~;]'''
    REGEX = '''LOCALPART + {@} + MIDDLEPART + DOM 

def filter_phones(text):
    """
    returns a list of uniformly formatted phone numbers extracted from
    the string 'text'
    """
    pass
