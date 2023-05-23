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
def getUserlike(api,idkeyword,keywordname,idproject,projectname,categoryid,category_project,dataaudience):
	i=1
	for doc in dataaudience:
		#try:
			user_id=doc['_id']
			userpk = user_id.split('_')
			print("USER ID: "+str(userpk[0]))
			userinfo = api.getUsernameInfo(userpk[0])
			result3 = api.LastJson['user']
			if result3['account_type']>1:
				email=result3['public_email']
				city=result3['city_name']
				address=for_string(str(result3['address_street']))
				phone=result3['public_phone_country_code']+result3['public_phone_number']
				latitude=result3['latitude']
				longitude=result3['longitude']
				category=result3['category']
			else:
				email=''
				city=''
				address=''
				phone=''
				latitude=''
				longitude=''
				category='person'
			#formatted_json = pprint.pformat(resultuser)
			#print(formatted_json)
			dtp=str(datetime.today())
			splitdate=dtp.split(" ")
			crawler_date=splitdate[0]
			posts = {
			"id":str(user_id),
			"username":str(result3['username']),
			"full_name":str(result3['full_name']),
			"category":str(category),
			"media_count":str(result3['media_count']),
			"followers":str(result3['follower_count']),
			"img":str(result3['profile_pic_url']),
			"email":str(email),
			"phone":str(phone),
			"city":str(city),
			"addres":str(address),
			"latitude":str(latitude),
			"longitude":str(longitude),
			"idpost":str(doc['_source']['idpost']),
			"is_private":str(result3['is_private']),
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
			#print(posts)
			totali=len(str(i))
			totali2=totali-1
			number = str(i)
			if(totali>1):
				tmslp=number[totali2]
			else:
				tmslp=number
			senddata = requests.post("https://wa.dad.id/audience", data=json.dumps(posts))
			print("SAVE PROFILE AUDIENCE USERNAME: "+str(result3['username'])+" Loop:"+str(i))
			print("sleep"+str(tmslp))
			if (int(i) == int(len(dataaudience))):
				break
			i += 1
			time.sleep(int(tmslp))
		#except:
			# print("Erorr!..return next get like")
			# time.sleep(20)

while True:
	pass
	resp = requests.get("https://wa.dad.id/search_projectlike?idproject=342&nourut=6&engine=com")
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
			api = InstagramAPI("sariningsih565", "sajadah")
			api.login()
			print('GET PROFILE LIKE ACOUNT?KEYWORD'+ str(keyword))
			print('-------------------------------------------------------------')
			get_audience = requests.get("https://wa.dad.id/profile_audience?idkeyword="+str(idkeyword))
			#print(feed.status_code)
			listrespon=get_audience.text
			jsondata=json.loads(listrespon)
			dataaudience=jsondata['hits']['hits']
			if(get_audience.status_code==200):
				if(int(jsondata['hits']['total']['value'])==0):
					print("data Audience dengan followers=empy KOSONG!!")
					time.sleep(6600)
				else:
					getUserlike(api,idkeyword,keyword,idproject,projectname,categoryid,category,dataaudience)
					time.sleep(100)
	else:
		print("DATA PROJECT NOT RESPONSE")
		time.sleep(3600)

				
			