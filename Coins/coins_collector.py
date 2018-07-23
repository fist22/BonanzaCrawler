from multiprocessing.pool import ThreadPool
import constants
import configurations
import coins_product_details


def collect_data():
    prod_url_info = []

    # Collects product URLs from file
    prod_urls_file = open(constants.file_names["coins"]["product"]).read().splitlines()

    # Collects only NO_OF_PRODUCTS(from configurations.py) product URL info from file
    if configurations.PRODUCTS_FLAG == constants.FEW_PRODUCTS:
        for products in range(configurations.NO_OF_PRODUCTS):
            prod_url_info.append(str(products + 1) + '| ' + prod_urls_file[products])

    # Collects all product URLs from file
    elif configurations.PRODUCTS_FLAG == constants.ALL_PRODUCTS:
        sno = 1
        for line in prod_urls_file:
            prod_url_info.append(str(sno) + ' | ' + line)
            sno += 1

    ThreadPool().map(coins_product_details.get_details, prod_url_info)

collect_data()