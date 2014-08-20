#!venv/bin/python
# -*- coding: utf-8 -*-
import sys
import xml.etree.cElementTree as etree
import re

#Package imports
from jNlp.jCabocha import *

def add_target(jCabocha_tree,target_sent,**kwargs):
    """
    Following is to mark a target word
    Not called
    See jCabocha_with_target()
    """
    if kwargs.has_key('id'): attach_id = kwargs['id']
    else: attach_id = 'unknown'
    start_pos = len(target_sent.split('*')[0])
    tw = target_sent.split('*')[1]
    sent = u''
    for chunk in jCabocha_tree.getchildren():
        for tok in chunk:
            if tw in tok.text and len(sent) >= start_pos -3:
                tok.set("target", attach_id)
                return jCabocha_tree
            else: sent += tok.text
    return jCabocha_tree

def jStructure(target_sent):
    default_marker = '*'
    target = target_sent.replace(default_marker,'')
    jCabocha = JCabocha()
    sentence = jCabocha.structure(target).split("\n")
    result = []
    for token in sentence:
        a = re.sub(r"\-+D", "", token.strip())
        a = a.replace("|", "")
        a = a.strip()
        if a and "EOS" not in a:
            result.append(a)
    return result

if __name__ == '__main__':
    a = u'私は彼を５日前、つまりこの前の金曜日に駅で見かけた'
    print jStructure(a)
