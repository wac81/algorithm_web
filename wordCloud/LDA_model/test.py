# -*- coding: utf-8 -*-
from pymongo import MongoClient
from datetime import datetime
import time
import readMongo


brands = [u'奥迪']
client = MongoClient('localhost', 40000)  # 27017
db = client.lavector
collection = db.message
collection2 = db.projectInfo

begin = '2016-03-1 14:22:43'
end = '2016-03-13 14:22:43'


result_all_tags = collection2.find({'keywords': u'奔驰'})
if result_all_tags.count()==0:
    print True
#tags = result_all_tags[0]['tags']

# results = collection.find({"tags.name": {"$in": tags},"tC": {"$gt": datetime.strptime(begin, '%Y-%m-%d %H:%M:%S'),
#                                       "$lte": datetime.strptime(end, '%Y-%m-%d %H:%M:%S')}})
# for result in results:
#     print result
# print type(tags)
# for tag in tags:
#     print tag
# results = collection.find({'tags.name': '奥迪'})
# for result in results:
#     print result

#collection2 = db.projectInfo
# results = collection2.find({'keywords': u'奥迪'})
# print type(results)
# print results[0]['keywords'][0]
# print results[0]['_id']
# if results[0]['keywords'][0] == brands[0]:
#     print True
# print '======================'

'''========================================
    test writeMongo
'''

# begin = '2016-03-1 14:22:43'
# end = '2016-03-13 14:22:43'
#
# content_dic = readMongo.get_content(begin, end, u'奥迪')
# word_list = wordCloudLDAModel.get_word_cloud(content_dic['weibo'], 2)
# for value in word_list:
#     print value
# word = []
# words = []
# for item in word_list:
#     it = item.split('+')[0].split('*')
#     if it[1].strip() not in word:
#         words.append({it[1].strip(): it[0].strip()})
# for i in words:
#     print i

# dic = {'1':'奔驰skdj','2':'啊大家反馈啦就是看大家发', '3':'阿福世纪东方 i 哦哇何方'}
# for k, v in dic.items():
#     print v

# brand = '奔驰'
#
# tags = '奔驰ms'
#
# if brand in tags:
#     print True






'''============================================================
    second test: test mongodb
'''
'''
# 链接mongo数据库中
client = MongoClient('localhost', 27017)
db = client.lavector
collection = db.message
#collection.find({"tC":{"$gt":datetime.strptime(be,'%Y-%m-%d %H:%M:%S'), "$lte":datetime.strptime(end,'%Y-%m-%d %H:%M:%S')}}) :
# for r in collection.find({"tC":{"$gt":datetime.strptime("2007-03-04 21:08:12",'%Y-%m-%d %H:%M:%S'), "$lte":datetime.strptime("2017-03-04 21:08:12",'%Y-%m-%d %H:%M:%S')}}):
#     print r



print (datetime.strptime("2007-03-04 21:08:12", "%Y-%m-%d %H:%M:%S"))
results = collection.find({"tC":{"$lt":datetime.strptime("2016-03-10 00:00:12", '%Y-%m-%d %H:%M:%S')}});
for result in results:
    print result
'''

'''=============================================================
    first test
'''
'''
import jieba.posseg as pseg
import codecs
stop_words = []  # 停用此列表
stop_lines = codecs.open('stopwords.txt', encoding='UTF-8')
for stop_line in stop_lines:
    stop_words.append(stop_line.strip())

flag_list = ['v', 'vd', 'vn', 'vshi', 'vyou', 'vf', 'vx', 'vl', 'vg',
             'x', 'w', 'o', 'zg', 'uj', 'm', 'b', 'r', 'm', 'u',
             'y', 'e', 'p', 'q', 'z', 'f']  # 停用词性列表


def filter_stop_words(content):

    result = []  # 最终返回结果
    words = pseg.lcut(content)  # 分词
    for word in words:
        if word.word not in stop_words and word.flag[0] in [u'n', u'f', u'a', u'z']:
            result.append(word.word.encode('utf-8'))
    return result

content = u"启动的时候是蛮正常的,不知道后来启动报错了";
ws = pseg.lcut(content)
result = filter_stop_words(content)

for r in result:
    print r

print '===================='
for w in ws:
    print w
'''