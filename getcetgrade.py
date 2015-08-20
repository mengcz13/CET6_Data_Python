# -*- coding: utf-8 -*-
#大致流程 POST 到http://cet.99sushe.com/find

import json
import requests

url = 'http://cet.99sushe.com/find'
headers = {
    'Host': 'cet.99sushe.com',
	'Connection': 'keep-alive',
	'Content-Length': '36',
	'Cache-Control': 'max-age=0',
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
	'Origin': 'http://cet.99sushe.com',
	'Upgrade-Insecure-Requests': '1',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125 Safari/537.36',
	'Content-Type': 'application/x-www-form-urlencoded',
	'DNT': '1',
	'Referer': 'http://cet.99sushe.com/',
	'Accept-Encoding': 'gzip, deflate',
	'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,en-US;q=0.4'
}

class NoResultError(StandardError):
	pass

def GetCetGra(tar_id, tar_name):
	payload = {'id':tar_id, 'name':tar_name}
	r = requests.post(url, data=payload, headers=headers)
	glist = r.text.split(',')
	# if len(glist) == 1:
	# 	raise NoResultError('No Result! Please check if the id matches the name. Notice that you only need to input the first 2 charaters of the name.')
	if len(glist) == 1:
		nulldict = {'type':u'0','listening':u'0','reading':u'0','writing':u'0','total':u'0','school':u'0','name':u'0'}
		return nulldict
	else:
		gradedict = {'type':glist[0],'listening':glist[1],'reading':glist[2],'writing':glist[3],'total':glist[4],'school':glist[5],'name':glist[6]}
		return gradedict

if __name__ == '__main__':
	# id1 = '110410151204206'
	# name1 = u'孟垂正'.encode('gbk')
	id1 = raw_input()
	name1 = raw_input()
	print GetCetGra(id1,name1)