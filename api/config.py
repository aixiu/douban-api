# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Aixiu
# @Time  : 2022/10/12 22:40:10

import re

# 电影名称
def vod_name(page_text):
    vod_name_ex = re.compile(r'<span.*?property="v:itemreviewed">(?P<vod_name>.*?)</span>', re.S) 
    vod_name = vod_name_ex.search(page_text)
    return vod_name.group('vod_name').strip()

# 年份
def vod_year(page_text):
    vod_year_ex = re.compile(r'<span.*?class="year">[(](?P<vod_year>.*?)[)]</span>', re.S)  # [(]里的(只是一般的括号
    vod_year = vod_year_ex.search(page_text)
    return vod_year.group('vod_year').strip()

# 语言
def vod_lang(page_text):
    vod_lang_ex = re.compile(r'<span.*?class="pl">语言:</span>(?P<vod_lang>.*?)<br/>', re.S)
    vod_lang = vod_lang_ex.search(page_text)
    return vod_lang.group('vod_lang').strip().replace(' / ', ',')

# 别名
def vod_sub(page_text):
    vod_sub_ex = re.compile(r'<span.*?class="pl">又名:</span>(?P<vod_sub>.*?)<br/>', re.S)
    vod_sub = vod_sub_ex.search(page_text)
    return vod_sub.group('vod_sub').strip().replace(' / ', ',')

# 海报
def vod_pic(page_text):
    vod_pic_ex = re.compile(r'<img.*?src="(?P<vod_pic>.*?)".*?title="点击看更多海报"')
    vod_pic = vod_pic_ex.search(page_text)
    return vod_pic.group('vod_pic').strip()

# 分类
def vod_class(page_text):
    vod_class_ex = re.compile(r'<span\s*property="v:genre">(.*?)</span>', re.S)
    vod_class_list = vod_class_ex.findall(page_text)
    vod_class = ','.join(vod_class_list).strip()
    return vod_class

# 主演
def vod_actor(page_text):
    vod_actor_ex = re.compile(r'<a.*?rel="v:starring">(.*?)</a>', re.S)
    vod_actor_list = vod_actor_ex.findall(page_text)
    vod_actor = ','.join(vod_actor_list).strip()   
    return vod_actor

# 编剧
def vod_writer(page_text):
    
    vod_writer_ex = re.compile(r'<a\s*href="/celebrity/\d+/">(.*?)</a>', re.S)
    vod_writer_list = vod_writer_ex.findall(page_text)
    vod_writer = ','.join(vod_writer_list).strip()
    
    if vod_writer == '':
        vod_writer_ex = re.compile(r'<a\s*href="/subject_search.*?">(.*?)</a>', re.S)
        vod_writer_list = vod_writer_ex.findall(page_text)
        vod_writer = ','.join(vod_writer_list).strip()
    return vod_writer

# 评分
def vod_score(page_text):
    vod_score_ex = re.compile(r'<strong\s*class="ll\s*rating_num"\s*property="v:average">(?P<score>.*?)</strong>', re.S)
    vod_score = vod_score_ex.search(page_text)
    if vod_score.group('score').strip() == '':
        return None
    else:
        return vod_score.group('score').strip()

# 内容简介
def vod_content(page_text):
    # vod_content_ex = re.compile(r'<span property="v:summary".*?>([\s\S]*?)</span>')  
    # \s 空白字符 [ \t\n\r\f\v]; \S 非空白字符 相当于 [^ \t\n\r\f\v] 。一个字符要么是空白字符要么不是.一个字符要么是词语(word)字符要么不是
    # https://blog.csdn.net/dhkfo66064/article/details/101746346
      
    # vod_content_ex = re.compile(r'<span property="v:summary".*?>(?s:(.*?))</span>')
    # 应用了此选项之后，点号（.）既可以匹配文字，还可以匹配换行符\n（不然点号是不能匹配回车的）所以，(?s)之后的.*就可以匹配“整个文本”是.*匹配文本，而不是(?s)  
    # https://zhidao.baidu.com/question/1895021914228950780.html 
     
    vod_content_ex = re.compile(r'<span\s*property="v:summary".*?>(.*?)</span>', re.S)
    vod_content_data = vod_content_ex.search(page_text)
    vod_content_format = vod_content_data.group(1).strip().replace('<br />', '')  # 获取到内容
    vod_content = re.sub('\s', '', vod_content_format)  # 去掉文本中所有空白字符
    return vod_content

# 国家地区
def vod_area(page_text):
    vod_area_ex = re.compile(r'<span\s*class="pl">制片国家/地区:</span>\s*(?P<area>.*?)\s*<br/>', re.S)
    vod_area = vod_area_ex.search(page_text)
    return vod_area.group('area').strip().replace(' / ', ',')

# 导演
def vod_director(page_text):
    vod_director_ex = re.compile(r'<a.*?rel="v:directedBy">(.*?)</a>', re.S)
    vod_director_list = vod_director_ex.findall(page_text)
    vod_director = ','.join(vod_director_list)
    return vod_director.strip().replace(' / ', ',')

# 上映时间
def vod_pubdate(page_text):
    vod_pubdate_ex = re.compile(r'<span\s*property="v:initialReleaseDate"\s*content=".*?">(.*?)</span>', re.S)
    vod_pubdate_list = vod_pubdate_ex.findall(page_text)
    vod_pubdate = ','.join(vod_pubdate_list)
    return vod_pubdate
    
# 片长
def vod_duration(page_text):    
    vod_duration_ex = re.compile(r'<span.*?property="v:runtime".*?content="(?P<dianying>.*?)">.*?</span> | <span class="pl">单集片长:</span>\s*(?P<dianshiju>.*?)分钟', re.S)
    vod_duration = vod_duration_ex.search(page_text)
    if vod_duration.group('dianying') is None:
        return vod_duration.group('dianshiju')
    else:
        return vod_duration.group('dianying')
    
# 总集数
def vod_remarks(page_text):    
    vod_remarks_ex = re.compile(r'<span\s*class="pl">集数:</span>\s*(?P<remarks>.*?)\s*<br/>', re.S)
    vod_remarks = vod_remarks_ex.search(page_text)
    try:
        return vod_remarks.group('remarks')
    except Exception:        
        return 1


# if __name__ == '__main__':
#     url = f'https://movie.douban.com/subject/{vod_douban_id}/'
    
#     flie_path = f'./douban'
    
#     # 创建一个文件夹，保存所有的图片
#     if not os.path.exists(flie_path):
#         os.mkdir('./douban/')
    
#     # 获取文件夹下所有文件名
#     file_name_list = os.listdir(flie_path)

#     #判读豆瓣ID文件是否存在如果存在，直接读文件，如果不存在爬取数据并保存
#     if f'{vod_douban_id}.json' in file_name_list:
#         with open(f'{flie_path}/{vod_douban_id}.json', mode='r', encoding='utf-8') as fp:
#             json_data = json.load(fp=fp)
#             json_dict = json.dumps(json_data, ensure_ascii=False, indent=4)
#         print(json_dict)
#     else:
#         headers = {
#             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.53'
#         }
        
#         page_text_data = requests.post(url=url, headers=headers, timeout=20)
#         page_text_data.raise_for_status()
#         page_text_data.encoding = page_text_data.apparent_encoding
#         page_text = page_text_data.text
        
#         vod_name = vod_name(page_text=page_text)
#         vod_year = vod_year(page_text=page_text)
#         vod_lang = vod_lang(page_text=page_text)
#         vod_sub = vod_sub(page_text=page_text)
#         vod_pic = vod_pic(page_text=page_text)
#         vod_class = vod_class(page_text=page_text)
#         vod_actor = vod_actor(page_text=page_text)
#         vod_writer = vod_writer(page_text=page_text)
#         vod_score = vod_score(page_text=page_text)                
#         vod_content = vod_content(page_text=page_text)
#         vod_area = vod_area(page_text=page_text)
#         vod_director = vod_director(page_text=page_text)
#         vod_pubdate = vod_pubdate(page_text=page_text)
#         vod_duration = vod_duration(page_text=page_text)
#         vod_remarks = vod_remarks(page_text=page_text)
        
#         # 国语或英文中字
#         # if '中国' or '台湾' in vod_area:
#         #     vod_remarks = "高清国语"   
#         # else:
#         #     vod_remarks = "高清中字"            
        
#         vod_total =  vod_remarks
#         vod_score_num =  random.randint(100, 1000)
#         vod_score_all =  random.randint(200, 500)
#         vod_douban_score =  vod_score        
#         vod_reurl = url   # 豆瓣地址
        


#         print('电影名称 ==> ', vod_name)
#         print('上映时间 ==> ', vod_year)
#         print('语言 ==> ', vod_lang)
#         print('别名 ==> ', vod_sub)
#         print('海报 ==> ', vod_pic)
#         print('分类 ==> ', vod_class)
#         print('主演 ==> ', vod_actor)
#         print('编剧 ==> ', vod_writer)      
#         print('评分 ==> ', vod_score)        
#         print('电影简介 ==> ', vod_content)
#         print('国家地区 ==> ', vod_area)
#         print('总集数 ==> ', vod_remarks)
#         print('导演 ==> ', vod_director)
#         print('上映时间 ==> ', vod_pubdate)
#         print('播放量 ==> ', vod_total)
#         print('播放总量 ==> ', vod_score_num)
#         print('播放总量-1 ==> ', vod_score_all)
#         print('豆瓣评分 ==> ', vod_douban_score)
#         print('片长 ==> ', vod_duration)
#         print('豆瓣地址 ==> ', vod_reurl)
#         print('豆瓣ID ==> ', vod_douban_id)
        
        
'''
解释一下：

1.正则匹配串前加了r就是为了使得里面的特殊符号不用写反斜杠了。
2.[ ]具有去特殊符号的作用,也就是说[(]里的(只是平凡的括号。
3.正则匹配串里的()是为了提取整个正则串中符合括号里的正则的内容。
4.是为了表示除了换行符的任一字符。*克林闭包，出现0次或无限次。
5.加了？是最小匹配，不加是贪婪匹配。
6.re.S是为了让.表示除了换行符的任一字符。
'''

        
        