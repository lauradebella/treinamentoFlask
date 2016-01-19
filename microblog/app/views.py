# coding: utf-8

from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm
from flask import Flask, request, url_for
from db import posts


@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Laura'}
    posts = [
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html',
                           title='Home',
                           user=user,
                           posts=posts)


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



@app.route("/posts/cadastro", methods=["GET", "POST"])
def cadastro():
    if request.method == "POST":
        dados_do_formulario = request.form.to_dict()
        novo_post = posts.insert(dados_do_formulario)
        return u"""
            <h1>Post id %s inserido com sucesso!</h1>
            <a href="%s"> Inserir novo post </a>
        """ % (novo_post, url_for('cadastro'))
    else:  # GET
        formulario = u"""
           <form method="post" action="/posts/cadastro">
               <label>Titulo:<br />
                    <input type="text" name="titulo" id="titulo" />
               </label>
               <br />
               <label>Texto:<br />
                    <textarea name="texto" id="texto"></textarea>
               </label>
               <input type="submit" value="Postar no blog" />
           </form>
        """
        return base_html.format(title=u"Inserir nova post", body=formulario)



@app.route("/posts/see_all", methods=["GET", "POST"])
def see_all():

    posts_template = u"""
        <a href="/post/{post[id]}">{post[titulo]}</a>
    """

    # it's a kind of magic :)
    todos_os_posts = [

        posts_template.format(post=post)
        for post in posts.all()
    ]

    return base_html.format(
        title=u"Todos os posts do nosso blog",
        body=u"<br />".join(todos_os_posts)
    )


