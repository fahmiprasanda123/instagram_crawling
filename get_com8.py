import json
import time
import pytz
import re
#import mysql.connector
#import cv2
import math
import argparse
import pprint
import requests
from InstagramAPI import InstagramAPI
from datetime import datetime
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
#from textblob import TextBlob

def for_string(stri):
	return "".join(i for i in stri if ord(i)<128)

def highlightFace(net, frame, conf_threshold=0.7):
	frameOpencvDnn=frame.copy()
	frameHeight=frameOpencvDnn.shape[0]
	frameWidth=frameOpencvDnn.shape[1]
	blob=cv2.dnn.blobFromImage(frameOpencvDnn, 1.0, (300, 300), [104, 117, 123], True, False)

	net.setInput(blob)
	detections=net.forward()
	faceBoxes=[]
	for i in range(detections.shape[2]):
		confidence=detections[0,0,i,2]
		if confidence>conf_threshold:
			x1=int(detections[0,0,i,3]*frameWidth)
			y1=int(detections[0,0,i,4]*frameHeight)
			x2=int(detections[0,0,i,5]*frameWidth)
			y2=int(detections[0,0,i,6]*frameHeight)
			faceBoxes.append([x1,y1,x2,y2])
			cv2.rectangle(frameOpencvDnn, (x1,y1), (x2,y2), (0,255,0), int(round(frameHeight/150)), 8)
	return frameOpencvDnn,faceBoxes

#GE USERDATA FEED============================================================|
def getComments(api,idkeyword,keywordname,idproject,projectname,categoryid,category,datafeed):
	print("1. GET COMMENTS")
	for item in datafeed:
		media_id=str(item['_id'])
		code=str(item['_source']["code"])
		posting_date=str(item['_source']["posting_date"])
		tot_comments=int(item['_source']["tot_comments"])
		print(tot_comments)
		if(tot_comments > 0):
			until_date = str(datetime.today())
			count = 20
			#has_more_comments = True
			max_id = ''
			comments = []
			_ = api.getMediaComments(media_id, max_id=max_id)
			datap=api.LastJson
			print(len(api.LastJson['comments']))
			i=1
			for c in api.LastJson['comments']:
				textcomment=for_string(str(c['text']))
				utcdate = pytz.utc.localize(datetime.utcfromtimestamp(c['created_at_utc']))
				#proses phrase jika lebih dari 3 charakter
				posts_com = {
				"id":str(media_id)+'_'+str(utcdate),
				"pk":str(c['user']['pk']),
				"content_link":"https://www.instagram.com/p/"+str(code),
				"date_content":str(posting_date),
				"text":str(textcomment),
				"user_id":int(c['user_id']),
				"username":str(c['user']['username']),
				"full_name":str(c['user']['full_name']),
				"profile_pic_url":str(c['user']['profile_pic_url']),
				"idproject":int(idproject),
				"projectname":str(projectname),
				"idkeyword":int(idkeyword),
				"keyword_name":str(keywordname),
				"media_id":str(media_id),
				"date_comment":str(utcdate),
				"sentiment":0,
				"status_phrase":0
				}
				print(posts_com)
				res = requests.post("https://wa.dad.id/comments", data=json.dumps(posts_com))
				# if(len(str(textcomment)) > 3):
				# 	save_phrase(str(textcomment),str(c['user']['username']),int(idkeyword),str(keywordname),int(idproject),str(projectname),code,media_id,posting_date)
				if (i == int(len(api.LastJson['comments']))):
					posts_key_upd = {"id":str(media_id)}
					updkey = requests.post("https://wa.dad.id/updatefeedcom", data=json.dumps(posts_key_upd))
					break
				i += 1
				time.sleep(20)
			else:
				print('tot_comments = 0')
				time.sleep(20)

#GET KEYWORD/ACOUNT BY PROJECT========================================================|
while True:
	pass
	#resp = requests.get("https://wa.dad.id/search_project?nourut=0&engine=com")
	resp = requests.get("https://wa.dad.id/search_projectlike?idproject=280&nourut=8&engine=com")
	print(resp.status_code)
	listrespon=resp.text
	row=json.loads(listrespon)
	if(resp.status_code==200):
		print(row)
		if(int(row["tot"])>0):
			print("START RUN PROJECT ID:"+str(row["idproject"])+" PROJECT NAME:"+str(row["project_name"])+" KEYWORD/AKUN NAME:"+str(row["keyword"]))
			idkeyword=row["idkeyword"]
			keyword=row["keyword"]
			idproject=row["idproject"]
			projectname=row["project_name"]
			categoryid=row["categoryid"]
			category=row["category"]
			#api = InstagramAPI("testingakun16", "tes123456")
			api = InstagramAPI("dadtest2021", "tes123456")#pinjam ke like 8
			api.login()
			print('GET COMMENT ACOUNT?KEYWORD'+ str(keyword))
			print('-------------------------------------------------------------')
			feed = requests.get("https://wa.dad.id/search_feed?nourut=8&idkeyword="+str(idkeyword)+"&engine=com&sosmed=instagram")
			#print(feed.status_code)
			listrespon=feed.text
			jsondata=json.loads(listrespon)
			datafeed=jsondata['hits']['hits']
			if(feed.status_code==200):
				if(int(len(jsondata['hits']['hits']))==0):
					print("data feed dengan Status=0 KOSONG!!")
					time.sleep(6600)
				else:
					getComments(api,idkeyword,keyword,idproject,projectname,categoryid,category,datafeed)
					time.sleep(100)
		else:
			posts = {
			"status_engine":int('3'),
			"idproject":int(row["idproject"])
			}
			res = requests.post("https://wa.dad.id/updateproject", data=json.dumps(posts))
			time.sleep(3600)