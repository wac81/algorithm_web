# coding: utf-8
import readMongo
from wordCloudTextRankModel import sort_key_words
from datetime import datetime
import time
from pymongo import MongoClient
import csv

client = MongoClient('localhost', 40000)
db = client.lavector
collection = db.wordcloud
collection_project = db.projectInfo


def print_result(begin, end, brand):
    """
    往csv文件中写数据
    :param brand: 品牌
    :param end: 结束时间
    :param begin: 开始时间
    """
    if begin > end:
        return False
    content_dic = readMongo.get_content(begin, end, brand)  # 取出特定品牌的content
    print '内容读取结束'

    for key, value in content_dic.items():
        print key
        save_name = str(key.encode('utf-8')) + str(brand.encode('utf-8')) + '2.csv'
        csvfile = file(save_name, 'wb')
        writer = csv.writer(csvfile)
        writer.writerow(['word', 'frequent'])
        print '开始提取关键词和排序'
        sort_words = sort_key_words(value)
        print '提取关键词并排序结束'
        for sort in sort_words:
            writer.writerow([sort[0].encode('utf-8'), str(sort[1])])


def write_words_format(key_words, cal_time, brand, source, begin, end):
    result_all_tags = collection_project.find({'keywords': brand})
    if result_all_tags.count() == 0:
        return None, None
    project_id = result_all_tags[0]['_id']
    words = []
    for pair in key_words:
        words.append({pair[0]: pair[1]})
    post = {
        "words": words,
        "projectId": project_id,
        "tC": cal_time,
        "begin": datetime.strptime(begin, '%Y-%m-%d %H:%M:%S'),
        "end": datetime.strptime(end, '%Y-%m-%d %H:%M:%S'),
        "source": source,
        "brand": brand
    }
    return post


def write_words(key_words, cal_time, brand, source, begin, end):
    post = write_words_format(key_words, cal_time, brand, source, begin, end)
    collection.insert(post)
    print 'insert success !'


def get_wordcloud_data(begin, end, brand, source):
    cal_time = datetime.strptime(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()), '%Y-%m-%d %H:%M:%S')
    if begin > end:
        return False
    content_dic = readMongo.get_content(begin, end, brand)  # 取出特定品牌的content
    contents = content_dic[source]

    if len(contents) > 0:
        sort_words = sort_key_words(contents)
        post = write_words_format(sort_words, cal_time, brand, source, begin, end)
        # print ("write_words_format",post)
        return post
    return None


def write_mongo(begin, end, brand):
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
    cal_time = datetime.strptime(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()), '%Y-%m-%d %H:%M:%S')

    if begin > end:
        return False
    content_dic, project_id = readMongo.get_content(begin, end, brand)  # 取出特定品牌的content
    for key, value in content_dic.items():
        print key
        length = len(value)
        if length > 0:
            sort_words = sort_key_words(value)
            write_words(sort_words, cal_time, brand, key, begin, end, project_id)

if __name__ == '__main__':
    begin = '2016-02-01 00:00:00'
    end = '2016-02-10 00:00:00'
    result = get_wordcloud_data(begin, end, u'奥迪', 'autohome')
    print result


