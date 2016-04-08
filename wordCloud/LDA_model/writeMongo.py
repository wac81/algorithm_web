# -*- coding: utf-8 -*-
from pymongo import MongoClient
import time
from datetime import datetime
import readMongo
from wordCloudLDAModel import get_word_cloud

client = MongoClient('localhost', 40000)
db = client.lavector
collection = db.wordcloud

'''
向数据库中写入数据
'''

'''
按格式写入数据库
    {
    _id:ObjectId(),
    words : [
        {word : weight},
        {word : weight}
     ],
    projectId : WordCloud
    tC: ISODate(yyyy-MM-ddThh:mm:sssZ),
    source: weibo,
    brand: “奥迪”
    }
对单个字的词有一个白名单，在这个白名单中的单个字的词才能放入词云列表中
'''
white_list = [u'好', u'大', u'小', u'贵', u'快', u'棒', u'宽', u'长', u'钱', u'🈶️油']


def write_words(word_list, cal_time, brand, key, begin, end):
    '''0.002*手机 + 0.002*孩子 + 0.001*球 + 0.001*高校'''
    word = []
    words = []
    # for result in results:
    #     if result['keywords'][0] == brand:
    #         project_id = result['_id']
    #         break
    for wl in word_list:
        str = wl[1].strip().split('+')
        for s in str:
            ss = s.strip().split('*')
            if ss[1].strip() not in word:
                if len(ss[1]) == 1 and ss[1] not in white_list:
                    continue
                word.append(ss[1])
                words.append({ss[1].strip(): ss[0].strip()})

    '''取出每个主题的第一个词(可以单独写一个函数)'''
    '''
    for wl in word_list:  # 每个主题
        str = wl.strip().split('+')  # 每个主题的第一个词
        weight_word = str[0].split('*')

        if weight_word[1].strip() not in word:
            word.append(weight_word[1].strip())
            words.append({weight_word[1].strip(): weight_word[0].strip()})
    '''
    # post = {
    #     "words": words,
    #     "projectId": project_id,
    #     "tC": cal_time,
    #     "begin": datetime.strptime(begin, '%Y-%m-%d %H:%M:%S'),
    #     "end": datetime.strptime(end, '%Y-%m-%d %H:%M:%S'),
    #     "source": key,
    #     "brand": brand
    # }
    # if project_id != -1:
    #     collection.insert(post)
    #     print 'insert success !'


def write_mongo(begin, end, brand):
    """
    将指定日期内的,指定品牌,指定内容来源的词--权重写如数据库
    begin:开始日期
    end:结束日期
    brand:指定品牌
    """
    if begin > end:
        return False
    content_dic = readMongo.get_content(begin, end, brand)  # 取出特定品牌的content
    print '读取所有来源内容成功'
    for key, value in content_dic.items():
        print '分析' + key + '来源'
        if len(value) < 2:
            print 'source ' + key + ' content is too small !'
        else:
            word_list = get_word_cloud(value)  # 词--权重
            if word_list is not None:
                # 计算时的时间,转换为ISODate格式
                cal_time = datetime.strptime(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()), '%Y-%m-%d %H:%M:%S')
                write_words(word_list, cal_time, brand, key, begin, end)


'''输出lda效果，csv文件'''
import csv

def print_lda(begin, end, brand, time):

    content_dic = readMongo.get_content(begin, end, brand)  # 取出特定品牌的content
    print '读取数据成功'
    for key, value in content_dic.items():
        print key, len(value)
        if len(value) < 2:
            print 'source ' + key + ' content is too small !'
        else:
            word_list = get_word_cloud(value)  # 词--权重
            save_name = 'lda' + str(key.encode('utf-8')) + str(brand.encode('utf-8')) + '2.csv'
            csvfile = file(save_name, 'wb')
            writer = csv.writer(csvfile)
            writer.writerow(['topic_id', 'word', 'weight', 'delete_y'])
            if word_list is not None:
                for w_l in word_list:
                    print w_l[0]
                    pairs = w_l[1].split('+')
                    for pair in pairs:
                        weight_word = pair.split('*')
                        writer.writerow([str(w_l[0]), str(weight_word[1].encode('utf-8')), str(weight_word[0].encode('utf-8')), ''])
            csvfile.close()
#
#
# pos = codecs.open('./posdict.txt', encoding='utf-8').read().split('\n')
# neg = codecs.open('./negdict.txt', encoding='utf-8').read().split('\n')
# '''输出lda效果，csv文件'''
#
#

# def print_lda_filter(begin, end, brand, time):
#     content_dic = readMongo.get_content(begin, end, brand)  # 取出特定品牌的content
#     value = content_dic['xcar']
#     if len(value) < 2:
#         print 'source ' + 'xcar' + ' content is too small !'
#     else:
#         word_list = get_word_cloud(value)  # 词--权重
#         save_name = brand + str(time) + '.txt'
#         with open(save_name, 'w') as wr:
#             if word_list is not None:
#                 for w_l in word_list:
#                     result = ''
#                     wr.write('topic' + str(w_l[0]) + '#')
#                     ss = w_l[1].strip().split('+')
#                     for s in ss:
#                         ww = s.strip().split('*')
#                         if ww[1] in pos or ww[1] in neg:
#                             result += str(ww[1]) + ':' + str(ww[0]) + ' '
#                     wr.write(result + '\r\n')
