# Updated url_expander.py

import requests
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO)

class URLExpander:
    def __init__(self):
        self.session = requests.Session()

    def expand_url(self, short_url):
        try:
            response = self.session.head(short_url, allow_redirects=True)
            response.raise_for_status()  # Raise an error for bad responses

            # Log the expansion
            logging.info(f"Expanded URL: {response.url}")
            return response.url
        except requests.exceptions.RequestException as e:
            logging.error(f"Error expanding URL {short_url}: {e}")
            return None

    def expand_urls(self, urls):
        return [self.expand_url(url) for url in urls]

# Example usage
if __name__ == '__main__':
    url_expander = URLExpander()
    urls = ['http://short.url/example1', 'http://short.url/example2']
    expanded_urls = url_expander.expand_urls(urls)
    print(expanded_urls)
