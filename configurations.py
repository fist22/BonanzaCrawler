DATABASE = {
  "username": "root",
  "host": "localhost",
  "password": "<to_be_replaced_tih_password>",
  "port": 4444,
  "database": "alldata"
}


PATH = '/home/ubuntu/BonanzaData'

# 1 to configurable number of PRODUCTS' details
# 0 to collect ALL PRODUCTS' details
PRODUCTS_FLAG = 1

# Number of product-details to be collected
# For this to work PRODUCTS_FLAG should be equals to 1
NO_OF_PRODUCTS = 500

# 1 to write to single FILE
# 2 to write to DATABASE
# 3 to write to INDIVIDUAL FILES
STORAGE_FLAG = 2


# POSSIBLE VALUES:
# antiques, art, baby, books, business, cameras, cell_phones, coins, collectibles, computers, consumer_electronics,
# crafts, digital_goods, dolls, dvds_movies, entertainment, everything_else, fashion, health_beauty, home_garden,
# jewellery, music, musical_instruments, parts_accessories, pet_supplies, pottery, speciality_services, sporting_goods, sports_mem,
# stamps, tickets, toys, travel, video_games
CATEGORIES = ['books','computers','business']
