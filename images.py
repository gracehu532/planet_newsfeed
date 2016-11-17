#!usr/bin/local/python

import requests
import random


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

#TO DO: return a random image in image array
def getRandomPic(img_array):
    num = random.randrange(0, len(img_array), 1)
    return img_array[num]    


def main():
    obj = getJson()
    image_array = getMostRecent(obj)
    img = getRandomPic(image_array)
    print img['image']


if __name__ == '__main__':
    main()
    
