import os
from urllib.request import urlopen, Request
import bs4 as bs
import random
import urllib.request
import requests
import shutil
import sys

##### RUN THE SFW DOWNLOADER FIRST!!!!! #####


while 1==1:
    dir1 = "C:/Path/To/IMG Sorter/all_data/" #Path to all data folder
    dir2 = "C:/Path/To/IMG Sorter/New_Data/" #Path to new data folder
    dir3 = "C:/Path/To/IMG Sorter/train/"    #Path to train data folder

    list1 = os.listdir(dir1) 
    list2 = os.listdir(dir2)
    list3 = os.listdir(dir3)

    number_files = len(list1)
    if number_files > 800:
        sys.exit()
    else:
        name_file = str(number_files)

        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
        reg_url = "https://nekos.life/lewd"
        req = Request(url = reg_url, headers = headers)
        #Pinging Site For Images
        ping = urlopen(req)
        pinger = bs.BeautifulSoup(ping, 'lxml')

        source_frag2 = []

        for img in pinger.find('img').attrs['src']:
            source_frag1 = (img)
            source_frag2.append(source_frag1)

        source = ''.join(source_frag2)
        print("Downloading", source)
        #Saving File To Folder
        name = ("nsfw." + name_file + ".jpg")
        new_name = name_file + ".jpg"
        full_name1 = os.path.join(dir2, new_name)
        full_name2 = os.path.join(dir1, name)
        full_name3 = os.path.join(dir3, name)

        f = open(full_name1, 'wb')
        f.write(requests.get(source).content)
        f.close()

        f = open(full_name2, 'wb')
        f.write(requests.get(source).content)
        f.close()

        f = open(full_name3, 'wb')
        f.write(requests.get(source).content)
        f.close()
