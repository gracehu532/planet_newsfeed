#!/usr/local/bin/python2.7


from flask import Flask, render_template, url_for, request, redirect, flash
from jinja2 import Environment, FileSystemLoader
import os
from images import *
app = Flask(__name__)


@app.route('/')
def home():
   pic = getRandomPic()
   query = pic['title'] + ' ' + pic['subtitle']
   photo = pic['image']
   return render_template('home_base.html', search_term=query, photo_url=photo)


if __name__ == '__main__':
    app.debug = True
    app.run('0.0.0.0',3000)

