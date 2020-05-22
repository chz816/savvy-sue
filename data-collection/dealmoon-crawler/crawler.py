from bs4 import BeautifulSoup


from datetime import datetime as dt2
import urllib.request
import pandas as pd
import requests.exceptions
from urllib.parse import urlsplit
from collections import deque
import os
import html.parser
import os.path


## Mostly adapted from:
## https://www.freecodecamp.org/news/how-to-build-a-url-crawler-to-map-a-website-using-python-6a287be1da11/


def getDomain(url):
    return (url.split("://")[1].split("/")[0])


def scrape(retailer, url, domain, save_every=15):
    '''
    url: the URL of the homepage we wish to scrape
    retailer: the name of the Retailer we wish to preserve for human readability
    domain: the domain of the retailer's store to avoid entering foreign stores, blogs, or investor pages
    save_every: number of minutes between back-up saves, default is 15, 0 will never save till completion
       - save_every multiplies 60 for a seconds value, so fractions of minutes is also acceptable
       - can at lowest save after every URL parse, but this is HIGHLY NOT recommended

    '''

    # a queue of urls to be crawled next
    links_to_visit = deque([url])

    # a set of urls that we have already processed
    links_visited = set()

    # On the target site
    local_urls = set(domain)

    # Outside the target site
    foreign_urls = set()

    # Broken urls
    broken_urls = set()

    # Agent to declare to the website
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'

    ## And now variables for the desired data: ##
    all_products = []
    performance_data = []
    iteration = 0
    now = dt2.now()
    d = {"Iteration": iteration,
         "URL_Processed": "",
         "Queue_Size": 1,
         "Visited_Sites": 0,
         "Products": len(all_products),
         "Timestamp": str(now)
         }

    performance_data.append(d)

    never_save = False
    if (save_every > 0):
        save_every = 60 * save_every  # 15 minutes default
    else:
        never_save = True
    last_save = now

    # process urls one by one until we exhaust the queue
    while len(links_to_visit):
        iteration += 1

        # move url from the queue to processed url set
        url = links_to_visit.popleft()
        links_visited.add(url)
        # print the current url
        print("Processing %s" % url)

        try:
            request = urllib.request.Request(url, headers={'User-Agent': user_agent})
            response = urllib.request.urlopen(request)

        except(requests.exceptions.MissingSchema, requests.exceptions.ConnectionError, requests.exceptions.InvalidURL,
               requests.exceptions.InvalidSchema):
            # add broken urls to it’s own set, then continue
            broken_urls.add(url)
            continue
        except:
            print("Unknown error on URL: " + str(url))
            continue

        # extract base url to resolve relative links
        parts = urlsplit(url)
        base = "{0.netloc}".format(parts)
        strip_base = base.replace("www.", "")
        base_url = "{0.scheme}://{0.netloc}".format(parts)
        path = url[:url.rfind('/') + 1] if '/' in parts.path else url

        soup = BeautifulSoup(response, 'html.parser')

        # here html is the string type
        output_str = soup.prettify("utf-8").decode('utf-8')

        # here the output is the html file
        output_html = html.unescape(output_str)

        output = BeautifulSoup(output_html, "lxml")

        link_elements = output.find_all(
            'p', attrs={"class": 'brief'}
        )

        # 20 records on each website
        result = []
        for element in link_elements:
            result.append(element.text.strip().replace('              ',' '))
        #print(result)

        # today: apr. 23
        date_elements = output.find_all(
            'span', attrs={"class": 'ib published-date'}
        )

        date = []
        for element in date_elements:
            date.append(element.text.strip())
        #print(date[1])

        final = pd.DataFrame({'date': date, 'information': result})

        filename = "data/"+store + "-promotion.xlsx"
        if not os.path.exists(filename):
            # file doesn't exist
            final.to_excel(filename, index=None)
        else:
            # file exists
            current = pd.read_excel(filename)
            final = pd.concat([current, final], axis=0)
            final.to_excel(filename, index=None)


if __name__ == '__main__':
    # for nordstrom from dealmoon
    store = 'nordstrom'
    for i in range(1,101,1):
        if i == 1:
            url = 'https://www.dealmoon.com/en/stores/'+store
            scrape(retailer=store, url=url, domain="www.dealmoon.com", save_every=15)
        else:
            url = 'https://www.dealmoon.com/en/stores/'+store + '?p='+str(i)
            scrape(retailer=store, url=url, domain="www.dealmoon.com", save_every=15)
