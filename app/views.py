# -*- coding: utf-8 -*-

from flask import render_template
from app import app
from jNlp.jTokenize import jTokenize

@app.route('/')
@app.route('/index')
def index():
    targets = [u"つまり"]
    input_sentence = u'私は彼を５日前、つまりこの前の金曜日に駅で見かけた'
    list_of_tokens = jTokenize(input_sentence)
    print list_of_tokens
    st = []
    txt = u''
    for tk in list_of_tokens:
        print tk
        if tk not in targets:
            txt += tk
        else:
            print txt
            st.append(txt)
            st.append(u"＿＿")
            st.append(u"＿＿")
            st.append(u"＿★＿")
            st.append(u"＿＿")
            txt = u''
    print txt
    if txt:
        st.append(txt)
    print '--'.join(list_of_tokens).encode('utf-8')
    return render_template('index.html', st=st)

@app.route('/scrambler')
def scrambler():
    data = {
        1: '一日たりとも', 
        2: '我々は',
        3: '水なしには',
        4: 'いきられない'
    }
    return render_template('scrambler.html', data=data)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
