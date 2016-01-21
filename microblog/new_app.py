# coding: utf-8

from flask import Flask, request, url_for
from db import posts


app = Flask("wtf")

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
        nova_noticia = posts.insert(dados_do_formulario)
        return u"""
            <h1>Post id %s inserida com sucesso!</h1>
            <a href="%s"> Inserir novo post </a>
        """ % (nova_noticia, url_for('cadastro'))
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
               <input type="submit" value="Postar" />
           </form>
        """
        return base_html.format(title=u"Inserir nova noticia", body=formulario)


if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)

    