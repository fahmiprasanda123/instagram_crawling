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
myobj = {
"phone_number":"6283822921384",
"type":"text",
"messages":"ABC",
"send_date":"2021-10-18",
"source":"qoin"
}
x = requests.post('http://wa.dad.id/wasendbox', data=json.dumps(myobj))
print(x.text)

myobj2 = {
"phone_number":"6281317906140",
"type":"text",
"messages":"DEF",
"send_date":"2021-10-18",
"source":"qoin"
}
x2 = requests.post('http://wa.dad.id/wasendbox', data=json.dumps(myobj2))
print(x2.text)

myobj3 = {
"phone_number":"62895346016941",
"type":"text",
"messages":"GHI",
"send_date":"2021-10-18",
"source":"qoin"
}
x3 = requests.post('http://wa.dad.id/wasendbox', data=json.dumps(myobj3))
print(x3.text)
