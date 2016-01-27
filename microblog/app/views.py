# coding: utf-8

from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm
from flask import Flask, request, url_for, jsonify, json
from config import posts
from flask import Flask, jsonify, g, request
import sqlite3 
DATABASE = './posts.db'



@app.route('/')
@app.route('/index')
def index():

    return render_template('home.html')



@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="%s", remember_me=%s' %
              (form.openid.data, str(form.remember_me.data)))
        return redirect('/index')
    return render_template('login.html',
                           title='Sign In',
                           form=form,
                           providers=app.config['OPENID_PROVIDERS'])


# por enquanto vamos usar um template html hardcoded
# mas calma! em breve falaremos  sobre os templates com Jinja2
base_html = u"""
  <html>
  <head>
      <title>{title}</title>
  </head>
  <body>
     {body}
  </body>
  </html>
"""

def query_db(query, args=(), one=False):
    cur = g.db.execute(query, args)
    rv = [dict((cur.description[idx][0], value)
               for idx, value in enumerate(row)) for row in cur.fetchall()]
    return (rv[0] if rv else None) if one else rv


@app.route("/posts/cadastro", methods=["GET", "POST"])
def cadastro():
    if request.method == "POST":
      dados_do_formulario = request.form.to_dict()
      id_novo_post = posts.insert(dados_do_formulario)
      return render_template('cadastro-sucesso.html', id_novo_post = id_novo_post)
    else:
      return render_template('cadastro-formulario.html', title = u"Inserir novo post")


#exibe o json contendo todos os posts do blog 
@app.route("/see_posts", methods=["GET", "POST"])
def see_posts(): 
    return jsonify(posts_table=[post for post in posts.all()])
  


@app.route("/post/<int:post_id>")
def post(post_id):
    post = posts.find_one(id=post_id)  # query no banco de dados
    
    return render_template('post-id.html', title= post['titulo'],
      texto = post['texto'])




    #exibe todos os posts do blog a partir de um template
@app.route("/posts/see_all", methods=["GET", "POST"])
def see_all():
    todas_as_noticias = posts.all()
    return render_template('index.html',
                           posts=todas_as_noticias,
                           title=u"Todos os Posts do nosso blog",
                           body = u"<br />.join(todas_as_noticias)")
'''
    posts_template = u"""
        <a href="/post/{post[id]}">{post[titulo]}</a>
    """
    todos_os_posts = [

        posts_template.format(post=post)
        for post in posts.all()
    ]

    return base_html.format(
        title=u"Todos os posts do nosso blog",
        body=u"<br />".join(todos_os_posts)
    ) '''


