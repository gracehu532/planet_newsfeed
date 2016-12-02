#!usr/bin/local/python

from xml.etree import ElementTree
import requests
import random


def parseXML():
    url = 'http://www.news.google.com/news/section?pz=1&cf=all&ned=us&hl=en&as_scoring=r&as_maxm=2&q=cape_canaveral&as_qdr=m&as_drrb=q+&as_mind=29&as_minm=1&cf=all&as_maxd=28&output=rss'
    '''
    response = requests.get(url, stream=True)
    response.raw.decode_content = True
    events = ElementTree.iterparse(response.raw)
    for event in events:
        url = event.find('url')
        print url
    '''
    tree = ElementTree.parse(url)
    root = tree.getroot()
    for child in root:
        resp = child.find('link')
        print resp


def getJson():
    sesh = requests.Session()
    url = 'https://www.planet.com/gallery.json'
    resp = requests.get(url)
    resp = resp.json()
    return resp


#TO DO: if acquisiton date is within 6 months add to array
def getMostRecent(obj):
    images_info = []
    for i in range(10):
    	details = obj[i]
    	img = {
		'date': details['date'],
		'image': details['image'],
		'contents': details['contents'],
		'title': details['title'],
		'subtitle': details['subtitle']
	}
        images_info.append(img)
    return images_info

# return a random image in image array
def getRandomPic():
    obj = getJson()
    img_array = getMostRecent(obj)
    num = random.randrange(0, len(img_array), 1)
    image_info = img_array[num]
    return image_info

if __name__== '__main__':
    parseXML()
