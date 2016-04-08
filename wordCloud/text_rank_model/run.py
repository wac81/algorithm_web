# coding:utf-8
import readMongo
brands = [u'奥迪',u'大众',u'奔驰',u'宝马',u'丰田']


################计算一周####################
# '''指定开始和结束时间'''
begin = '2016-03-01 00:00:00'
end = '2016-03-08 00:00:00'

content_dic = readMongo.get_content(begin, end, u'奥迪')




# for brand in brands:
#    print '...' + brand + '...'
#    print_lda(begin, end, brand, '7')
