# -*- coding: utf-8 -*-


import settings
from flask import Flask, render_template#, request, redirect, url_for, flash
from models.ngit import NGit

app = Flask(__name__, static_path='/static')


@app.context_processor
def inject_settings():
    return vars(settings)


@app.route('/')
@app.route('/index.html')
def template_filtro():
    ngit = NGit()
    return render_template('index.html', ngit=ngit)

if __name__ == "__main__":
    app.debug=True
    app.run()
