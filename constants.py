import configurations

# This is the path where data of products will be stored IF
# configured to store each product's detail in individual file
#
# Change this as per the requirements
# This is tested on Windows File System

PATH = configurations.PATH

#
MARKETPLACE = "Bonanza_Us"

DOMAIN = 'https://www.bonanza.com'

WRITE_TO_SINGLE_FILE = 1

WRITE_TO_DATABASE = 2

WRITE_TO_INDIVIDUAL_FILE = 3

FEW_PRODUCTS = 1

ALL_PRODUCTS = 0


URL_SUFFIX = '&q[gallery_style]=1&q[page]=1&q[per_page]=48&q[sort_by]=relevancy'

ALL_CATEGORIES_URL = 'https://www.bonanza.com/booths/browse_categories'


CURRENCY = "USD"

# This Dicttionary has 'Category' as key and corresponding dictionary
# has FILE_NAMES
#
# page - stores 'SUB_CATEGORY' URLs
# product - stores 'PRODUCT' URLs
# success - stores successfully completed 'SUB_CATEGORY' URLs
# output - stores respective OUTPUT file name
file_names = {
    "antiques": {
        "page": PATH + "\\antiques\\antiques_page_urls.txt",
        "product": PATH + "\\antiques\\antiques_prod_urls.txt",
        "success": PATH + "\\antiques\\antiques_success.txt",
        "output": PATH + "\\antiques\\antiques_products.json"
    },
    "art": {
        "page": PATH + "\\art\\art_page_urls.txt",
        "product": PATH + "\\art\\art_prod_urls.txt",
        "success": PATH + "\\art\\art_success.txt",
        "output": PATH + "\\art\\art_products.json"
    },
    "baby": {
        "page": PATH + "\\baby\\baby_page_urls.txt",
        "product": PATH + "\\baby\\baby_prod_urls.txt",
        "success": PATH + "\\baby\\baby_success.txt",
        "output": PATH + "\\baby\\baby_products.json"
    },
    "books": {
        "page": PATH + "/books/books_page_urls.txt",
        "product": PATH + "/books/books_prod_urls.txt",
        "success": PATH + "/books/books_success.txt",
        "output": PATH + "/books/books_products.json"
    },
    "business": {
        "page": PATH + "/business/business_page_urls.txt",
        "product": PATH + "/business/business_prod_urls.txt",
        "success": PATH + "/business/business_success.txt",
        "output": PATH + "/business/business_products.json"
    },
    "cameras": {
        "page": PATH + "/cameras/cameras_page_urls.txt",
        "product": PATH + "/cameras/cameras_prod_urls.txt",
        "success": PATH + "/cameras/cameras_success.txt",
        "output": PATH + "/cameras/cameras_products.json"
    },
    "cell_phones": {
        "page": PATH + "\cell_phones\cell_phones_page_urls.txt",
        "product": PATH + "\cell_phones\cell_phones_prod_urls.txt",
        "success": PATH + "\cell_phones\cell_phones_success.txt",
        "output": PATH + "\cell_phones\cell_phones_products.json"
    },
    "coins": {
        "page": PATH + "/coins/coins_page_urls.txt",
        "product": PATH + "/coins/coins_prod_urls.txt",
        "success": PATH + "/coins/coins_success.txt",
        "output": PATH + "/coins/coins_products.json"
    },
    "collectibles": {
        "page": PATH + "\collectibles\collectibles_page_urls.txt",
        "product": PATH + "\collectibles\collectibles_prod_urls.txt",
        "success": PATH + "\collectibles\collectibles_success.txt",
        "output": PATH + "\collectibles\collectibles_products.json"
    },
    "computers": {
        "page": PATH + "/computers/computers_page_urls.txt",
        "product": PATH + "/computers/computers_prod_urls.txt",
        "success": PATH + "/computers/computers_success.txt",
        "output": PATH + "/computers/computers_products.json"
    },
    "consumer_electronics": {
        "page": PATH + "/consumer_electronics/consumer_electronics_page_urls.txt",
        "product": PATH + "/consumer_electronics/consumer_electronics_prod_urls.txt",
        "success": PATH + "/consumer_electronics/consumer_electronics_success.txt",
        "output": PATH + "/consumer_electronics/consumer_electronics_products.json"
    },
    "crafts": {
        "page": PATH + "\crafts\crafts_page_urls.txt",
        "product": PATH + "\crafts\crafts_prod_urls.txt",
        "success": PATH + "\crafts\crafts_success.txt",
        "output": PATH + "\crafts\crafts_products.json"
    },
    "digital_goods": {
        "page": PATH + "\digital_goods\digital_goods_page_urls.txt",
        "product": PATH + "\digital_goods\digital_goods_prod_urls.txt",
        "success": PATH + "\digital_goods\digital_goods_success.txt",
        "output": PATH + "\digital_goods\digital_goods_products.json"
    },
    "dolls": {
        "page": PATH + "\dolls\dolls_page_urls.txt",
        "product": PATH + "\dolls\dolls_prod_urls.txt",
        "success": PATH + "\dolls\dolls_success.txt",
        "output": PATH + "\dolls\dolls_products.json"
    },
    "dvds_movies": {
        "page": PATH + "\dvds_movies\dvds_movies_page_urls.txt",
        "product": PATH + "\dvds_movies\dvds_movies_prod_urls.txt",
        "success": PATH + "\dvds_movies\dvds_movies_success.txt",
        "output": PATH + "\dvds_movies\dvds_movies_products.json"
    },
    "entertainment": {
        "page": PATH + "\entertainment\entertainment_page_urls.txt",
        "product": PATH + "\entertainment\entertainment_prod_urls.txt",
        "success": PATH + "\entertainment\entertainment_success.txt",
        "output": PATH + "\entertainment\entertainment_products.json"
    },
    "everything_else": {
        "page": PATH + "\everything_else\everything_else_page_urls.txt",
        "product": PATH + "\everything_else\everything_else_prod_urls.txt",
        "success": PATH + "\everything_else\everything_else_success.txt",
        "output": PATH + "\everything_else\everything_else_products.json"
    },
    "fashion": {
        "page": PATH + "\\fashion\\fashion_page_urls.txt",
        "product": PATH + "\\fashion\\fashion_prod_urls.txt",
        "success": PATH + "\\fashion\\fashion_success.txt",
        "output": PATH + "\\fashion\\fashion_products.json"
    },
    "health_beauty": {
        "page": PATH + "\health_beauty\health_beauty_page_urls.txt",
        "product": PATH + "\health_beauty\health_beauty_prod_urls.txt",
        "success": PATH + "\health_beauty\health_beauty_success.txt",
        "output": PATH + "\health_beauty\health_beauty_products.json"
    },
    "home_garden": {
        "page": PATH + "\home_garden\home_garden_page_urls.txt",
        "product": PATH + "\home_garden\home_garden_prod_urls.txt",
        "success": PATH + "\home_garden\home_garden_success.txt",
        "output": PATH + "\home_garden\home_garden_products.json"
    },
    "jewellery": {
        "page": PATH + "\jewellery\jewellery_page_urls.txt",
        "product": PATH + "\jewellery\jewellery_prod_urls.txt",
        "success": PATH + "\jewellery\jewellery_success.txt",
        "output": PATH + "\jewellery\jewellery_products.json"
    },
    "music": {
        "page": PATH + "\music\music_page_urls.txt",
        "product": PATH + "\music\music_prod_urls.txt",
        "success": PATH + "\music\music_success.txt",
        "output": PATH + "\music\music_products.json"
    },
    "musical_instruments": {
        "page": PATH + "\musical_instruments\musical_instruments_page_urls.txt",
        "product": PATH + "\musical_instruments\musical_instruments_prod_urls.txt",
        "success": PATH + "\musical_instruments\musical_instruments_success.txt",
        "output": PATH + "\musical_instruments\musical_instruments_products.json"
    },
    "parts_accessories": {
        "page": PATH + "\parts_accessories\parts_accessories_page_urls.txt",
        "product": PATH + "\parts_accessories\parts_accessories_prod_urls.txt",
        "success": PATH + "\parts_accessories\parts_accessories_success.txt",
        "output": PATH + "\parts_accessories\parts_accessories_products.json"
    },
    "pet_supplies": {
        "page": PATH + "\pet_supplies\pet_supplies_page_urls.txt",
        "product": PATH + "\pet_supplies\pet_supplies_prod_urls.txt",
        "success": PATH + "\pet_supplies\pet_supplies_success.txt",
        "output": PATH + "\pet_supplies\pet_supplies_products.json"
    },
    "pottery": {
        "page": PATH + "\pottery\pottery_page_urls.txt",
        "product": PATH + "\pottery\pottery_prod_urls.txt",
        "success": PATH + "\pottery\pottery_success.txt",
        "output": PATH + "\pottery\pottery_products.json"
    },
    "speciality_services": {
        "page": PATH + "\speciality_services\speciality_services_page_urls.txt",
        "product": PATH + "\speciality_services\speciality_services_prod_urls.txt",
        "success": PATH + "\speciality_services\speciality_services_success.txt",
        "output": PATH + "\speciality_services\speciality_services_products.json"
    },
    "sporting_goods": {
        "page": PATH + "/sporting_goods/sporting_goods_page_urls.txt",
        "product": PATH + "/sporting_goods/sporting_goods_prod_urls.txt",
        "success": PATH + "/sporting_goods/sporting_goods_success.txt",
        "output": PATH + "/sporting_goods/sporting_goods_products.json"
    },
    "sports_mem": {
        "page": PATH + "\sports_mem\sports_mem_page_urls.txt",
        "product": PATH + "\sports_mem\sports_mem_prod_urls.txt",
        "success": PATH + "\sports_mem\sports_mem_success.txt",
        "output": PATH + "\sports_mem\sports_mem_products.json"
    },
    "stamps": {
        "page": PATH + "\stamps\stamps_page_urls.txt",
        "product": PATH + "\stamps\stamps_prod_urls.txt",
        "success": PATH + "\stamps\stamps_success.txt",
        "output": PATH + "\stamps\stamps_products.json"
    },
    "tickets": {
        "page": PATH + "\\tickets\\tickets_page_urls.txt",
        "product": PATH + "\\tickets\\tickets_prod_urls.txt",
        "success": PATH + "\\tickets\\tickets_success.txt",
        "output": PATH + "\\tickets\\tickets_products.json"
    },
    "toys": {
        "page": PATH + "\\toys\\toys_page_urls.txt",
        "product": PATH + "\\toys\\toys_prod_urls.txt",
        "success": PATH + "\\toys\\toys_success.txt",
        "output": PATH + "\\toys\\toys_products.json"
    },
    "travel": {
        "page": PATH + "\\travel\\travel_page_urls.txt",
        "product": PATH + "\\travel\\travel_prod_urls.txt",
        "success": PATH + "\\travel\\travel_success.txt",
        "output": PATH + "\\travel\\travel_products.json"
    },
    "video_games": {
        "page": PATH + "\video_games\video_games_page_urls.txt",
        "product": PATH + "\video_games\video_games_prod_urls.txt",
        "success": PATH + "\video_games\video_games_success.txt",
        "output": PATH + "\video_games\video_games_products.json"
    },
}
