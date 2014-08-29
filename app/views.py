# -*- coding: utf-8 -*-

from flask import render_template
from app import app, db, lm
from models import Sentence
from jNlp.jTokenize import jTokenize
from jCustom import jStructure
import base64
import random

@app.route('/')
@app.route('/index')
def index():
    st = []
    return render_template('index.html', st=st)

@app.route('/scrambler')
def scrambler():
    id = random.randint(1, 10000)
    s = Sentence.query.get(id)
    tokens = jStructure(s.content)
    data = {}
    good = ''
    ans = ''
    indexs = range(len(tokens))
    random.shuffle(indexs)
    for i, tok in enumerate(tokens):
        data[indexs[i]] = tok
        ans += tok
        good += "t%dk" % indexs[i]
    data = dict(zip(data.keys(), data.values()))
    return render_template('scrambler.html',
        data=data, good=base64.b64encode(good),
        ans=base64.b64encode(ans),
        meaning_en=base64.b64encode(s.meaning_en)
    )

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
