import requests
from bs4 import BeautifulSoup
import configurations
import constants
import datetime
import time

url_suffix = constants.URL_SUFFIX

marketplace = constants.MARKETPLACE

domain = constants.DOMAIN

product_urls = []

sub_cat_urls = []


# Gets source code of the given URL using BeautifulSoup
def set_bsoup(url, data=None):
    if data is None:
        bsoup = BeautifulSoup(requests.get(url).text, "lxml")
        return bsoup
    else:
        bsoup = BeautifulSoup(requests.get(url, params=data).text, "lxml")
        return bsoup


# Gets product URLs from the page and writes them to a file
def get_prod_url():

    for sub_cat_url in sub_cat_urls:

        category_url_info = sub_cat_url.split('|')

        url = category_url_info[-1]

        name = ''
        for sub_category in category_url_info[:-1]:
            name += sub_category + '|'

        if url not in sub_cat_urls:
            sub_level_count = len(name.split('|'))

            bsoup = set_bsoup(url.replace('facets', 'search').replace(url_suffix, ''))
            tot_pages = int(bsoup.find_all('div', {'class': 'scroll_progress_bar_container'})[0].get('title').split(' ')[-1])

            for page in range(0, tot_pages):

                print name, page, tot_pages

                bsoup = set_bsoup(url.replace('facets', 'search').replace(url_suffix, ''), {'q[page]': page + 1})
                products = bsoup.find_all('div', {'class': 'list_style_row'})

                for product in products:
                    product_url = domain + product.find('a').get('href')
                    product_urls.append(product_url)
                    file.write(marketplace + '|' + domain + main_category + '|' + name + str(
                        sub_level_count) + '|' + product_url + '\n')
                    # file.flush()

            success_urls_file.write(name + url + '\n')
            success_urls_file.flush()


# Finds and traverses sub-categories in the URL
# Gets product URLs in the page, if any are present
def sub_categories(url, name):

    name = name.replace(',', '').encode('utf8','ignore')
    try:
        bsoup = set_bsoup(url)
    except:
        return

    sub_cat_urls.append(name + url)

    kid_cats = bsoup.find_all('ul', {'class': 'cat_kids shown'})

    print name
    if kid_cats:
        kid_cats_list = kid_cats[0].find_all('li')
        for kid in kid_cats_list:
            kid_cat_url = kid.find('a').get('href').replace('search', 'facets') + url_suffix
            kid_cat_name = name + kid.find('a').text.replace('&', 'and').replace(' ', '_').replace(',', '') + '|'
            sub_categories(kid_cat_url, kid_cat_name)

    category_pages_file.write( name + url + '\n')
    category_pages_file.flush()
    # else:


# The control starts here
# Reads the sub-categories under the main-category in BROWSE_ALL_CATEGORIES URL
def sub_cat_collect():
    global main_category

    global file
    file = open(constants.file_names["dolls"]["product"], 'a')

    global sub_cat_urls
    try:

        success_cat_urls= open(constants.file_names["dolls"]["success"]).read().splitlines()
        page_urls = open(constants.file_names["dolls"]["page"]).read().splitlines()
        sub_cat_urls.extend([page_url for page_url in page_urls if page_url not in success_cat_urls])

    except:
        # sub_cat_urls = []
        pass

    global success_urls_file
    success_urls_file = open(constants.file_names["dolls"]["success"],'a')
    
    global category_pages_file
    category_pages_file = open(constants.file_names["dolls"]["page"],'a')

    print 'Dolls Start Time: ' + str(datetime.datetime.now().strftime("%H:%M:%S"))

    start_time = time.time()

    url = constants.ALL_CATEGORIES_URL
    sub_cats = []

    bsoup = set_bsoup(url)
    category = bsoup.find_all('div', {'class': 'category_group_container'})[13]
    main_category = bsoup.find_all('div', {'class': 'category_group_container_mid'})[13].find('a').text
    for x in category.find_all('div', {'class': 'sub_category_list'})[0].find_all('a', {'class', 'link_to_search'}):
        sub_cats.append([x.text.replace('&', 'and').replace(' ', '_'), x.get('href')])
        sub_categories(x.get('href').replace('search', 'facets') + url_suffix,
                       x.text.replace('&', 'and').replace(' ', '_').encode('utf8','ignore') + '|')
        print x.text

    get_prod_url()

    end_time = time.time()
    print 'Dolls End Time: ' + str(datetime.datetime.now().strftime("%H:%M:%S"))
    print 'Dolls Product URLs collected in : ' + str(int(end_time - start_time)) + 's'