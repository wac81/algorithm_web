# -*- coding: utf-8 -*-
from pymongo import MongoClient
from datetime import datetime


# 内容字数限制
content_limit = 10  # 内容字数限制

# 链接mongo数据库中
client = MongoClient('localhost', 40000)  # 27017
db = client.lavector
collection = db.message
collection_project = db.projectInfo
'''获取指定时间,指定品牌,各种来源的评论内容
    begin:开始时间
    end:结束时间
    brand:指定品牌
    ==============================
    source一共包括:autohome,xcar,sina,weibo,weixin,zhihu
'''
def get_content(begin, end, brand):
    content_dic = {}

    result_all_tags = collection_project.find({'keywords': brand})
    if result_all_tags.count() == 0:
        return None, None
    brand_tags = result_all_tags[0]['tags']
    project_id = result_all_tags[0]['_id']
    results = collection.find({"tags.name": {"$in": brand_tags},"tC": {"$gt": datetime.strptime(begin, '%Y-%m-%d %H:%M:%S'),
                                      "$lte": datetime.strptime(end, '%Y-%m-%d %H:%M:%S')}})
    print '查询数据库结束'
    count = 1
    for result in results:
        print count
        count += 1
        if 'content' in result.keys() and result['content'] > content_limit:
            '''===========================================================
                    根据tags判断
            '''
            if result['site'] == 'weibo':
                if 'tags' in result.keys() and len(result['tags']) != 0 and 'name' in result['tags'][0].keys():
                    if brand in result['tags'][0]['name']:
                        content_dic.setdefault('weibo', [])
                        content_dic['weibo'].append(result['content'])

            elif result['site'] == 'sina':
                if 'tags' in result.keys() and len(result['tags']) != 0 and 'name' in result['tags'][0].keys():
                    if brand in result['tags'][0]['name']:
                        content_dic.setdefault('sina', [])
                        content_dic['sina'].append(result['content'])

            elif result['site'] == 'xcar':
                if brand in result['tags'][0]['name']:
                    content_dic.setdefault('xcar', [])
                    content_dic['xcar'].append(result['content'])

            elif result['site'] == 'autohome':
                if len(result['tags']) != 0 and 'name' in result['tags'][0].keys():
                    if brand in result['tags'][0]['name']:
                        content_dic.setdefault('autohome', [])
                        content_dic['autohome'].append(result['content'])

            # elif result['site'] == 'weixin':
            #     if brand in result['tags'][0]['name']:
            #         content_dic.setdefault('weixin', [])
            #         content_dic['weixin'].append(result['content'])

            elif result['site'] == 'zhihu':
                if 'tags' in result.keys() and len(result['tags']) != 0 and 'name' in result['tags'][0].keys():
                    if brand in result['tags'][0]['name']:
                        content_dic.setdefault('zhihu', [])
                        content_dic['zhihu'].append(result['content'])
    return content_dic
