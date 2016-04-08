# coding:utf-8
import codecs
from datetime import datetime
import time
import keras

import jieba.posseg as psg

if None is not None:
    print True
# print psg.lcut(u'漂亮')[0].flag
# if psg.lcut(u'漂亮')[0].flag not in [u'n']:
#     print True


# stop_words = open('../data/stopwords.txt').read().split('\r\n')
# print type(stop_words)
#
# for word in stop_words:
#     print word


# a_dict = {'a':1, 'b':2, 'c':3}
# print sorted(a_dict.iteritems(), key=lambda x: x[1], reverse=True)
#

'''
dic = {'1':'a', '2':'b'}
print dic.keys()
cal_time = datetime.strptime(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())), '%Y-%m-%d %H:%M:%S')
#print cal_time
#e=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
#iso = datetime.strptime(e,'%Y-%m-%d %H:%M:%S')
print type(cal_time)


endTime = datetime.strptime('2016-03-13 00:00:00','%Y-%m-%d %H:%M:%S')
cal_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
t = datetime.strptime(cal_time, '%Y-%m-%d %H:%M:%S')
print cal_time
print endTime
print t
# brands = [brand.strip() for brand in codecs.open('brand.txt', encoding='UTF-8')]
# brands.pop(0)
# for brand in brands:
#     print brand, len(brand.strip())
'''