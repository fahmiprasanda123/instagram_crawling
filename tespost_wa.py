# import logging
# import requests
# def get_access_token(url, client_id, client_secret):
#     myobj={"grant_type": "client_credentials"}
#     authh=(client_id, client_secret)
#     x = requests.post(url, data = myobj, auth = authh)
#     print(x)
#     #return x.json()
# get_access_token("http://wa.dad.id/wasendbox", "abcde", "12345")
import json
import requests
# from datetime import datetime
# now = datetime.now()
# ftime=now.strftime('%Y%m%d%H%M%S')
myobj = {
"phone_number":"6283822921384",
"type":"text",
"messages":"Code OTP qoin anda: JKT48",
"send_date":"2021-11-23",
"source":"qoin"
}
x = requests.post('https://wa.dad.id/wasendbox', data=json.dumps(myobj))
#print(x.text)

myobj2 = {
"phone_number":"62895346016941",
"type":"text",
"messages":"Code OTP qoin anda: JKT48",
"send_date":"2021-10-18",
"source":"qoin"
}
x2 = requests.post('http://wa.dad.id/wasendbox', data=json.dumps(myobj2))
print(x2.text)

myobj3 = {
"phone_number":"6281317906140",
"type":"text",
"messages":"Code OTP qoin anda: JKT48",
"send_date":"2021-10-18",
"source":"qoin"
}
x3 = requests.post('http://wa.dad.id/wasendbox', data=json.dumps(myobj3))
print(x3.text)


myobj4 = {
"phone_number":"628979238837",
"type":"text",
"messages":"Code OTP qoin anda: JKT48",
"send_date":"2021-10-18",
"source":"qoin"
}
x4 = requests.post('http://wa.dad.id/wasendbox', data=json.dumps(myobj4))
print(x4.text)

myobj5 = {
"phone_number":"6285703656866",
"type":"text",
"messages":"Code OTP qoin anda: JKT48",
"send_date":"2021-10-18",
"source":"qoin"
}
x5 = requests.post('http://wa.dad.id/wasendbox', data=json.dumps(myobj5))
print(x5.text)

myobj6 = {
"phone_number":"628119783200",
"type":"text",
"messages":"Code OTP qoin anda: JKT48",
"send_date":"2021-10-18",
"source":"qoin"
}
x6 = requests.post('http://wa.dad.id/wasendbox', data=json.dumps(myobj6))
print(x6.text)

myobj7 = {
"phone_number":"6282114605644",
"type":"text",
"messages":"Code OTP qoin anda: JKT48",
"send_date":"2021-10-18",
"source":"qoin"
}
x7 = requests.post('http://wa.dad.id/wasendbox', data=json.dumps(myobj7))
print(x7.text)

myobj8 = {
"phone_number":"628977898959",
"type":"text",
"messages":"Code OTP qoin anda: JKT48",
"send_date":"2021-10-18",
"source":"qoin"
}
x8 = requests.post('http://wa.dad.id/wasendbox', data=json.dumps(myobj8))
print(x8.text)

myobj9 = {
"phone_number":"628977898959",
"type":"text",
"messages":"Code OTP qoin anda: JKT48",
"send_date":"2021-10-18",
"source":"qoin"
}
x9 = requests.post('http://wa.dad.id/wasendbox', data=json.dumps(myobj9))
print(x9.text)

myobj10 = {
"phone_number":"6281280004521",
"type":"text",
"messages":"Code OTP qoin anda: JKT48",
"send_date":"2021-10-18",
"source":"qoin"
}
x10 = requests.post('http://wa.dad.id/wasendbox', data=json.dumps(myobj10))
print(x10.text)

myobj11 = {
"phone_number":"6287780801293",
"type":"text",
"messages":"Code OTP qoin anda: JKT48",
"send_date":"2021-10-18",
"source":"qoin"
}
x11 = requests.post('http://wa.dad.id/wasendbox', data=json.dumps(myobj11))
print(x11.text)

myobj12 = {
"phone_number":"6281291617192",
"type":"text",
"messages":"Code OTP qoin anda: JKT48",
"send_date":"2021-10-18",
"source":"qoin"
}
x12 = requests.post('http://wa.dad.id/wasendbox', data=json.dumps(myobj12))
print(x12.text)

myobj13 = {
"phone_number":"6287777162502",
"type":"text",
"messages":"Code OTP qoin anda: JKT48",
"send_date":"2021-10-18",
"source":"qoin"
}
x13 = requests.post('http://wa.dad.id/wasendbox', data=json.dumps(myobj13))
print(x13.text)

myobj14 = {
"phone_number":"628118686622",
"type":"text",
"messages":"Code OTP qoin anda: JKT48",
"send_date":"2021-10-18",
"source":"qoin"
}
x14 = requests.post('http://wa.dad.id/wasendbox', data=json.dumps(myobj14))
print(x14.text)

myobj15 = {
"phone_number":"628118306229",
"type":"text",
"messages":"Code OTP qoin anda: JKT48",
"send_date":"2021-10-18",
"source":"qoin"
}
x15 = requests.post('http://wa.dad.id/wasendbox', data=json.dumps(myobj15))
print(x15.text)

myobj16 = {
"iduser":12,
"phone_number":"6281289060272",
"type":"text",
"messages":"Code OTP qoin anda: JKT48",
"send_date":"2021-10-18",
"source":"qoin"
}
x16 = requests.post('http://wa.dad.id/wasendbox', data=json.dumps(myobj16))
print(x16.text)

myobj17 = {
"iduser":17,
"phone_number":"6281297217128",
"type":"text",
"messages":"Code OTP qoin anda: JKT48",
"send_date":"2021-10-18",
"source":"qoin"
}
x17 = requests.post('http://wa.dad.id/wasendbox', data=json.dumps(myobj17))
print(x17.text)

