from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
from urllib.request import Request
from urllib.parse import urlsplit
import urllib.error
import json
import argparse
import os

# file path to main directory location to store images
file_path = '/home/ericly/Documents/ComputerVision/images/gomi-shift/'

# run in command line downloadimages.py -q <your search query>
ap = argparse.ArgumentParser()
ap.add_argument('-q', '--query', required=True, help='enter search query')
args = vars(ap.parse_args())

# url for search query
url = 'http://www.bing.com/images/search?q=' + args["query"] + \
"&FORM=HDRSC2"

# new file path with the search query as the directory name
file_path = file_path + args["query"]
# print(file_path)

# make directory of search
if not os.path.exists(file_path):
	os.makedirs(file_path)
header={'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36\
 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"}

# soup = get_soup(url, header)
soup_page = soup(urlopen(Request(url, headers=header)), 'html.parser')

images = []
iusc = soup_page.find_all("a",{"class":"iusc"})
for i in iusc:
	mad = json.loads(i["mad"])
	turl = mad["turl"]
	m = json.loads(i["m"])
	murl = m["murl"]

	image_name = urlsplit(murl).path.split("/")[-1]
	print(image_name)

	images.append((image_name, turl, murl))
print("total: ", len(images), " images")

##print images
for i, (image_name, turl, murl) in enumerate(images):
    try:
        raw_img = urlopen(turl).read()

        cntr = len([i for i in os.listdir(file_path) if image_name in i]) + 1
        #print cntr

        f = open(os.path.join(file_path, image_name), 'wb')
        f.write(raw_img)
        f.close()
    except Exception as e:
        print("could not load : " + image_name)
        print(e)
        
# html parsing
# soup_page = str(soup(iusc, "html.parser"))
# text_file = open("output.txt", "w")
# text_file.write(str(soup_page))
# text_file.close()