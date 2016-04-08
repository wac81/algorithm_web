# coding:utf-8
import jieba.posseg as psg
import jieba.analyse as tr
from readMongo import get_content
import os

print os.path.abspath('.')
########加载停用词########
stop_words = open('./wordCloud/data/stopwords.txt').read().split('\r\n')

def extract_words(contents, num_words=10):
    '''每条评论提取num_words个关键词'''
    key_words = []
    for content in contents:
        key_words.append(tr.textrank(content, num_words))
    return key_words


def sort_key_words(contents, topN=100):
    '''对关键词求出现频率,排序,提取topN个词'''
    key_words = extract_words(contents)
    key_dic = {}
    for key_word in key_words:
        for word in key_word:
            if word.strip().encode('utf-8') not in stop_words:
                # if psg.lcut(word)[0].flag in [u'vn', u'z', u'nz', u'a', u'']:
                key_dic.setdefault(word, 0)
                key_dic[word] += 1
    sort_dict = sorted(key_dic.iteritems(), key=lambda x: x[1], reverse=True)
    if len(sort_dict) >= topN:
        return sort_dict[:topN]
    return sort_dict

