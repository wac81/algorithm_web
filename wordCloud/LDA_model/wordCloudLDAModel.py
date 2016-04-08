# -*- coding: utf-8 -*-
from gensim import corpora, models
import jieba.posseg as pseg
import codecs

# 加载停用词和词的词性
stop_words = []
stop_lines = codecs.open('../data/stopwords.txt', encoding='UTF-8')
for stop_line in stop_lines:
    stop_words.append(stop_line.strip())

flag_list = ['v', 'vd', 'vn', 'vshi', 'vyou', 'vf', 'vx', 'vl', 'vg', 'x', 'w', 'o',
             'zg', 'uj', 'm', 'b', 'r', 'n', 'u', 'y', 'e', 'p', 'q', 'z', 'f']


'''分词,此行标注,去除停用此和一些指定词性的词'''
def filter_stop_words(content):
    result = []  # 最终返回结果
    words = pseg.lcut(content)  # 分词
    for word in words:
        if word.word.strip() not in stop_words and word.flag[0] in [u'n']:
            result.append(word.word.strip().encode('utf-8'))
    return result


'''用lda计算主题词属于某个主题的概率'''

def get_word_cloud(documents, num_topics=10):
    texts = []
    for document in documents:
        if len(document) > 0:  # 去空
            words = filter_stop_words(document)
            if len(words) > 2:  # 过滤停用词后当一个文档中的词多于2个时
                texts.append(words)

    if len(texts) < 2:  # 至少有两片文档满足条件,否则返回None
        return None

    dictionary = corpora.Dictionary(texts)
    corpus = [dictionary.doc2bow(text) for text in texts]  # 生成词袋
    copurs_tfidf = models.TfidfModel(corpus)[corpus]
    lda = models.LdaModel(copurs_tfidf, id2word=dictionary, num_topics=num_topics)
    # 每个主题num_words个词
    word_list = lda.show_topics(num_topics=num_topics, num_words=5)  # 每个主题取前多少个词
    return word_list


'''测试'''
if __name__ == '__main__':
    docs = ['今天下午是我们的大课间活动，想知道发生了什么事吗？那就接着看吧！老师刚走进来',
            '我们就安静下来了。中午有些同学作业没写好，老师叫他们留下来。当老师说带跳绳的人可以加一百分时',
            '我心想：我怎么可以不带跳绳呢？唉，可是现在后悔又有什么用呢？“排队！”我们立马排好队伍，“你和谁搭档就和谁站在一起',
            '我们又兵荒马乱的散开去找搭档。到了操场，“男生女生各排成一排，向后转。”男生立马转过来了。老师说女生先跳，男生数着。',
            '我们各自散开去向男生借跳绳。我则是去向朱伟刚借了：因为左边太远了，差不多离我较近的人都没跳绳了。开始跳绳了，',
            '男生们帮我们数着。或许是绳子太长了，我只跳了八十七个。接下来我不说你们也知道是谁跳了吧！哈哈，对啦！就是男生跳了！',
            '我的对面是葛俊宗——嘿嘿，不知道名字写的对不对。告诉你们一个秘密哦！其实他跳了一百三十二下，我骗他说只跳了三十二下他也信',
            '做出了一个很惊讶的表情，超可爱的！可是最终我也把真相告诉了他。当老师说自由活动时，我去找薛欣妮去跳绳。可我们配合的不默契',
            '双人调最高纪录是五个！我常常笑的差点坐到地上！唉，还是自己带跳绳好啊！',
            ' 四（1）班 周袁缘名师点评：很有趣的大课间的活动哦，连老师也不禁羡慕小作者了呢。',
            '就文章的内容来说，小作者主要讲叙了自己在大课间发生的有趣的故事以及小朋友之间的互动，',
            '向读者展现了充满了活力的一批小朋友的课外生活，就文章的语言来说，很有小作者自己的特色，充满了幽默的气息，',
            '活泼的气息。希望小作者继续加油哦。']
