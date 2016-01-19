#!flask/bin/python
from app import app
#from config import posts

#post = posts.find_one(id=1)
#print post
app.run(debug=True, use_reloader=True)