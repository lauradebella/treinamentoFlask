# coding: utf-8

import dataset

db = dataset.connect('sqlite:///posts.db')
posts = db['posts']