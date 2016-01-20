#!flask/bin/python
from app import app

#from config import posts

#post = posts.find_one(id=4)
#p=post['id']
#p=post['titulo']
#print post['titulo']
app.run(debug=True, use_reloader=True)