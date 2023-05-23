import json
import pytz
import nltk
import time
import re
import pprint
import requests
from InstagramAPI import InstagramAPI
from datetime import datetime

def for_string(stri):
	#replace with ""
	return "".join(i for i in stri if ord(i)<128)

def getUserProfile(result,idkeyword,alias_kyword,keyword,idproject,projectname):
	today = datetime.today()
	date_now = today.strftime("%Y-%m-%d")
	test=result['account_type']
	biography=result['biography']
	posts = {
	"userid":str(result['pk']),
	"profile_pic_url":str(result['profile_pic_url']),
	"username":str(result['username']),
	"biography":str(result['biography']),
	"external_url":str(result['external_url']),
	"media_count":int(result['media_count']),
	"totalfollowers":int(result['follower_count']),
	"idproject":int(idproject),
	"projectname":str(projectname),
	"idkeyword":int(idkeyword),
	"keyword_name":str(alias_kyword),
	"crawler_date":str(date_now),
	"sosmed":"instagram"
	}
	res = requests.post("https://wa.dad.id/profileuser", data=json.dumps(posts))
	print(posts)
	#break

def hastagdata(api,user_feed,idkeyword,alias_kyword,keywordname,idproject,projectname,totfeed):
	i = 1
	while i < 155:
		for item in user_feed:
			if 'user' in item.keys():
				usernameid=item['user']['pk']
				username=item['user']['username']
				full_name=item['user']['full_name']
				profile_pic_url=item['user']['profile_pic_url']
				utcdate = pytz.utc.localize(datetime.utcfromtimestamp(item['caption']['created_at_utc']))
				dtp=str(utcdate)
				splitdate=dtp.split(" ")
				postingdate=splitdate[0]
				postingtime=splitdate[1]
			if 'view_count' in item.keys():
				view_count=item['view_count']
			else:
				view_count=0
			likecount=item['like_count']
			if 'location' in item.keys():
				if 'lat' in item.keys():
					lat=item['lat']
					lng=item['lng']
				else:
					lat=''
					lng=''

				if 'city_name' in item.keys():
					city=item['city_name']
					address = item['address_street']
				else:
					city=''
					address =''
			else:
				lat=''
				lng=''
				city=''
				address =''

			if item['media_type']==2:
				image_url =item['video_versions'][0]['url']
			else:
				if 'image_versions2' in item.keys():
					image_url = item['image_versions2']['candidates'][0]['url']
				else:
					image_url =''

			if 'caption' in item.keys():
				try:
					caption=for_string(str(item['caption']['text']))
				except:
					caption=''
			else:
				caption=''

			if 'comment_count' in item.keys():
				comment_count=item['comment_count']
			else:
				comment_count=0

			if 'view_count' in item.keys():
				view_count=item['view_count']
			else:
				view_count=0

			# sql_check = "SELECT `idpost` FROM `ig_keywordpost` where `idpost`='"+str(item['id'])+"' and idkywords='"+str(idkeyword)+"'"
			# mycursor.execute(sql_check)
			# result = mycursor.fetchone()
			# res = es.search(index="instagram_feed", body={"query":{"match":{"_id":str(item['id'])}}})
			# result=json.dumps(res)

			worddate = str(utcdate)
			arrword=worddate.split()
			datesplit=arrword[0]
			xsplit=datesplit.split('-')
			dsplit=xsplit[0]+xsplit[1]
			# if(dsplit == '202011'):
			# 	sentimentpol=getsentimen(str(caption),str(username),str(idkeyword),str(idproject),str(item['code']))
			# 	st_sentimen=sentimentpol
			# else:
			# 	st_sentimen='0'
			# sentimentpol=getsentimen(str(caption),str(username),str(idkeyword),str(idproject),str(item['code']),str(item['id']),str(utcdate))
			# st_sentimen=sentimentpol
			st_sentimen=0
			print("3. PROCESS SENTIMEN = "+str(st_sentimen))
			#parseexst=parse_exstraction(str(caption),str(username),str(idkeyword),str(idproject),str(item['code']))
			if int(item['media_type'])==1:
				mediatypes="image"
			elif int(item['media_type'])==2:
				mediatypes="video"
			elif int(item['media_type'])==8:
				mediatypes="image"
			posts = {
			"id":str(item['id'])+"_"+str(idkeyword),
			"code":str(item['code']),
			"type_post":str(mediatypes),
			"image":str(image_url),
			"text":str(caption),
			"tot_like":int(likecount),
			"tot_share":0,
			"tot_comments":int(comment_count),
			"tot_save":0,
			"video_view":int(view_count),
			"lat":str(lat),
			"lng":str(lng),
			"username":str(username),
			"usernameid":str(item['pk']),
			"posting_date":str(postingdate),
			"posting_time":str(postingtime),
			"crawler_date":str(datetime.today()),
			"idkeyword":int(idkeyword),
			"keyword":str(alias_kyword),
			"idproject":int(idproject),
			"projectname":str(projectname),
			"status":0,
			"getLike":0,
			"sentimen":str(st_sentimen),
			"get_taging":0,
			"sosmed":"instagram"
			}
			#print(posts)
			res = requests.post("https://wa.dad.id/brandshare", data=json.dumps(posts))
			tmslp=i * 2
			print("==================================================================================================================================")
			print("1. GET HASTAG FEED Project_id:"+str(idproject)+" Date: "+str(utcdate)+" Code: "+str(item['code'])+" DatePost:"+str(utcdate)+" Loop:"+str(i))
			time.sleep(5)
			if (i == 155):
				posts_key_upd = {
				"status":str('2'),
				"idkeyword":str(idkeyword)
				}
				updkey = requests.post("https://wa.dad.id/updatekeyword", data=json.dumps(posts_key_upd))
				break
			i += 1
#GE USERDATA FEED============================================================|
def getUserDataFeed(api,user_feed,idkeyword,alias_kyword,keywordname,idproject,projectname,totfeed):
	# try:
		i = 1
		while i < int(totfeed):
			for item in user_feed:
				# print(item)
				# time.sleep(30)
				if 'user' in item.keys():
					usernameid=item['user']['pk']
					username=item['user']['username']
					full_name=item['user']['full_name']
					profile_pic_url=item['user']['profile_pic_url']
					utcdate = pytz.utc.localize(datetime.utcfromtimestamp(item['taken_at']))
					dtp=str(utcdate)
					splitdate=dtp.split(" ")
					postingdate=splitdate[0]
					postingtime=splitdate[1]
					likecount=item['like_count']
					if 'location' in item.keys():
						if 'lat' in item.keys():
							lat=item['lat']
							lng=item['lng']
						else:
							lat=''
							lng=''
						if 'city_name' in item.keys():
							city=item['city_name']
							address = item['address_street']
						else:
							city=''
							address =''
					else:
						lat=''
						lng=''
						city=''
						address =''
					if item['media_type']==2:
						image_url =item['image_versions2']['candidates'][0]['url']
					else:
						if 'image_versions2' in item.keys():
							image_url = item['image_versions2']['candidates'][0]['url']
						else:
							image_url =''
					if 'caption' in item.keys():
						try:
							caption=for_string(str(item['caption']['text']))
						except:
							caption=''
					else:
						caption=''

					if 'view_count' in item.keys():
						view_count=item['view_count']
					else:
						view_count=0

					if 'comment_count' in item.keys():
						comment_count=item['comment_count']
					else:
						comment_count=0
					# sql_check = "SELECT `idpost` FROM `ig_keywordpost` where `idpost`='"+str(item['id'])+"' and idproject='"+str(idproject)+"'"
					# mycursor.execute(sql_check)
					# result = mycursor.fetchone()
					# res = es.search(index="instagram_feed", body={"query":{"match":{"_id":str(item['id'])}}})
					# result=json.dumps(res)

					worddate = str(utcdate)
					arrword=worddate.split()
					datesplit=arrword[0]
					xsplit=datesplit.split('-')
					dsplit=xsplit[0]+xsplit[1]

					#sentimen--------------------------------------------------------------------------------------------------------------
					if(dsplit == '202011'):
						# sentimentpol=getsentimen(str(caption),str(username),str(idkeyword),str(idproject),str(item['code']),str(item['id']),str(utcdate))
						# st_sentimen=sentimentpol
						st_sentimen='0'
					else:
						st_sentimen='0'
					print("3. PROCESS STATUS SENTIMEN = "+str(st_sentimen))
					#prase exstrak---------------------------------------------------------------------------------------------------------
					#parseexst=parse_exstraction(str(caption),str(username),str(item['id']),str(idkeyword),str(idproject),str(item['code']))
					if int(item['media_type'])==1:
						mediatypes="image"
					elif int(item['media_type'])==2:
						mediatypes="video"
					elif int(item['media_type'])==8:
						mediatypes="image"

					posts = {
					"id":str(item['id'])+"_"+str(idkeyword),
					"code":str(item['code']),
					"type_post":str(mediatypes),
					"image":str(image_url),
					"text":str(caption),
					"tot_like":int(likecount),
					"tot_share":0,
					"tot_comments":int(comment_count),
					"tot_save":0,
					"video_view":int(view_count),
					"lat":str(lat),
					"lng":str(lng),
					"username":str(username),
					"usernameid":str(item['pk']),
					"posting_date":str(postingdate),
					"posting_time":str(postingtime),
					"crawler_date":str(datetime.today()),
					"idkeyword":int(idkeyword),
					"keyword":str(alias_kyword),
					"idproject":int(idproject),
					"projectname":str(projectname),
					"status":0,
					"getLike":0,
					"sentimen":str(st_sentimen),
					"get_taging":0,
					"get_phrase":0,
					"sosmed":"instagram"
					}
					res = requests.post("https://wa.dad.id/brandshare", data=json.dumps(posts))
					#post_esfeed(posts,str(item['id'])+"_"+str(idkeyword))
					print("========================================================================================================================================")
					# if(int(comment_count)>0):
					# 	getComment(api,str(item['id']),idproject,projectname,idkeyword,keywordname)
					tmslp=i * 2
					print("1. GET Posting INSTAGRAM project_id: "+str(idproject)+" ID:"+str(item['id'])+" Username:"+str(username)+" DatePost:"+str(utcdate)+" loop:"+str(i)+" sleep"+str(tmslp))
					time.sleep(2)
					if (i == int(totfeed)):
						posts_key_upd = {
						"status":str('2'),
						"idkeyword":str(idkeyword)
						}
						updkey = requests.post("https://wa.dad.id/updatekeyword", data=json.dumps(posts_key_upd))
						break
					i += 1
#GET PAGINATION USER FEED=====================================================================|
def getTotalUserFeed(api, user_id):
    user_feed = []
    next_max_id = True
    i=1
    while next_max_id:
        # first iteration hack
        if next_max_id is True:
            next_max_id = ''
        _ = api.getUserFeed(user_id, maxid=next_max_id)
        user_feed.extend(api.LastJson.get('users', []))
        next_max_id = api.LastJson.get('next_max_id', '')
        print(str(i)+' nex page id:'+str(next_max_id))
        time.sleep(11)
        if(next_max_id==""):
        	next_max_id = False
        	break
        if (i == 10):
        	next_max_id = False
        	break
        i += 1
    return user_feed
    
#GET PAGINATION HASTAG FEED=====================================================================|
def getTotalHastagFeed(api, user_id):
    user_feed = []
    next_max_id = True
    i=1
    while next_max_id:
        # first iteration hack
        if next_max_id is True:
            next_max_id = ''
        _ = api.getHashtagFeed(user_id, maxid=next_max_id)
        user_feed.extend(api.LastJson.get('users', []))
        next_max_id = api.LastJson.get('next_max_id', '')
        print(str(i)+' nex page id:'+str(next_max_id))
        time.sleep(11)
        if(next_max_id==""):
        	next_max_id = False
        	break
        if (i == 10):
        	next_max_id = False
        	break
        i += 1
    return user_feed


while True:
	pass
	resp = requests.get("https://wa.dad.id/search_project?nourut=0&engine=feed")
	print(resp.status_code)
	listrespon=resp.text
	row=json.loads(listrespon)
	if(resp.status_code==200):
		print(row)
		if(int(row["tot"])>0):
			print("START RUN PROJECT ID:"+str(row["idproject"])+" PROJECT NAME:"+str(row["project_name"])+" KEYWORD/AKUN NAME:"+str(row["keyword"]))
			idkeyword=row["idkeyword"]
			keyword=row["keyword"]
			alias_kyword=str(row["alias_kyword"])
			idproject=row["idproject"]
			projectname=row["project_name"]
			#api = InstagramAPI("ade074492020", "sepatukaca")=> chalange requere
			# api = InstagramAPI("sariningsih9841", "bantalguling")
			api = InstagramAPI("cintaoktarina", "bajubagus123")
			api.login()
			if row["type"]=='Account':
				api.searchUsername(keyword)
				resultu = api.LastJson['user']
				getUserProfile(resultu,idkeyword,alias_kyword,keyword,idproject,projectname)
				#getTotalUserFeed(api, user_id)
				# formatted_json = pprint.pformat(resultu)
				# print(formatted_json)
				#quit()

				username_id = resultu['pk']
				user_id = username_id
				
				print('GET ACOUNT POSTING ID'+str(user_id)+' Account:'+ str(keyword))
				print('-------------------------------------------------------------')
				user_feed = getTotalUserFeed(api, user_id)
				user_feed = api.getTotalUserFeed(user_id)
				print('Number of userFeed:', len(user_feed))
				getUserDataFeed(api,user_feed,idkeyword,alias_kyword,keyword,idproject,projectname,len(user_feed))
				time.sleep(100)
				print("ACCOUNT PROJECT REQUEST after 60 Munites")
			else:
				print('GET KEYWORD/HASTAG POSTING:'+ str(keyword))
				print('-------------------------------------------------------------')
				user_feed = getTotalHastagFeed(api, keyword)
				user_feed = api.getTotalHastagFeed(user_id)
				print('Number of HastagFeed:', len(user_feed))
				hastagdata(api,user_feed,idkeyword,alias_kyword,keyword,idproject,projectname,len(user_feed))
				time.sleep(100)

		else:
			posts = {
			"status_engine":int('2'),
			"idproject":int(row["idproject"])
			}
			res = requests.post("https://wa.dad.id/updateproject", data=json.dumps(posts))
			time.sleep(3600)