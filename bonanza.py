import os
import requests
from bs4 import BeautifulSoup
import json
import threading
import constants
import configurations
from Antiques import antiques_main
from Art import art_main
from Baby import baby_main
from Books import books_main
from Business import business_main
from Cameras import cameras_main
from Cell_Phones import cell_phones_main
from Coins import coins_main
from Collectibles import collectibles_main
from Computers import computers_main
from Consumer_Electronics import consumer_electronics_main
from Crafts import crafts_main
from Digital_Goods import digital_goods_main
from Dolls import dolls_main
from Dvds_movies import dvds_movies_main
from Entertainment import entertainment_main
from Everything_Else import everything_else_main
from Fashion import fashion_main
from Health_Beauty import health_beauty_main
from Home_Garden import home_garden_main
from Jewellery import jewellery_main
from Music import music_main
from Musical_Instruments import musical_instruments_main
from Parts_Accessories import parts_accessories_main
from Pet_Supplies import pet_supplies_main
from Pottery import pottery_main
from Speciality_Services import speciality_services_main
from Sporting_Goods import sporting_goods_main
from Sports_Mem import sports_mem_main
from Stamps import stamps_main
from Tickets import tickets_main
from Toys import toys_main
from Travel import travel_main
from Video_Games import video_games_main

# Stores the category names in list
category_names = configurations.CATEGORIES

# Creates main category directories in the output location
for category_name in category_names:
    try:
        os.makedirs(os.path.dirname(constants.PATH + '/' + category_name + '/'))
    except:
        pass

# Declares the threads
antiques_thread = threading.Thread(target=antiques_main.sub_cat_collect)
art_thread = threading.Thread(target=art_main.sub_cat_collect)
baby_thread = threading.Thread(target=baby_main.sub_cat_collect)
books_thread = threading.Thread(target=books_main.sub_cat_collect)
business_thread = threading.Thread(target=business_main.sub_cat_collect)
cameras_thread = threading.Thread(target=cameras_main.sub_cat_collect)
cell_phones_thread = threading.Thread(target=cell_phones_main.sub_cat_collect)
coins_thread = threading.Thread(target=coins_main.sub_cat_collect)
collectibles_thread = threading.Thread(target=collectibles_main.sub_cat_collect)
computers_thread = threading.Thread(target=computers_main.sub_cat_collect)
consumer_electronics_thread = threading.Thread(target=consumer_electronics_main.sub_cat_collect)
crafts_thread = threading.Thread(target=crafts_main.sub_cat_collect)
digital_goods_thread = threading.Thread(target=digital_goods_main.sub_cat_collect)
dolls_thread = threading.Thread(target=dolls_main.sub_cat_collect)
dvds_movies_thread = threading.Thread(target=dvds_movies_main.sub_cat_collect)
entertainment_thread = threading.Thread(target=entertainment_main.sub_cat_collect)
everything_else_thread = threading.Thread(target=everything_else_main.sub_cat_collect)
fashion_thread = threading.Thread(target=fashion_main.sub_cat_collect)
health_beauty_thread = threading.Thread(target=health_beauty_main.sub_cat_collect)
home_garden_thread = threading.Thread(target=home_garden_main.sub_cat_collect)
jewellery_thread = threading.Thread(target=jewellery_main.sub_cat_collect)
music_thread = threading.Thread(target=music_main.sub_cat_collect)
musical_instruments_thread = threading.Thread(target=musical_instruments_main.sub_cat_collect)
parts_accessories_thread = threading.Thread(target=parts_accessories_main.sub_cat_collect)
pet_supplies_thread = threading.Thread(target=pet_supplies_main.sub_cat_collect)
pottery_thread = threading.Thread(target=pottery_main.sub_cat_collect)
speciality_services_thread = threading.Thread(target=speciality_services_main.sub_cat_collect)
sporting_goods_thread = threading.Thread(target=sporting_goods_main.sub_cat_collect)
sports_mem_thread = threading.Thread(target=sports_mem_main.sub_cat_collect)
stamps_thread = threading.Thread(target=stamps_main.sub_cat_collect)
tickets_thread = threading.Thread(target=tickets_main.sub_cat_collect)
toys_thread = threading.Thread(target=toys_main.sub_cat_collect)
travel_thread = threading.Thread(target=travel_main.sub_cat_collect)
video_games_thread = threading.Thread(target=video_games_main.sub_cat_collect)

# Spawning threads to run category-specific modules, mentioned in configurations.py
for category in configurations.CATEGORIES:
    if category == 'antiques':
        antiques_thread.start()
    elif category == 'art':
        art_thread.start()
    elif category == 'baby':
        baby_thread.start()
    elif category == 'books':
        books_thread.start()
    elif category == 'business':
        business_thread.start()
    elif category == 'cameras':
        cameras_thread.start()
    elif category == 'cell_phones':
        cell_phones_thread.start()
    elif category == 'coins':
        coins_thread.start()
    elif category == 'collectibles':
        collectibles_thread.start()
    elif category == 'computers':
        computers_thread.start()
    elif category == 'consumer_electronics':
        consumer_electronics_thread.start()
    elif category == 'crafts':
        crafts_thread.start()
    elif category == 'digital_goods':
        digital_goods_thread.start()
    elif category == 'dolls':
        dolls_thread.start()
    elif category == 'dvds_movies':
        dvds_movies_thread.start()
    elif category == 'entertainment':
        entertainment_thread.start()
    elif category == 'everything_else':
        everything_else_thread.start()
    elif category == 'fashion':
        fashion_thread.start()
    elif category == 'health_beauty':
        health_beauty_thread.start()
    elif category == 'home_garden':
        home_garden_thread.start()
    elif category == 'jewellery':
        jewellery_thread.start()
    elif category == 'music':
        music_thread.start()
    elif category == 'musical_instruments':
        musical_instruments_thread.start()
    elif category == 'parts_accessories':
        parts_accessories_thread.start()
    elif category == 'pet_supplies':
        pet_supplies_thread.start()
    elif category == 'pottery':
        pottery_thread.start()
    elif category == 'speciality_services':
        speciality_services_thread.start()
    elif category == 'sporting_goods':
        sporting_goods_thread.start()
    elif category == 'sports_mem':
        sports_mem_thread.start()
    elif category == 'stamps':
        stamps_thread.start()
    elif category == 'tickets':
        tickets_thread.start()
    elif category == 'toys':
        toys_thread.start()
    elif category == 'travel':
        travel_thread.start()
    elif category == 'video_games':
        video_games_thread.start()

# Waits for the threads to be finished in order to go to next step
if antiques_thread.isAlive():
    antiques_thread.join()
if art_thread.isAlive():
    art_thread.join()
if baby_thread.isAlive():
    baby_thread.join()
if books_thread.isAlive():
    books_thread.join()
if business_thread.isAlive():
    business_thread.join()
if cameras_thread.isAlive():
    cameras_thread.join()
if cell_phones_thread.isAlive():
    cell_phones_thread.join()
if coins_thread.isAlive():
    coins_thread.join()
if collectibles_thread.isAlive():
    collectibles_thread.join()
if computers_thread.isAlive():
    computers_thread.join()
if consumer_electronics_thread.isAlive():
    consumer_electronics_thread.join()
if crafts_thread.isAlive():
    crafts_thread.join()
if digital_goods_thread.isAlive():
    digital_goods_thread.join()
if dolls_thread.isAlive():
    dolls_thread.join()
if dvds_movies_thread.isAlive():
    dvds_movies_thread.join()
if entertainment_thread.isAlive():
    entertainment_thread.join()
if everything_else_thread.isAlive():
    everything_else_thread.join()
if fashion_thread.isAlive():
    fashion_thread.join()
if health_beauty_thread.isAlive():
    health_beauty_thread.join()
if home_garden_thread.isAlive():
    home_garden_thread.join()
if jewellery_thread.isAlive():
    jewellery_thread.join()
if music_thread.isAlive():
    music_thread.join()
if musical_instruments_thread.isAlive():
    musical_instruments_thread.join()
if parts_accessories_thread.isAlive():
    parts_accessories_thread.join()
if pet_supplies_thread.isAlive():
    pet_supplies_thread.join()
if pottery_thread.isAlive():
    pottery_thread.join()
if speciality_services_thread.isAlive():
    speciality_services_thread.join()
if sporting_goods_thread.isAlive():
    sporting_goods_thread.join()
if sports_mem_thread.isAlive():
    sports_mem_thread.join()
if stamps_thread.isAlive():
    stamps_thread.join()
if tickets_thread.isAlive():
    tickets_thread.join()
if toys_thread.isAlive():
    toys_thread.join()
if travel_thread.isAlive():
    travel_thread.join()
if video_games_thread.isAlive():
    video_games_thread.join()
