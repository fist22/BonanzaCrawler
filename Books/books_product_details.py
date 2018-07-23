import requests
from bs4 import BeautifulSoup
import datetime
import time
import configurations
import constants
import json
import re
import os
import MySQLdb

store_to_flag = configurations.STORAGE_FLAG

product_parameters = {}

database = configurations.DATABASE

domain = constants.DOMAIN

path = configurations.PATH


def set_bsoup(url):
    bsoup = BeautifulSoup(requests.get(url).text, "lxml")
    return bsoup


# Writes Product details to configured Database
def to_db(details):
    db = MySQLdb.connect(host=database['host'], user=database['username'], passwd=database['password'],
                         db=database['database'], port=database['port'])
    cursor = db.cursor()
    values = (details['SKU'], details['Date'], details['Time'], details['Marketplace'],
              details['Domain'], details['Category'], details['SubCategory1'], details['SubCategory2'],
              details['SubCategory3'], details['SubCategory4'], details['SubCategory5'], details['SubCategory6'],
              details['SubCategory7'], details['SubCategory8'], details['SubCategory9'],
              json.dumps(details['Condition']),
              details['Saved_Price'], details['Added_Date'], json.dumps(details['Additional_Policies']),
              details['Availability'],
              details['Brand'], json.dumps(details['Description']), details['Discount'], details['Price'],
              details['EAN'], json.dumps(details['Highlights']), details['Id'], details['ImageUrl'],
              details['ISBN'], details['Likes'], details['MPN'], details['Product_Name'],
              details['Reviews'], details['Original_Price'], details['Rating'], details['Shipping_Price'],
              details['Size'], json.dumps(details['Specifications']), details['UPC'], details['URL'],
              details['Quantity'], details['Sold'], json.dumps(details['Return_Policies']), details['Seller_Code'],
              details['Seller_Location'], details['Seller_Name'], details['Seller_Negative_Rating'],
              details['Seller_Neutral_Rating'],
              details['Seller_Positive_Rating'], details['Seller_Overall_Rating'], details['Seller_Rank'],
              details['Seller_Year_Joining'],
              details['Available_Countries'], details['Shipping_Location'], details['Logistic_Name'],
              details['Shipping_Price'],
              details['Shop_Location'], details['Shop_Name'], details['Shop_Sales'], details['Shop_Rating'],
              details['Tax_Info'], details['Visibility'], json.dumps(details['Warranty']), details['Currency'],
              json.dumps(details['Shipping_Policies']))

    # These columns take JSON object as values
    # - ProductCondition
    # - ProductAdditionalPolicies
    # - ProductDescription
    # - ProductHighlights
    # - ProductReturnPolicies
    # - ProductWarranty
    # - ProductSpecifications
    time.sleep(1)

    sql = "INSERT INTO `products` " \
          "(`ProductSKU`,           `ProductDate` ,           `ProductTime`,               `ProductMarketplace`," \
          " `ProductDomain`,        `ProductCategory`,        `ProductSubCategory1`,       `ProductSubCategory2`," \
          " `ProductSubCategory3`,  `ProductSubCategory4`,    `ProductSubCategory5`,       `ProductSubCategory6`," \
          " `ProductSubCategory7`,  `ProductSubCategory8`,    `ProductSubCategory9`,       `ProductCondition`," \
          " `ProductSavedPrice`,    `ProductAddedDate`,       `ProductAdditionalPolicies`, `ProductAvailability`," \
          " `ProductBrand`,         `ProductDescription`,     `ProductDiscountPercentage`, `ProductSellingPrice`, " \
          " `ProductEAN`,           `ProductHighlights`,      `ProductId`,                 `ProductImageUrl`," \
          " `ProductISBN`,          `ProductLikes`,           `ProductMPN`,                 `ProductName`," \
          " `ProductNoOfReviews`,   `ProductOriginalPrice`,   `Productrating`,              `ProductShippingPrice`," \
          " `ProductSize`,          `ProductSpecifications`,  `ProductUPC`,                 `ProductUrl`," \
          " `ProductsAvailable`,    `ProductsSold`,           `ProductReturnPolicies`,      `SellerCode`," \
          " `SellerLocation`,       `SellerName`,             `SellerNegativeRating`,       `SellerNeutralRating`, " \
          " `SellerPositiveRating`, `SellerOverallRating`,    `SellerRank`,                 `SellerYearOfJoining`," \
          " `ShippingAvailableCountries`, `ShippingLocation`, `ShippingLogisticName`,       `ShippingPrice`," \
          " `ShopLocation`,         `ShopName`,               `ShopNoOfSales`,              `ShopRating`," \
          " `TaxInformation`,        `ProductVisibility`,      `ProductWarranty`,            `ProductCurrency`, `ProductShippingPolicies`)" \
          " VALUES" \
          "(%s,            %s,                   %s,                     %s," \
          " %s,            %s,                   %s,                     %s," \
          " %s,            %s,                   %s,                     %s," \
          " %s,            %s,                   %s,                     %s," \
          " %s,            %s,                   %s,                     %s," \
          " %s,            %s,                   %s,                     %s," \
          " %s,            %s,                   %s,                     %s," \
          " %s,            %s,                   %s,                     %s," \
          " %s,            %s,                   %s,                     %s," \
          " %s,            %s,                   %s,                     %s," \
          " %s,            %s,                   %s,                     %s," \
          " %s,            %s,                   %s,                     %s," \
          " %s,            %s,                   %s,                     %s," \
          " %s,            %s,                   %s,                     %s," \
          " %s,            %s,                   %s,                     %s," \
          " %s,            %s,                   %s,                     %s,  %s)"

    cursor.execute(sql, values)
    cursor.close()
    db.commit()


# Writes all Product details to a single file
def to_file(prod):
    products = open(constants.file_names["books"]['output'], 'a')
    products.write(json.dumps(prod) + ',\n')


# Writes all individual Product details to individual files
def to_ind_file(prod, sub_cats):
    file = prod["Id"] + '_' + str(int(time.time())) + '.json'

    location = '\\'

    for x in sub_cats.split('+'):
        location += x.strip().replace('-', '_').replace('&', 'and').replace(' ', '_') + '\\'

    try:
        filename = path + location + file
        os.makedirs(os.path.dirname(filename))
    except:
        pass
    finally:
        file_pointer = open(filename, 'w')
        file_pointer.write(json.dumps(prod, sort_keys=True, indent=4))


def get_details(prod_url_info):
    # Notes thread start time
    thread_start_time = datetime.datetime.now().strftime("%H:%M:%S:%M")
    start_time = time.time()

    line = prod_url_info.split('|')

    directories = ''
    try:
        for category in line[4:-2]:
            directories += category + '+'
    except:
        directories = 'Books'

    product_link = line[-1]

    try:
        product_source = set_bsoup(product_link)
    except:
        return

    # Stores all the default values of the product's details
    product_parameters = {
        "SKU": "NA",  # ss
        "UPC": "Not Applicable",  # ss
        "Rating": "NA",  # ss
        "Shipping_Policies": {'Policies': "Not Applicable"},  # ss
        "Marketplace": "NA",  # ss
        "Description": {'Description': "NA", },  # ss
        "Seller_Name": "NA",  # ss
        "Domain": "NA",  # ss
        "Date": "NA",  # ss
        "Time": "NA",  # ss
        "SubCategory1": "NA",  # ss
        "SubCategory2": "NA",  # ss
        "SubCategory3": "NA",  # ss
        "SubCategory4": "NA",  # ss
        "SubCategory5": "NA",  # ss
        "SubCategory6": "NA",  # ss
        "SubCategory7": "NA",  # ss
        "SubCategory8": "NA",  # ss
        "SubCategory9": "NA",  # ss
        "URL": "NA",  # ss
        "Category": "NA",  # ss
        "Sold": "Not Applicable",  # ss
        "Return_Policies": {'Policies': "Not Applicable"},  # ss
        "Seller_Code": "Not Applicable",  # ss
        "Seller_Location": "Not Applicable",  # ss
        "Seller_Negative_Rating": "Not Applicable",  # ss
        "Seller_Neutral_Rating": "Not Applicable",  # ss
        "Seller_Overall_Rating": "Not Applicable",  # ss
        "Seller_Positive_Rating": "Not Applicable",  # ss
        "Seller_Rank": "Not Applicable",  # ss
        "Seller_Year_Joining": "Not Applicable",  # ss
        "Available_Countries": "Not Applicable",  # ss
        "Shipping_Location": "Not Applicable",  # ss
        "Logistic_Name": "Not Applicable",  # ss
        "Shop_Location": "Not Applicable",  # ss
        "Shop_Name": "Not Applicable",  # ss
        "Shop_Sales": "Not Applicable",  # ss
        "Shop_Rating": "Not Applicable",  # ss
        "Tax_Info": "Not Applicable",  # ss
        "Visibility": "Not Applicable",  # ss
        "ImageUrl": "NA",  # ss
        "ISBN": "Not Applicable",  # ss
        "Brand": "NA",  # ss
        "Price": "NA",  # ss
        "Availability": "NA",  # ss
        "Currency": "MXN",  # ss
        "Seller_Rating": "NA",  # ss
        "EAN": "Not Applicable",  # ss
        "Highlights": {'Highlights': "Not Applicable"},  # ss
        "Id": "Not Applicable",  # ss
        "Product_Name": "NA",  # ss
        "Likes": "Not Applicable",  # ss
        "MPN": "Not Applicable",  # ss
        "Reviews": "NA",  # ss
        "Shipping_Price": "NA",  # ss
        "Saved_Price": "Not Applicable",  # ss
        "Added_Date": "NA",  # ss
        "Additional_Policies": {'Policies': "NA"},  # ss
        "Quantity": "NA",  # ss
        "Condition": {"Condition": "NA"},  # ss
        "Discount": "NA",  # SS
        "Warranty": {'Warranty': "NA"},  # ss
        "Original_Price": "NA",  # ss
        "Size": "NA",  # ss
        "Specifications": {
            "Variants": "NA",
            "Aroma": "NA",
            "Model": "NA",
            "Age": "NA",
            "Guarantee": "NA",
            "Battery_Type": "NA",
            "Physical_Detail": "NA",
            "Mattress_Firmness": "NA",
            "Weight": "NA",
            "Power": "NA",
            "Screen_Size": "NA",
            "Format": "NA",
            "Megapixels": "NA",
            "OS": "NA",
            "Screen": "NA",
            "RAM": "NA",
            "Secondary_Camera": "NA",
            "Processor": "NA",
            "Processor_Speed": "NA",
            "Capacity": "NA",
            "Pieces_In_Set": "NA",
            "Color": "NA",
            "Type": "NA",
            "Shape": "NA",
            "Material": "NA",
            "HDMI_Ports": "NA",
            "Optical_Zoom": "NA",
            "Dimensions": "NA",
            "Other_Sellers": "NA",
        }  # ss
    }

    # Finds product name
    try:
        prod_name = product_source.find_all('div', {'class': 'item_listing_title_and_price'})[0].find(
            'h2').text.replace(' ','_').strip().encode('utf8', 'ignore')
    except:
        prod_name = 'NA'

    # Finds original product price
    try:
        product_original_price = product_source.find('span',{'class':'nondiscount_price'}).text.replace('$','').replace(',','')
        product_parameters["Original_Price"] = product_original_price

    except:
        product_parameters["Original_Price"] = "NA"

    # Finds product selling price
    try:
        prod_price = product_source.find_all('div', {'class': 'item_price'})[0].text.strip().replace('$','').replace(',','').encode('utf8', 'ignore')
    except:
        prod_price = "NA"


    # Finds product's shop name
    try:
        shop_name = product_source.find_all('div', {'class': 'booth_link'})[0].find('a').text.replace("'s booth",
                                                                                           '').replace(' ','_').strip().encode('utf8',
                                                                                                              'ignore')
    except:
        shop_name = "NA"

    try:
        shop_rating = product_source.find_all('div', {'class': 'feedback_rating'})[0].find('a').text.replace('%  rating','').encode('utf8', 'ignore')
    except:
        shop_rating = "NA"


    # Finds product's decription
    try:
        description_url = product_source.find_all('div', {'class': 'plain_text_description'})[0].get('data-url')

        descr_page = set_bsoup(domain + description_url)

        description = descr_page.find('body').text.encode('utf8','ignore')
    except:
        description = "NA"


    # Finds Return Policies
    try:
        return_policy = product_source.find_all('div',{'class': 'item_listing_additional_details_section'})[1].text.strip()
        return_policy = return_policy.replace('Return policy','',).strip().encode('utf8','ignore')
    except:
        return_policy = "NA"



    # Finds shipping policies
    try:
        shipping_policy = product_source.find_all('div',{'class': 'item_listing_additional_details_section'})[0].text.strip()
        shipping_policy = shipping_policy.replace('Shipping options','').strip().encode('utf8','ignore')
        shipping_policy = re.sub('(\s+)' , ' ', shipping_policy).encode('utf8','ignore')
    except:
        shipping_policy = "NA"


    product_parameters["Product_Name"] = prod_name
    product_parameters["Price"] = prod_price
    product_parameters["Shop_Name"] = shop_name
    product_parameters["Shop_Rating"] = shop_rating
    product_parameters["Description"]["Description"] = description
    product_parameters['Date'] = datetime.datetime.now().strftime("%d-%m-%y")
    product_parameters['Time'] = datetime.datetime.now().strftime("%H:%M:%S")
    product_parameters["Marketplace"] = constants.MARKETPLACE
    product_parameters["Domain"] = constants.DOMAIN
    product_parameters["Category"] = line[3]
    product_parameters["Return_Policies"]["Policies"] = return_policy
    product_parameters["Shipping_Policies"]["Policies"] = shipping_policy


    sub_category_number = 1

    # Assigns sub-category values to product details
    try:
        for sub_category in line[4:-2]:
            product_parameters['SubCategory{}'.format(sub_category_number)] = sub_category
            sub_category_number += 1
    except:
        pass

    # Reads all the traits from the table
    try:
        traits_table = product_source.find_all('table',{'class':'extended_info_table'})[0].find_all('td')
        no_of_rows = len(traits_table)
        for row in range(0, no_of_rows, 2):
            key = traits_table[row].text.strip().encode('utf8', 'ignore')
            value = traits_table[row + 1].text.strip().encode('utf8', 'ignore')
            if 'Quantity' in key:
                product_parameters["Quantity"] = value
            elif 'Condition' in key:
                product_parameters["Condition"]["Condition"] = value
            elif 'Size' in key:
                product_parameters["Size"] = value
            elif 'Material' in key:
                product_parameters["Specifications"]["Material"] = value
            elif 'UPC' in key:
                product_parameters["UPC"] = value
            elif 'Framed' in key:
                product_parameters["Highlights"]["Frame"] = value
            elif 'Features' in key:
                product_parameters["Highlights"]["Features"] = value
            elif 'MPN' in key:
                product_parameters["MPN"] = value
            elif 'weight' in key:
                product_parameters["Specifications"]["Weight"] = value
            elif 'Year' in key:
                product_parameters["Highlights"]["Year"] = value
            elif 'Brand' in key:
                product_parameters["Brand"] = value
            elif 'Date of Creation' in key:
                product_parameters["Highlights"]["Date of Creation"] = value
            elif 'Region of Origin' in key:
                product_parameters["Highlights"]["Region of Origin"] = value
            elif 'Style' in key:
                product_parameters["Highlights"]["Style"] = value
            elif 'Original' in key:
                product_parameters["Highlights"]["Original/Reproduction"] = value
            elif 'Signed' in key:
                product_parameters["Highlights"]["Signed"] = value
            elif 'Listed By' in key:
                product_parameters["Highlights"]["Listed By"] = value
            elif 'Subject' in key:
                product_parameters["Highlights"]["Subject"] = value
            elif 'Artist' in key:
                product_parameters["Highlights"]["Artist"] = value
            elif 'Medium' in key:
                product_parameters["Highlights"]["Medium"] = value
            elif 'Artist' in key:
                product_parameters["Highlights"]["Artist"] = value
            elif 'Height' in key:
                product_parameters["Specifications"]["Height"] = value
            elif 'Width' in key:
                product_parameters["Specifications"]["Width"] = value
            elif 'Color' in key:
                product_parameters["Specifications"]["Color"] = value
            elif 'Reviews' in key:
                continue
            elif 'Category' in key:
                continue
            else:
                print 'Traits-table- ',key + ' ' + value
    except:
        pass


    # Reads all the listing details from the table
    try:
        listing_table = product_source.find_all('table',{'class':'extended_info_table'})[1].find_all('td')
        no_of_rows = len(listing_table)
        for row in range(0, no_of_rows, 2):
            key = listing_table[row].text.strip().encode('utf8', 'ignore')
            value = listing_table[row + 1].text.strip().encode('utf8', 'ignore')
            if 'Posted for sale' in key:
                product_parameters["Added_Date"] = value
            elif 'Item number' in key:
                product_parameters["Id"] = value
            elif 'Shipping discount' in key:
                product_parameters["Shipping_Price"] = value
            elif 'Price discount' in key:
                product_parameters["Discount"] = value
            elif 'Seller policies' in key:
                product_parameters["Seller_Name"] = listing_table[row + 1].find('a').get('href').split('/')[-1]
            else:
                print 'Listing-table- ',key, value
    except:
        pass


    product_parameters['Date'] = datetime.datetime.now().strftime("%d-%m-%y")
    product_parameters['Time'] = datetime.datetime.now().strftime("%H:%M:%S")


    # print json.dumps(product_parameters, sort_keys=True, indent=4)

    # Storage location and type of product details
    if store_to_flag == constants.WRITE_TO_SINGLE_FILE:
        to_file(product_parameters)
    elif store_to_flag == constants.WRITE_TO_DATABASE:
        to_db(product_parameters)
    elif store_to_flag == constants.WRITE_TO_INDIVIDUAL_FILE:
        to_ind_file(product_parameters, directories)



    thread_end_time = datetime.datetime.now().strftime("%H:%M:%S:%M")
    end_time = time.time()

    # Prints product URL information, thread start time, end time and toal time taken for completion
    # the first number is serial
    print prod_url_info + ' | ' + thread_start_time + ' | ' + thread_end_time + '|', int(end_time - start_time), '\bs'



