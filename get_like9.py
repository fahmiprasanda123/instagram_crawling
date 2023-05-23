import json
import time
import pytz
#import cv2
import math
import argparse
import pprint
import requests
from InstagramAPI import InstagramAPI
from datetime import datetime

def for_string(stri):
	#replace with ""
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
def getUserlike(api,idkeyword,keywordname,idproject,projectname,categoryid,category_project,datafeed):
	print('Data feed LIKE')
	for doc in datafeed:
		mid=doc['_id']
		x = mid.split('_')
		if(len(x)==3):
			media_id=x[0]+'_'+x[1]
		else:
			media_id=mid
		likecount=doc['_source']['tot_like']
		_ = api.getMediaLikers(media_id)
		resultuser = api.LastJson['users']
		totalmedialike=len(resultuser)
		print("TOTAL LIKE"+str(totalmedialike))
		#formatted_json = pprint.pformat(resultuser)
		#print(formatted_json)
		dtp=str(datetime.today())
		splitdate=dtp.split(" ")
		crawler_date=splitdate[0]
		i=1
		for item in resultuser:
			#try:
				private_status=item['is_private']
				musername=item['username']
				chk = requests.get("https://wa.dad.id/chek_audience?idproject="+str(idproject)+"&musername="+str(musername)+"")
				chkrespon=chk.text
				chekaudience=json.loads(chkrespon)
				audience_total=chekaudience['hits']['total']['value']
				if(audience_total==0):
					user_id=item['pk']
					username=item['username']
					full_name=item['full_name']
					profile_pic_url=item['profile_pic_url']
					if(private_status==False):
						posts = {
						"id":str(user_id)+'_'+str(idproject),
						"username":str(username),
						"full_name":str(full_name),
						"category":'',
						"media_count":'none',
						"followers":'none',
						"img":str(profile_pic_url),
						"email":'',
						"phone":'',
						"city":'',
						"addres":'',
						"latitude":'',
						"longitude":'',
						"idpost":str(mid),
						"is_private":str(private_status),
						"idkeyword":str(idkeyword),
						"keyword":str(keywordname),
						"idproject":str(idproject),
						"projectname":str(projectname),
						"categoryid":int(categoryid),
						"category_project":str(category_project),
						"gender":'',
						"umur":'',
						"range_umur":'',
						"status_dm":0,
						"status_wa":0,
						"status_email":0,
						"crawler_date":str(crawler_date)
						}
						print(posts)
						#print("SAVE USER LIKE:"+str(item['pk'])+" Username"+str(item['username'])+" latitude"+str(latitude)+" Loop:"+str(i))
						senddata = requests.post("https://wa.dad.id/audience", data=json.dumps(posts))
					else:
						print("USERNAME: "+str(username)+" is_private=True Note Save"+" Loop:"+str(i))
				else:
					print('Jumlah followers Database sudah ada'+' Loop:'+str(i))
				if (int(i) == int(totalmedialike)):
					posts_feed_upd = {"id":str(mid)}
					updatefeed = requests.post("https://wa.dad.id/updatefeedlike", data=json.dumps(posts_feed_upd))
					print("LIMIT MAX")
					break
				i += 1
				time.sleep(5)
			# except:
			# 	print("Erorr!..return next get like")

while True:
	pass
	resp = requests.get("https://wa.dad.id/search_projectlike?idproject=280&nourut=9&engine=com")
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
			api = InstagramAPI("dadtest2021", "tes123456")
			api.login()
			print('GET LIKE ACOUNT?KEYWORD'+ str(keyword))
			print('-------------------------------------------------------------')
			feed = requests.get("https://wa.dad.id/search_feed?nourut=8&idkeyword="+str(idkeyword)+"&engine=like&sosmed=instagram")
			#print(feed.status_code)
			listrespon=feed.text
			jsondata=json.loads(listrespon)
			datafeed=jsondata['hits']['hits']
			if(feed.status_code==200):
				if(int(len(jsondata['hits']['hits']))==0):
					print("data feed dengan StatusLike=0 KOSONG!!")
					time.sleep(6600)
				else:
					getUserlike(api,idkeyword,keyword,idproject,projectname,categoryid,category,datafeed)
					time.sleep(100)
	else:
		print("DATA PROJECT NOT RESPONSE")
		time.sleep(3600)

				
			