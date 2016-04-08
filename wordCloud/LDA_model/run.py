# -*- coding: utf-8 -*-
import codecs
from writeMongo import write_mongo, print_lda#, print_lda_filter


# '''文件中指定的品牌'''
# brands = [brand.strip() for brand in codecs.open('brand.txt', encoding='UTF-8')]  # 汽车品牌
# brands.pop(0)
brands = [u'奥迪']


################计算一周####################
'''指定开始和结束时间'''
begin = '2016-02-01 00:00:00'
end = '2016-03-02 00:00:00'
for brand in brands:
   print '...' + brand + '...'
   print_lda(begin, end, brand, '30')
#################计算两周#################
# begin = '2016-02-01 00:00:00'
# end = '2016-03-02 00:00:00'
# for brand in brands:
#     print '...' + brand + '...'
#     write_mongo(begin, end, brand)

###############计算三周###################
# begin = '2016-02-01 00:00:00'
# end = '2016-02-22 00:00:00'
# for brand in brands:
#     print '...' +brand+ '...'
#     print_lda(begin, end, brand, '14')
###############计算24小时###################
# begin = '2016-03-14 00:00:00'
# end = '2016-03-15 00:00:00'
# for brand in brands:
#     print '...' +brand+ '...'
#     print_lda(begin, end, brand, '24')
###############计算48小时###################
# begin = '2016-03-14 00:00:00'
# end = '2016-03-16 00:00:00'
# for brand in brands:
#     print '...' + brand + '...'
#     print_lda(begin, end, brand, '48')
###############计算72小时###################
# begin = '2016-03-14 00:00:00'
# end = '2016-03-17 00:00:00'
# for brand in brands:
#     print '...' + brand + '...'
#     print_lda(begin, end, brand, '72')
###############计算30天#####################
# begin = '2016-02-01 00:00:00'
# end = '2016-03-03 00:00:00'
# for brand in brands:
#     print '...' + brand + '...'
#     print_lda(begin, end, brand, '30day')


# '''指定品牌'''
# for brand in brands:
#     print '...' + brand + '...'
#     write_mongo(begin, end, brand)
