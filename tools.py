# -*- coding: utf-8 -*-
"""
Created on Tues Mar 23 2017

@author: Lily
"""
# data cleaning for zhihu_live(v1.2)

# import modules
import re
import pandas as pd

# define functions

# pick int from string


def pick_int(x):
    m = re.compile(r'\d+')
    num = m.findall(x)[0]
    if x == '0':
        x = None
    else:
        x = int(num)
    return x

# count how many words the content has

words = []


def count_words(text):
    text = text.decode('utf-8')
    num = 0
    for i in text:
        if i not in ' \n!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~':
            num += 1
    words.append(num)
    return words

# import data
df_ended = pd.read_csv('live_ednde.csv')
df_ongo = pd.read_csv('live_ongoing.csv')

# deal with data


def main():
    # change 0 into nan
    global df_ongo , df_ended , words
    df_ended = df_ended[df_ended!=0]
    df_ongo = df_ongo[df_ongo!=0]

    # apply tools
    # apply pick int
    df_ongo['费用'] = df_ongo['费用'].map(pick_int)
    df_ended['费用'] = df_ended['费用'].map(pick_int)

    # apply count words
    df_ongo['介绍'].map(count_words)
    s1 = pd.DataFrame({'介绍字数': words})
    df_ongo = pd.concat([df_ongo ,s1],axis=1)

    words=[]
    df_ended['介绍'].map(count_words)
    s2 = pd.DataFrame({'介绍字数': words})
    df_ended = pd.concat([df_ended ,s2],axis=1)

    # save
    df_ongo.to_csv('ongoing.csv')
    df_ended.to_csv('ended.csv')

if 'name' == 'main':
    main()